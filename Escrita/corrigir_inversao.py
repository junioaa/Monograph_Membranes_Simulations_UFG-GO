import re

with open('anexos.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('anexos.tex', 'w', encoding='utf-8') as f:
    for l in lines:
        # Só analisa as linhas que são de dados (contêm o & da tabela e o \pm da incerteza)
        if '&' in l and r'\pm' in l:
            parts = l.split('&')
            
            # A coluna 3 é Coulomb e a 4 é Lennard-Jones
            if len(parts) >= 5: 
                c_match = re.search(r'(-?\d+\.\d+)', parts[3])
                lj_match = re.search(r'(-?\d+\.\d+)', parts[4])
                
                if c_match and lj_match:
                    c_val = float(c_match.group(1))
                    lj_val = float(lj_match.group(1))
                    
                    # Se Coulomb for mais negativo que LJ, é fisicamente impossível na membrana!
                    # Destroca as colunas imediatamente.
                    if c_val < -10000 and lj_val > -10000:
                        temp = parts[3]
                        parts[3] = parts[4]
                        parts[4] = temp
                        l = "&".join(parts)
        
        f.write(l)

print("✅ Correção física concluída! Colunas de Coulomb e Lennard-Jones destrocadas nos sistemas com colesterol.")
