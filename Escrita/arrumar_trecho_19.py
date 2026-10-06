import re

with open('04_revisao_bibliografica.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# Expressão regular para encontrar o texto antigo, ignorando quebras de linha
trecho_antigo = r'Um dos desafios clássicos na entrega de fármacos hidrofóbicos reside no aprisionamento.*?empregado na medicina tropical \[19\]\.'

# Texto novo focado na impessoalidade e na ciência
trecho_novo = r"Um dos desafios clássicos na entrega de fármacos hidrofóbicos reside no aprisionamento estável da molécula terapêutica sem catalisar a desintegração estérica da bicamada vetorial. Investigações computacionais e experimentais recentes escrutinaram o efeito do grau de saturação de esteróis no perfil reológico de lipossomas vetorizados com Ivermectina (IVM) --- um macrocíclico anti-helmíntico amplamente empregado na medicina tropical [19]."

# Aplica a substituição
texto = re.sub(trecho_antigo, lambda m: trecho_novo, texto, flags=re.DOTALL | re.IGNORECASE)

with open('04_revisao_bibliografica.tex', 'w', encoding='utf-8') as f:
    f.write(texto)

print("✅ Trecho da referência [19] reescrito para o formato impessoal com sucesso!")
