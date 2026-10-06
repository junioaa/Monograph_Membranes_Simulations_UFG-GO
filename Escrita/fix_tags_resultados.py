import os
import re

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'Permuta Entálpica e a Dinâmica de Compensação do Colesterol' in content:
            
            # 1. Corrige o artefato de quebra de página 'coxlii\nlesterol' -> 'colesterol'
            content = re.sub(r'co\s*xlii\s*\n?\s*lesterol', 'colesterol', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'coxlii\s*lesterol', 'colesterol', content, flags=re.DOTALL | re.IGNORECASE)
            
            # 2. Substitui os marcadores de interrogação [? ] pelas referências e citações corretas
            content = content.replace(r'para −565,7 kJ/mol (com 30% de colesterol) [? ].', r'para $-565,7$ kJ/mol (com 30% de colesterol) (Tabela~\ref{tab:tabela_energias}).')
            content = content.replace(r'para -565,7 kJ/mol (com 30% de colesterol) [? ].', r'para $-565,7$ kJ/mol (com 30% de colesterol) (Tabela~\ref{tab:tabela_energias}).')
            
            content = content.replace(r'presentes no DPPC e DSPC [? ].', r'presentes no DPPC e DSPC [8].')
            content = content.replace(r'graus de liberdade rotacionais [? ].', r'graus de liberdade rotacionais [8].')
            content = content.replace(r'estabilidade no núcleo apolar [? ].', r'estabilidade no núcleo apolar [8].')
            content = content.replace(r'profundezas da bicamada [? ].', r'profundezas da bicamada [9].')
            
            # Ajusta a grafia do -OH e de trade-off para o padrão correto do LaTeX
            content = content.replace(r'(-OH)', r'($-\text{OH}$)')
            content = content.replace(r'(tradeoff)', r'(\textit{trade-off})')
            content = content.replace(r'(Lo)', r'($L_{o}$)')

            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Bloco de permuta entálpica e compensação do colesterol corrigido com sucesso em: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ Não encontrei o trecho com os marcadores '[? ]'. Certifique-se de que o texto não foi alterado previamente.")
