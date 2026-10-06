import os
import re

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procura onde está a subseção do Objetivo Geral (ignorando maiúsculas/minúsculas)
        if re.search(r'\\subsection\{OBJETIVO GERAL\}', content, re.IGNORECASE):
            # Se ainda não tiver o Capítulo de Objetivos, injeta ele!
            if r'\section{OBJETIVOS}' not in content.upper():
                content = re.sub(r'(\\subsection\{OBJETIVO GERAL\})', r'\\section{OBJETIVOS}\n\1', content, flags=re.IGNORECASE)
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Sucesso! Os Objetivos foram isolados em um novo Capítulo no arquivo: {file}")
                encontrou = True

if not encontrou:
    print("⚠️ Não foi necessário ajustar, ou o formato já estava correto.")
