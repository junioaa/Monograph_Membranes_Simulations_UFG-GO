import re

arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

texto_novo = r"""

\subsection{Biofísica Translacional: Vetores Farmacológicos, Lipossomas e Peptídeos Antimicrobianos}

O avanço na precisão termodinâmica dos campos de força culmina num impacto formidável no reposicionamento de moléculas bioativas e na formulação de nanoveículos farmacêuticos. A validação destas metodologias \textit{in silico} tem consolidado pilares estruturais para combater pandemias virais e endereçar patologias endêmicas. O fomento científico produzido pelas cátedras de vanguarda no Brasil ilustra a versatilidade desta frente, unificando cálculos termodinâmicos de Potencial da Força Média (PMF - \textit{Potential of Mean Force}) com metodologias instrumentais robustas, como a Ressonância Paramagnética Eletrônica (EPR) e o espalhamento dinâmico.

\subsubsection*{Lipossomas Baseados em Colesterol para a Captura Otimizada de Fármacos}

Um dos desafios clássicos na entrega de fármacos hidrofóbicos reside no aprisionamento estável da molécula terapêutica sem catalisar a desintegração estérica da bicamada vetorial. Em investigações publicadas no periódico \textit{ACS Applied Materials \& Interfaces} (2026), Barros \textit{et al.} escrutinaram computacionalmente e experimentalmente o efeito do grau de saturação de esteróis no perfil reológico de lipossomas vetorizados com Ivermectina (IVM) --- um macrocíclico anti-helmíntico amplamente empregado na medicina tropical \cite{barros2026}.
"""

# Adiciona o novo texto ao final do arquivo, mantendo o que já existe intacto
with open(arquivo_tex, 'w', encoding='utf-8') as f:
    f.write(texto.strip() + texto_novo)

# Formatação completa do artigo para o BibTeX com todos os autores, DOI e URL
arquivo_bib = 'referencias.bib'
nova_referencia = """
@article{barros2026,
  title={Cholesterol-Driven Optimization of Liposomal Systems for Ivermectin Capture: Insights from Experimental and Molecular Dynamics Studies},
  author={Barros, Alexandre C. M. and Pires, Jader and Mendanha, Karinna and de Sousa, Lucas R. and Fontanezi, Bianca B. and Colherinhas, Guilherme and Botelho, Ana F. M. and Mendanha, Sebasti{\\~a}o A. and Lima, Eliana M.},
  journal={ACS Applied Materials \\& Interfaces},
  volume={18},
  number={7},
  pages={10832--10841},
  year={2026},
  publisher={American Chemical Society},
  doi={10.1021/acsami.5c21365},
  url={https://pubs.acs.org/doi/10.1021/acsami.5c21365}
}
"""

try:
    with open(arquivo_bib, 'r', encoding='utf-8') as f:
        bib_atual = f.read()
except FileNotFoundError:
    bib_atual = ""

if 'barros2026' not in bib_atual:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + nova_referencia)

print("✅ Seção de Biofísica Translacional inserida no final e referência adicionada com sucesso e sem erros!")
