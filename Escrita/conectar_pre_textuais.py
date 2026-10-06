import re

with open('main.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# Remove injeções antigas para evitar duplicação
texto = re.sub(r'\\input\{00_pre_textuais\.tex\}\n*', '', texto)
texto = re.sub(r'\\pagenumbering\{roman\}\n*', '', texto)
texto = re.sub(r'\\pagenumbering\{arabic\}\n*', '', texto)
texto = re.sub(r'\\tableofcontents\n*', '', texto)
texto = re.sub(r'\\listoffigures\n*', '', texto)
texto = re.sub(r'\\listoftables\n*', '', texto)
texto = re.sub(r'\\newpage\n*', '', texto)

# 1. Injeta os elementos pré-textuais logo no \begin{document}
bloco_inicial = r"""\\begin{document}

% Início dos pré-textuais (numeração romana exigida pela UFG)
\\pagenumbering{roman}
\\input{00_pre_textuais.tex}
"""
texto = texto.replace(r'\begin{document}', bloco_inicial)

# 2. Injeta as listas (Sumário, Figuras, Tabelas) logo antes da introdução, 
# e inicia a numeração arábica a partir da Introdução
bloco_listas = r"""
\\tableofcontents
\\newpage
\\listoffigures
\\newpage
\\listoftables
\\newpage

% Fim dos pré-textuais, início da numeração arábica exigida pela UFG
\\pagenumbering{arabic}
\\section{INTRODUÇÃO}
"""
texto = re.sub(r'\\section\{INTRODUÇÃO\}', bloco_listas, texto, count=1)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(texto)

print("✅ Capa, Folhas de Rosto, Listas Automáticas e Numeração Romana configuradas no padrão UFG!")
