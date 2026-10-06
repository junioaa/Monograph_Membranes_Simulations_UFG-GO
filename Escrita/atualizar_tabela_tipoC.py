import os
import re
import math

arquivo = 'anexos.tex' # <--- Confirme se o nome do arquivo que contém a Tabela 5.1 é este mesmo

if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    novas_linhas = []
    for linha in linhas:
        # 1. Adicionar espaço para uma coluna extra no alinhamento do LaTeX
        if r'\begin{longtable}' in linha or r'\begin{tabular}' in linha:
            linha = re.sub(r'\{([\|lrc]+)\}', lambda m: '{' + m.group(1).replace('}', '') + 'c|}' if not m.group(1).endswith('c|}') else m.group(0), linha)
            
        # 2. Atualizar o cabeçalho para adicionar "Energia Total"
        if 'Lennard-Jones' in linha and 'Coulomb' in linha and '&' in linha:
            if 'Total' not in linha:
                linha = linha.replace('Lennard-Jones $(kJ/mol)$', 'Lennard-Jones $(kJ/mol)$ & Total $(kJ/mol)$')
                linha = linha.replace('Lennard-Jones (kJ/mol)', 'Lennard-Jones (kJ/mol) & Total (kJ/mol)')

        # 3. Propagar Incerteza Tipo C e somar energias
        if '&' in linha and r'\pm' in linha:
            partes = linha.split('&')
            if len(partes) >= 5:
                coulomb_str = partes[-2]
                lj_str = partes[-1].split(r'\\')[0]
                
                match_c = re.search(r'(-?[\d\.]+)\s*(?:\\pm|\+)\s*([\d\.]+)', coulomb_str.replace('$', '').replace(' ', ''))
                match_lj = re.search(r'(-?[\d\.]+)\s*(?:\\pm|\+)\s*([\d\.]+)', lj_str.replace('$', '').replace(' ', ''))
                
                if match_c and match_lj:
                    vc, ec = float(match_c.group(1)), float(match_c.group(2))
                    vlj, elj = float(match_lj.group(1)), float(match_lj.group(2))
                    
                    # Cálculo Físico: Incerteza do Tipo C
                    v_tot = vc + vlj
                    e_tot = math.sqrt(ec**2 + elj**2)
                    
                    # Formatar a nova coluna (Limitado a 1 casa decimal para manter elegância)
                    nova_col = f" ${v_tot:.1f} \\pm {e_tot:.1f}$ "
                    
                    partes[-1] = lj_str + " &" + nova_col
                    linha = "&".join(partes) + r" \\" + "\n"
        
        novas_linhas.append(linha)

    with open(arquivo, 'w', encoding='utf-8') as f:
        f.writelines(novas_linhas)
    print("✅ Tabela do anexo atualizada! A coluna Energia Total com Incerteza do Tipo C (Regras UFG) foi inserida.")
else:
    print(f"❌ Ficheiro {arquivo} não encontrado.")
