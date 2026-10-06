import re, math

with open('anexos.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('anexos.tex', 'w', encoding='utf-8') as f:
    for l in lines:
        # 1. Ajusta o número de colunas do LaTeX
        if r'\begin{longtable}' in l or r'\begin{tabular}' in l:
            l = re.sub(r'\{([\|lrc]+)\}', lambda m: '{' + m.group(1).replace('}', '') + 'c|}' if not m.group(1).endswith('c|}') else m.group(0), l)
        
        # 2. SUBSTITUI O CABEÇALHO (Com trava de segurança para não corromper o texto)
        elif 'Coulomb' in l and 'Lennard-Jones' in l and '&' in l and (r'\\' in l or r'\tabularnewline' in l):
            fim = re.search(r'(\\\\|\tabularnewline).*', l)
            sufixo = fim.group(0) if fim else r'\\'
            l = r'\textbf{Sistema} & \textbf{Prop.} & \textbf{Temp.} & \textbf{C (kJ/mol)} & \textbf{LJ (kJ/mol)} & \textbf{Total (kJ/mol)} ' + sufixo + '\n'
        
        # 3. Faz a matemática para os dados e cria a última coluna
        elif ('15W' in l or '27W' in l or '45W' in l or 'CHOL' in l) and '&' in l and r'\pm' in l:
            floats = re.findall(r'-?\d+\.\d+', l)
            if len(floats) >= 4:
                vc, ec = float(floats[-4]), float(floats[-3])
                vlj, elj = float(floats[-2]), float(floats[-1])
                
                vt = vc + vlj
                et = math.sqrt(ec**2 + elj**2)
                
                l = re.sub(r'&?\s*(\\\\|\tabularnewline)', lambda m: f' & ${vt:.1f} \\pm {et:.1f}$ ' + m.group(1), l)
        
        f.write(l)
print("✅ Tabela gerada de forma blindada! Cabeçalhos abreviados e Incerteza do Tipo C aplicada.")
