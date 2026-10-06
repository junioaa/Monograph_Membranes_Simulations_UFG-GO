import re

with open('06_resultados.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# 1. Renomeia a primeira subseção
texto = texto.replace(
    r'\subsection{Validação Estrutural e o Papel da Hidratação na Dinâmica de Fase}',
    r'\subsection{Dinâmica Estrutural: Efeitos da Hidratação, Cooperatividade e Espessura da Bicamada}'
)

# 2. Rebaixa a antiga subseção 4.2
texto = texto.replace(
    r'\subsection{Cooperatividade Termotrópica em Misturas Binárias}',
    r'\vspace{1em}' + '\n' + r'\noindent\textbf{Cooperatividade Termotrópica em Misturas Binárias:}'
)

# 3. Conserta o subtítulo duplicado do Colesterol
texto = texto.replace(
    r'\subsection{Modulação Eletrostática e o Efeito Condensador do Colesterol}',
    r'SUB_COLESTEROL_TEMP', 1
)
texto = texto.replace(
    r'\subsection{Modulação Eletrostática e o Efeito Condensador do Colesterol}',
    r''
)
texto = texto.replace(
    r'SUB_COLESTEROL_TEMP',
    r'\subsection{Modulação Eletrostática e o Efeito Condensador do Colesterol}'
)

# 4. Caça e move o bloco da "Espessura"
padrao_espessura = r'(Espessura da Bicamada e Efeito do Comprimento da Cadeia.*?\\end\{table\})'
match = re.search(padrao_espessura, texto, re.DOTALL)

if match:
    bloco_espessura = match.group(1)
    # Apaga do local original
    texto = texto.replace(bloco_espessura, '')
    
    # Formata como texto contínuo
    bloco_formatado = "\\vspace{1em}\n\\noindent\\textbf{" + bloco_espessura.replace('Espessura da Bicamada e Efeito do Comprimento da Cadeia', 'Espessura da Bicamada e Efeito do Comprimento da Cadeia:') + "}"
    
    # Insere no local exato usando string segura (imune a \cite)
    ponto_insercao = 'Embora a mescla de fosfolipídios atue como um facilitador cinético'
    texto = texto.replace(ponto_insercao, bloco_formatado + '\n\n' + ponto_insercao)

with open('06_resultados.tex', 'w', encoding='utf-8') as f:
    f.write(texto)

print("Estrutura reorganizada com sucesso e sem erros!")
