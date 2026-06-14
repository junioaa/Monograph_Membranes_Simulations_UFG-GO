import re

arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

# Expressão regular para achar o título da subseção e o início do próximo parágrafo
texto_antigo_regex = r'(\\subsection\{O Papel Modulador do Colesterol e o Modelo de Cordas Flexíveis\})\s+(No estado fluido, as cadeias hidrocarbônicas)'

# A função isola o texto do LaTeX das regras da biblioteca 're'
def injetar_texto(match):
    return match.group(1) + r"""

\subsubsection*{O Efeito Condensador do Colesterol: Mecânica Estatística e Avaliação Paramétrica}

O colesterol é um modulador biomecânico essencial nas membranas celulares, presente em concentrações que variam de 20\% a 50\% na membrana plasmática animal. Sua estrutura molecular peculiar --- baseada em um núcleo tetracíclico planar altamente rígido, uma cauda iso-octil flexível e um pequeno grupamento hidroxila (-OH) de ancoragem interfacial --- instiga um fenômeno de ordem supramolecular conhecido como "efeito condensador" \cite{sawdon2025}.

""" + match.group(2)

# Substitui usando a função
texto_substituido = re.sub(texto_antigo_regex, injetar_texto, texto, flags=re.DOTALL)

with open(arquivo_tex, 'w', encoding='utf-8') as f:
    f.write(texto_substituido)

# Inserção da referência completa com DOI e a URL da Universidade de Southampton
arquivo_bib = 'referencias.bib'
nova_referencia = """
@article{sawdon2025,
  title={How well do empirical molecular mechanics force fields model the cholesterol condensing effect?},
  author={Sawdon, James and Piggot, Thomas J and Essex, Jonathan W},
  journal={The Journal of Chemical Physics},
  volume={162},
  number={4},
  pages={044901},
  year={2025},
  publisher={AIP Publishing},
  doi={10.1063/5.0238409},
  url={https://eprints.soton.ac.uk/499235/1/Chol_AIP_JCP_rev_2_clean.pdf}
}
"""

try:
    with open(arquivo_bib, 'r', encoding='utf-8') as f:
        bib_atual = f.read()
except FileNotFoundError:
    bib_atual = ""

if 'sawdon2025' not in bib_atual:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + nova_referencia)

print("✅ Parágrafo do Efeito Condensador inserido e referência adicionada com sucesso e sem erros!")
