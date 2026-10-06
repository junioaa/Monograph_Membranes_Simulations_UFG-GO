import re

with open('main.tex', 'r', encoding='utf-8') as f:
    main = f.read()

# 1. Limpa os comandos \newpage soltos que tínhamos colocado antes nas listas, 
# para evitar que a nova regra crie páginas em branco duplicadas.
main = re.sub(r'\\tableofcontents\s*\\newpage', r'\\tableofcontents\n', main)
main = re.sub(r'\\listoftables\s*\\newpage', r'\\listoftables\n', main)
main = re.sub(r'\\listoffigures\s*\\newpage', r'\\listoffigures\n', main)
main = re.sub(r'\\input\{01b_listas\.tex\}\s*\\newpage', r'\\input{01b_listas.tex}\n', main)

# 2. Injeta a Regra de Ouro no preâmbulo: toda seção pula página!
regra_quebra = r"""
% --- REGRA DA UFG: CADA CAPÍTULO E ITEM PRÉ-TEXTUAL EM PÁGINA SEPARADA ---
\let\oldsection\section
\renewcommand{\section}{\clearpage\oldsection}
"""

if r'\let\oldsection\section' not in main:
    main = main.replace(r'\begin{document}', regra_quebra + r'\begin{document}')

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main)

print("✅ Regra de quebra de página automática aplicada a todos os capítulos!")
