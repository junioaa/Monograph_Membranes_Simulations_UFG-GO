import os
import re

print("Iniciando varredura de resgate...")

# 1. FIX MAIN.TEX (Arruma as barras duplas e troca o pacote de formatação)
with open('main.tex', 'r', encoding='utf-8') as f:
    main = f.read()

# Conserta o erro fatal das barras duplas
main = main.replace(r'\\begin{document}', r'\begin{document}')
main = main.replace(r'\\pagenumbering', r'\pagenumbering')
main = main.replace(r'\\input{00_pre_textuais.tex}', r'\input{00_pre_textuais.tex}')
main = main.replace(r'\\tableofcontents', r'\tableofcontents')
main = main.replace(r'\\listoffigures', r'\listoffigures')
main = main.replace(r'\\listoftables', r'\listoftables')
main = main.replace(r'\\newpage', r'\newpage')
main = main.replace(r'\\section', r'\section')

# Remove o titlesec que conflitava com o hyperref do Sumário
main = re.sub(r'\\usepackage\{titlesec\}.*?\\titlespacing\*\{\\subsubsection\}\{0pt\}\{10pt\}\{6pt\}\n', '', main, flags=re.DOTALL)

# Injeta formatação segura (sectsty) que não quebra o documento
if 'sectsty' not in main:
    main = re.sub(r'(\\usepackage.*?)\n', r'\1\n\\usepackage{sectsty}\n\\sectionfont{\\fontsize{17}{20}\\selectfont\\bfseries}\n\\subsectionfont{\\fontsize{14}{17}\\selectfont\\bfseries}\n\\subsubsectionfont{\\fontsize{12}{15}\\selectfont\\itshape}\n', main, count=1)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main)

# 2. FIX RESUMO/ABSTRACT (Adequa as nomenclaturas para o formato Article)
if os.path.exists('01_resumo_abstract.tex'):
    with open('01_resumo_abstract.tex', 'r', encoding='utf-8') as f:
        resumo = f.read()
    resumo = resumo.replace(r'\begin{resumo}', r'\section*{RESUMO}')
    resumo = resumo.replace(r'\end{resumo}', '')
    resumo = resumo.replace(r'\begin{abstract}', r'\section*{ABSTRACT}')
    resumo = resumo.replace(r'\end{abstract}', '')
    resumo = resumo.replace(r'\vspace{\onelineskip}', r'\vspace{\baselineskip}')
    with open('01_resumo_abstract.tex', 'w', encoding='utf-8') as f:
        f.write(resumo)

# 3. FIX UNDERSCORES E LISTAS ABERTAS EM TODOS OS .TEX
for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Escapa underscores que causam "Missing $"
        content = content.replace('15W_L', r'15W\_L')
        content = content.replace('27W_L', r'27W\_L')
        content = content.replace('45W_L', r'45W\_L')
        content = content.replace('80W_L', r'80W\_L')
        content = content.replace('CHOL_', r'CHOL\_')
        
        # Retira underscores das chaves de citação para evitar quebras
        content = content.replace('olmsted_membranes', 'olmstedmembranes')
        content = content.replace('etsu_etd', 'etsuetd')
        content = content.replace('ufg_fisexp_2020', 'ufgfisexp2020')
        content = content.replace('martini3_jctc', 'martini3jctc')
        
        # Fecha listas (enumerate) que ficaram abertas e causaram "missing \item"
        if content.count(r'\begin{enumerate}') > content.count(r'\end{enumerate}'):
            content += '\n\\end{enumerate}\n'
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. FIX REFERENCIAS.BIB (Sincroniza as chaves)
if os.path.exists('referencias.bib'):
    with open('referencias.bib', 'r', encoding='utf-8') as f:
        bib = f.read()
    bib = bib.replace('olmsted_membranes', 'olmstedmembranes')
    bib = bib.replace('etsu_etd', 'etsuetd')
    bib = bib.replace('ufg_fisexp_2020', 'ufgfisexp2020')
    bib = bib.replace('martini3_jctc', 'martini3jctc')
    with open('referencias.bib', 'w', encoding='utf-8') as f:
        f.write(bib)

print("✅ Operação Resgate concluída! Erros sintáticos neutralizados.")
