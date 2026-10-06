import os
import re

# Expressão regular flexível que ignora quebras de linha e espaços extras
padrao = r'Agradeço primeiramente ao meu orientador,\s*Prof\.\s*Dr\.\s*Wesley Bueno Cardoso,\s*pela\s*confiança\s*e\s*direcionamento\s*ímpar\s*ao\s*longo\s*deste\s*trabalho\.'

novo_texto = r'Agradeço primeiramente ao meu orientador, Prof. Dr. Wesley Bueno Cardoso, pela confiança e direcionamento ao longo deste trabalho.'

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if re.search(padrao, content, flags=re.IGNORECASE):
            content_atualizado = re.sub(padrao, novo_texto, content, flags=re.IGNORECASE)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content_atualizado)
            
            print(f"✅ Agradecimento atualizado com sucesso no arquivo: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ Não encontrei a frase. Verifique se ela já foi alterada ou se está escrita de forma diferente.")
