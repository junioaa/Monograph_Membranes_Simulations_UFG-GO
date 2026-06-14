import re

# 1. Arruma o texto da revisão bibliográfica
arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

# Substitui o trecho problemático usando \\cite (escapado) para o Python não reclamar do \c
texto = re.sub(r'indispensável na biofísica moderna.*?Através da', 
               r'indispensável na biofísica moderna \\cite{crippa2023}. Através da', texto, flags=re.DOTALL)

with open(arquivo_tex, 'w', encoding='utf-8') as f:
    f.write(texto)

# 2. Arruma o arquivo de referências
arquivo_bib = 'referencias.bib'
try:
    with open(arquivo_bib, 'r', encoding='utf-8') as f:
        bib = f.read()
except FileNotFoundError:
    bib = ""

entrada_crippa = """
@article{crippa2023,
  title={Detecting dynamic domains and local fluctuations in complex molecular systems via timelapse neighbors shuffling},
  author={Crippa, Martina and Cardellini, Annalisa and Caruso, Cristina and Pavan, Giovanni M},
  journal={Proceedings of the National Academy of Sciences},
  volume={120},
  number={30},
  pages={e2300565120},
  year={2023},
  publisher={National Acad Sciences},
  doi={10.1073/pnas.2300565120},
  url={https://www.pnas.org/doi/epdf/10.1073/pnas.2300565120}
}
"""

if 'crippa2023' not in bib:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + entrada_crippa)
else:
    # Se a entrada já existir, garante que a URL com o /epdf/ está atualizada
    bib = re.sub(r'url\s*=\s*\{.*?pnas\.2300565120\}', r'url={https://www.pnas.org/doi/epdf/10.1073/pnas.2300565120}', bib)
    with open(arquivo_bib, 'w', encoding='utf-8') as f:
        f.write(bib)

print("✅ Citação e bibliografia corrigidas sem erros de sintaxe!")
