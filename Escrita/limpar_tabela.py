import re

with open('anexos.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
vistos = set()
in_table = False

for l in lines:
    # 1. Detecta o início da tabela e ajusta a fonte e as colunas
    if r'\begin{longtable}' in l or r'\begin{tabular}' in l:
        in_table = True
        if r'\footnotesize' not in "".join(new_lines[-2:]):
            new_lines.append(r'\footnotesize' + '\n')
        # Força exatamente 6 colunas centralizadas com bordas
        l = re.sub(r'\{([\|lrcp]+)\}', '{|c|c|c|c|c|c|}', l)
        new_lines.append(l)
        continue
        
    # 2. Detecta o fim da tabela e restaura a fonte do texto
    if r'\end{longtable}' in l or r'\end{tabular}' in l:
        in_table = False
        new_lines.append(l)
        new_lines.append(r'\normalsize' + '\n')
        continue

    # 3. Processa apenas as linhas com dados numéricos
    if in_table and '&' in l and r'\pm' in l and 'textbf' not in l:
        parts = l.split('&')
        if len(parts) >= 6:
            sys = parts[0].strip()
            prop = parts[1].strip()
            temp = parts[2].strip()
            
            # Cria um "RG" único para a linha (ex: CHOL_3_100:0_290K)
            row_id = f"{sys}_{prop}_{temp}"
            
            # Só escreve a linha se esse "RG" for inédito
            if row_id not in vistos:
                vistos.add(row_id)
                
                # Função para limpar sujeiras e garantir que o número está dentro do $ $
                def clean_math(val):
                    val = re.sub(r'(\\\\|\tabularnewline|\s*\\midrule|\s*\\hline).*', '', val)
                    val = val.replace('$', '').strip()
                    return f"${val}$"

                c_val = clean_math(parts[3])
                lj_val = clean_math(parts[4])
                
                raw_last = parts[5]
                tot_val = clean_math(raw_last)
                
                # Preserva a quebra de linha original do LaTeX
                end_match = re.search(r'(\\\\|\tabularnewline)(\s*\\midrule|\s*\\hline)?', raw_last)
                end_marker = end_match.group(0) if end_match else r'\\'
                
                # Reconstrói a linha com espaçamento limpo e alinhamento exato
                clean_line = f"{sys} & {prop} & {temp} & {c_val} & {lj_val} & {tot_val} {end_marker}\n"
                new_lines.append(clean_line)
        else:
            new_lines.append(l)
    else:
        new_lines.append(l)

with open('anexos.tex', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ Limpeza pesada concluída! Duplicatas removidas e alinhamento A4 corrigido.")
