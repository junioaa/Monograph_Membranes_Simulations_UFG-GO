import re

with open('main.tex', 'r') as f:
    t = f.read()

# 1. Separa as listas em páginas diferentes e resgata a Lista de Abreviaturas
bloco_antigo = r'\\listoffigures\s*\\listoftables\s*\\tableofcontents'
bloco_novo = r'\\newpage\n\\input{01b_listas}\n\\newpage\n\\listoffigures\n\\newpage\n\\listoftables\n\\newpage\n\\tableofcontents'
t = re.sub(bloco_antigo, bloco_novo, t)

# 2. Garante que os capítulos textuais sempre quebrem a página (Regra UFG) usando o pacote titlesec
if r'\sectionbreak' not in t:
    t = t.replace(r'\usepackage{titlesec}', "\\usepackage{titlesec}\n\\newcommand{\\sectionbreak}{\\clearpage}")

with open('main.tex', 'w') as f:
    f.write(t)
