import os
import re

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procura a menção aos autores e ao modelo no mesmo arquivo
        if 'Kheyfets e Mukhin' in content and 'Flexible Strings Model' in content:
            
            # Regex robusto para capturar a primeira parte da frase (mantendo o número da figura intacto) e substituir o resto
            padrao = r'(A constância energética aferida na Figura \d+\.\d+, em contraste com a contração física\s*da membrana, encontra explicação na mecânica estatística por intermédio) das elaborações de\s*Kheyfets e Mukhin referentes à Teoria de Cordas Flexíveis \(Flexible Strings Model\) \[7\]\..*?volume livre associado à fase fluida.*?\[7\]\.'
            
            # Novo texto lapidado e com formatação matemática
            novo_paragrafo = r"\g<1> da Teoria de Cordas Flexíveis (\textit{Flexible Strings Model}) [7]. Este modelo postula que as caudas hidrocarbônicas dos fosfolipídios (DPPC e DSPC) podem ser tratadas como cordas vibrantes flexíveis, que oscilam impulsionadas pela energia térmica ($k_{B}T$), criando o volume livre associado à fase fluida ($L_{\alpha}$) [7]."
            
            content_atualizado = re.sub(padrao, novo_paragrafo, content, flags=re.DOTALL | re.IGNORECASE)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content_atualizado)
            
            print(f"✅ Trecho da referência [7] (Teoria de Cordas Flexíveis) atualizado com sucesso no arquivo: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ Não encontrei o trecho. Verifique se ele já não foi alterado.")
