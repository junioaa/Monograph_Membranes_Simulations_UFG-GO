import os
import re

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modificado = False

        # Correção 1: Proteger o link do GitHub da formatação matemática
        link_cru = r'https://github.com/junioaa/TCC_Membranes_UFG'
        link_protegido = r'\url{https://github.com/junioaa/TCC_Membranes_UFG}'
        if link_cru in content and link_protegido not in content:
            content = content.replace(link_cru, link_protegido)
            modificado = True

        # Correção 2: Forçar a substituição dos marcadores perdidos na Permuta Entálpica
        if 'Permuta Entálpica' in content:
            content = re.sub(r'\(com 30% de colesterol\)\s*[\(\[]\?\s*[\)\]]', r'(com 30\% de colesterol) (Tabela~\\ref{tab:tabela_energias})', content)
            content = re.sub(r'presentes no DPPC e DSPC\s*[\(\[]\?\s*[\)\]]', r'presentes no DPPC e DSPC [8]', content)
            content = re.sub(r'graus de liberdade rotacionais\s*[\(\[]\?\s*[\)\]]', r'graus de liberdade rotacionais [8]', content)
            content = re.sub(r'estabilidade no núcleo apolar\s*[\(\[]\?\s*[\)\]]', r'estabilidade no núcleo apolar [8]', content)
            content = re.sub(r'profundezas da bicamada\s*[\(\[]\?\s*[\)\]]', r'profundezas da bicamada [9]', content)
            modificado = True

        if modificado:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Bugs de formatação corrigidos no arquivo: {file}")
