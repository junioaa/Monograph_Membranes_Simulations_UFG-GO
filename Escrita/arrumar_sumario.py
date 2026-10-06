import re

with open('main.tex', 'r', encoding='utf-8') as f:
    t = f.read()

# 1. Limpa qualquer menção antiga ou comentada da conclusão para evitar duplicatas
t = re.sub(r'%?\s*\\input\{07_conclusao(\.tex)?\}\n?', '', t)

# 2. Injeta a Conclusão ativada de volta, exatamente após os Resultados
t = re.sub(r'(\\input\{06_resultados(\.tex)?\})', r'\1\n\\input{07_conclusao}\n', t)

# 3. Força o LaTeX a colocar as REFERÊNCIAS no Sumário
if 'addcontentsline{toc}' not in t:
    t = re.sub(r'(\\bibliography\{referencias\})', r'\\clearpage\n\\addcontentsline{toc}{section}{REFERÊNCIAS}\n\1', t)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(t)
