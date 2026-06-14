import re

arquivo_tex = '04_revisao_bibliografica.tex'

texto_novo = r"""

\subsubsection*{Triagem e Reposicionamento Virucida (Vírus Oropouche e SARS-CoV-2)}

O potencial do escrutínio dinâmico também desponta na virologia molecular e no \textit{design} de inibidores esterostáticos contra agentes infecciosos emergentes. Pesquisas focadas na prospecção terapêutica contra o Vírus Oropouche (OROV) --- arbovírus negligenciado com alto impacto na saúde pública latino-americana --- revelam as fraquezas analíticas das predições estáticas clássicas.

Colherinhas e Cardoso (2025) executaram simulações de espectro atomístico pareadas para testar a inibição competitiva da glicoproteína celular Gc do envelope viral do OROV, utilizando acervos de retrovirais classicamente prescritos contra proteases do HIV \cite{colherinhas2025}. Abordagens teóricas conservadoras pautadas em ancoragem computacional rígida (\textit{Molecular Docking}) posicionaram erroneamente o fármaco Saquinavir no topo do escalonamento de afinidade. Todavia, quando o complexo ligante-proteína foi mergulhado e submetido aos fluxos solvatados ininterruptos da modelagem molecular de longa duração, as coordenadas energéticas sofreram metamorfose.

A DM comprovou que compostos homólogos concorrentes, notadamente o Nelfinavir e o Indinavir, abrigam resiliência estrutural incomparável. Durante as trajetórias microscópicas, estes compostos neutralizaram a flutuação do centro de massa e mantiveram ancoragens por pontes de hidrogênio constantes sob severa instabilidade colisional. Resultados complementares executados sobre o complexo da protease Mpro do coronavírus pandêmico (SARS-CoV-2) espelham idênticas hierarquias reativas. Este balanço termodinâmico denota que a seleção profilática rigorosa carece intrinsicamente dos vetores temporais viabilizados pelos campos de força aplicados na prospecção.
"""

# Adiciona o novo texto ao final do arquivo (anexando na seção de Biofísica Translacional)
with open(arquivo_tex, 'a', encoding='utf-8') as f:
    f.write(texto_novo)

# Formatação completa do artigo para o BibTeX
arquivo_bib = 'referencias.bib'
nova_referencia = """
@article{colherinhas2025,
  title={Insights into Antiviral Candidates against Oropouche Virus: A Molecular Dynamics Study},
  author={Colherinhas, Guilherme and Cardoso, Wesley B},
  journal={ACS Physical Chemistry Au},
  volume={5},
  pages={549--559},
  year={2025},
  publisher={American Chemical Society},
  url={https://pmc.ncbi.nlm.nih.gov/articles/PMC12464750/pdf/pg5c00042.pdf}
}
"""

try:
    with open(arquivo_bib, 'r', encoding='utf-8') as f:
        bib_atual = f.read()
except FileNotFoundError:
    bib_atual = ""

if 'colherinhas2025' not in bib_atual:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + nova_referencia)

print("✅ Seção de Virologia Molecular inserida e referência (Colherinhas e Cardoso) adicionada com sucesso!")
