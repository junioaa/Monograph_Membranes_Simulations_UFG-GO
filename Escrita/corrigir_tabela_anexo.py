import re
import math

with open('anexos.tex', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open('anexos.tex', 'w', encoding='utf-8') as f:
    for l in linhas:
        # Adiciona a 6ª coluna no alinhamento do LaTeX
        if r'\begin{longtable}' in l or r'\begin{tabular}' in l:
            l = re.sub(r'\{([\|lrc]+)\}', lambda m: '{' + m.group(1).replace('}', '') + 'c|}' if not m.group(1).endswith('c|}') else m.group(0), l)
            
        # Arruma o cabeçalho com os parênteses corretos
        if 'Coulomb' in l and 'Lennard-Jones' in l:
            l = re.sub(r'Lennard-Jones.*$', r'Lennard-Jones (kJ/mol) & \\textbf{Total (kJ/mol)} \\\\', l)

        # Processa os dados numéricos sem corromper a string
        if r'\pm' in l and '\\\\' in l:
            partes = l.split('&')
            if len(partes) >= 5:
                coulomb_str = partes[3]
                lj_str = partes[4].replace('\\\\', '').replace('\n', '')
                
                # Extrai os valores numéricos exatos
                mc = re.search(r'(-?\d+\.?\d*)\s*(?:\\pm|\+|-)\s*(\d+\.?\d*)', coulomb_str)
                mlj = re.search(r'(-?\d+\.?\d*)\s*(?:\\pm|\+|-)\s*(\d+\.?\d*)', lj_str)
                
                if mc and mlj:
                    vc, ec = float(mc.group(1)), float(mc.group(2))
                    vlj, elj = float(mlj.group(1)), float(mlj.group(2))
                    
                    v_tot = vc + vlj
                    e_tot = math.sqrt(ec**2 + elj**2)
                    
                    # Formata a nova coluna preservando 1 casa decimal
                    nova_col = f" ${v_tot:.1f} \\pm {e_tot:.1f}$ "
                    
                    # Reconstrói a linha intacta
                    l = f"{partes[0]}&{partes[1]}&{partes[2]}&{partes[3]}& {lj_str} &{nova_col} \\\\\n"
        
        f.write(l)
print("✅ Tabela do anexo corrigida! A Incerteza do Tipo C foi propagada com sucesso.")
