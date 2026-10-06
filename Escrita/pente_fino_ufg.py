import re

print("Iniciando o Pente Fino da UFG...")

# 1. ARRUMAR AS LISTAS NO MAIN.TEX (Blindado contra escape de string)
with open('main.tex', 'r', encoding='utf-8') as f:
    main = f.read()

# Margens 2.5cm
if 'geometry' not in main:
    main = re.sub(r'(\\usepackage.*?)\n', lambda m: m.group(1) + r'\n\usepackage[left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm]{geometry}\n', main, count=1)
else:
    main = re.sub(r'\\usepackage\[.*?\]\{geometry\}', r'\\usepackage[left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm]{geometry}', main)

# Fonte do Nível 3 (13pt negrito)
main = main.replace(r'\subsubsectionfont{\fontsize{12}{15}\selectfont\itshape}', r'\subsubsectionfont{\fontsize{13}{16}\selectfont\bfseries}')

# Ordem correta das listas (Função Lambda para blindar as barras)
def injetar_listas(match):
    return r"""\tableofcontents
\newpage
\listoftables
\newpage
\listoffigures
\newpage
\input{01b_listas.tex}
\newpage

% Fim dos pré-textuais, início da numeração arábica exigida pela UFG
\pagenumbering{arabic}
"""
main = re.sub(r'\\tableofcontents.*?\\pagenumbering\{arabic\}', injetar_listas, main, flags=re.DOTALL)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main)

# 2. RECORTAR A LISTA DE ABREVIATURAS E AJUSTAR A FOLHA DE ROSTO E DEDICATÓRIA
with open('00_pre_textuais.tex', 'r', encoding='utf-8') as f:
    pre = f.read()

# Extrai a lista de abreviaturas para o arquivo isolado
match_listas = re.search(r'(% --- LISTA DE ABREVIATURAS E SÍMBOLOS ---.*)', pre, flags=re.DOTALL)
if match_listas:
    listas_text = match_listas.group(1)
    pre = pre.replace(listas_text, '')
    with open('01b_listas.tex', 'w', encoding='utf-8') as f:
        f.write(listas_text)

# Folha de Rosto (Recuo 7cm e entrelinha 1.15)
folha_rosto_antiga = r"""\begin{flushright}
\begin{minipage}{8cm}
\fontsize{12}{14.4}\selectfont
Monografia apresentada na disciplina de Trabalho de Conclusão de Curso da graduação em Física Médica do Instituto de Física da Universidade Federal de Goiás.

\vspace{\baselineskip}
Orientador: Prof. Dr. Wesley Bueno Cardoso
\end{minipage}
\end{flushright}"""

folha_rosto_nova = r"""\vspace*{2cm}
\noindent\hspace*{7cm}
\begin{minipage}{\dimexpr\textwidth-7cm\relax}
\fontsize{12}{13.8}\selectfont
Monografia apresentada na disciplina de Trabalho de Conclusão de Curso da graduação em Física Médica do Instituto de Física da Universidade Federal de Goiás.

\vspace{\baselineskip}
Orientador: Prof. Dr. Wesley Bueno Cardoso
\end{minipage}"""

pre = pre.replace(folha_rosto_antiga, folha_rosto_nova)

# Dedicatória (Terço inferior, TNR 11, Itálico)
dedicatoria_antiga = r"""\vspace*{20cm}
\begin{flushright}
\textit{Dedico este trabalho à minha família, \\
pelo apoio incondicional em toda a minha jornada, \\
e a todos que impulsionam o avanço da física médica.}
\end{flushright}"""

dedicatoria_nova = r"""\vspace*{\fill}
\begin{flushright}
\fontsize{11}{13.2}\selectfont\itshape
Dedico este trabalho à minha família, \\
pelo apoio incondicional em toda a minha jornada, \\
e a todos que impulsionam o avanço da física médica.
\end{flushright}
\vspace*{2cm}"""

pre = pre.replace(dedicatoria_antiga, dedicatoria_nova)

with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(pre)

print("✅ Formatação da UFG aplicada com sucesso e sem erros do Python!")
