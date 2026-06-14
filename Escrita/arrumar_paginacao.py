import re

# 1. ARRUMAR A POSIÇÃO DA PÁGINA NO MAIN.TEX (Canto inferior direito)
with open('main.tex', 'r', encoding='utf-8') as f:
    main = f.read()

config_paginacao = r"""
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{} % Limpa cabeçalhos e rodapés padrão
\renewcommand{\headrulewidth}{0pt} % Remove a linha do cabeçalho
\fancyfoot[R]{\thepage} % Número da página no canto inferior direito

% Força as páginas de capítulos e sumários a obedecerem à regra da direita
\fancypagestyle{plain}{
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[R]{\thepage}
}
"""

if 'fancyhdr' not in main:
    # A função lambda impede o Python de interpretar o \u do \usepackage
    main = re.sub(r'(\\usepackage.*?)\n', lambda m: m.group(1) + '\n' + config_paginacao, main, count=1)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main)

# 2. ARRUMAR A CONTAGEM DA CAPA
with open('00_pre_textuais.tex', 'r', encoding='utf-8') as f:
    pre = f.read()

# Substitui o titlepage que resetava a contagem por um comando que só esconde o número
pre = pre.replace(r'\begin{titlepage}', r'\thispagestyle{empty}')
pre = pre.replace(r'\end{titlepage}', '')

with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(pre)

print("✅ Paginação corrigida e blindada contra erros de Unicode!")
