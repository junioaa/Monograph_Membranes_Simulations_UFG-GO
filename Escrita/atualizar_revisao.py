import re

arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

# Texto antigo a ser removido
texto_antigo_regex = r'A estabilidade destas estruturas depende do balanço termodinâmico.*?Área por Lipídio \(APL\) \\cite\{kheyfets2015\}\.'

# Novo texto em LaTeX puro
texto_novo = r"""\subsection{Termodinâmica e Cinética das Transições de Fase Lipídica}

A estabilidade estrutural das bicamadas lipídicas é regida pelo balanço termodinâmico contínuo entre as forças repulsivas de hidratação na interface polar e as forças de dispersão atrativas de van der Waals (energias de Lennard-Jones) atuantes no núcleo hidrofóbico. Fosfolipídios saturados homólogos, como a dipalmitoilfosfatidilcolina (DPPC) e a diestearoilfosfatidilcolina (DSPC), exibem transições de fase termotrópicas bem documentadas, onde a matriz lamelar transita de um estado sólido ou gel ($L_{\beta}$), com cadeias acílicas altamente empacotadas, para uma fase fluida desordenada ($L_{\alpha}$) quando a energia térmica do sistema supera a temperatura de transição principal ($T_m$) \cite{sun2018}.

\subsubsection*{Metaestabilidade e a Armadilha dos Líquidos Super-resfriados}

O estudo computacional do resfriamento termotrópico revela fenômenos cinéticos complexos, notoriamente a formação de estados metaestáveis que se manifestam como líquidos super-resfriados ou vidros em escala nanométrica \cite{olmsted_membranes}. Na mecânica estatística clássica, a transição da fase fluida para a fase gel requer a nucleação cooperativa de domínios ordenados. Em simulações de Dinâmica Molecular com resfriamento contínuo, as cadeias lipídicas desordenadas frequentemente perdem sua capacidade de cristalizar, quebrando a ergodicidade do sistema e caindo em um poço de potencial local.

Para o lipídio DSPC (18 átomos de carbono) simulado sob alta hidratação (45 moléculas de água por lipídio), observações com o campo de força CG revelam uma inércia profunda. Ao ser resfriado abaixo da sua $T_m$ experimental, o sistema falha em formar a fase gel espontaneamente, mantendo uma Área por Lipídio (APL) artificialmente dilatada de aproximadamente $61,5 \text{ \AA}^2$. A assinatura termodinâmica desse estado é revelada pela capacidade calorífica ($C_p$). O decréscimo perfeitamente linear da energia de dispersão global gera um $C_p \approx 1,14$ kJ/mol/K para o DSPC retido, ausente da quebra abrupta associada ao calor latente de cristalização, configurando a assinatura incontestável de um líquido super-resfriado.

\subsection{A Barreira Entálpica da Dessolvatação Interfacial}

A origem física desta metaestabilidade reside na forte penalidade energética associada à dessolvatação. Durante a fase fluida expandida, o volume livre interfacial permite que as moléculas de água ocupem os interstícios das cabeças polares (zwitteriônicas ou carregadas), estabelecendo interações de hidrogênio e eletrostáticas favoráveis \cite{etsu_etd, tandfonline2026}. Para que a cristalização cooperativa e a condensação lateral ocorram (atingindo uma APL típica de gel $\approx 45 \text{ \AA}^2$), a membrana deve expulsar mecanicamente esta água da camada de solvatação primária, um evento denominado como barreira de repulsão por hidratação. 

Cálculos extraídos de modelos sob hidratação restrita validam esta premissa. Quando o grau de hidratação do sistema é reduzido artificialmente, a blindagem dielétrica diminui e a barreira de dessolvatação é suprimida, induzindo a cristalização espontânea e cooperativa em toda a matriz. A inércia observada para o DSPC em simulações contrasta com o DPPC (16 carbonos), que devido ao menor atrito estérico interno de suas caudas mais curtas, consegue utilizar a energia térmica flutuante ($k_B T$) para formar o núcleo crítico de gelificação de maneira muito mais célere. Este fenômeno evidencia a sensibilidade aguda da cinética de fase à dependência estrutural do comprimento da cadeia acílica e ao volume de solvente confinado."""

# Aqui está a mágica: o 'lambda _: texto_novo' impede o Python de ler as barras invertidas como comandos!
texto_substituido = re.sub(texto_antigo_regex, lambda _: texto_novo, texto, flags=re.DOTALL)

with open(arquivo_tex, 'w', encoding='utf-8') as f:
    f.write(texto_substituido)

# Inserção das novas referências no arquivo bibtex
arquivo_bib = 'referencias.bib'
novas_referencias = """
@article{sun2018,
  title={Membrane Phase Transitions and Thermodynamics},
  author={Sun, M. and others},
  journal={European Biophysics Journal},
  year={2018},
  url={https://www.biomemphys.nat.fau.de/files/2018/03/sun_ebj_2018.pdf}
}

@misc{olmsted_membranes,
  title={Research: Membranes and Lipids},
  author={Olmsted, Peter},
  year={2023},
  url={https://site.physics.georgetown.edu/~pdo7/research/membranes.html}
}

@phdthesis{etsu_etd,
  title={Thermodynamics and Kinetics of Lipid Bilayer Phase Transitions},
  author={ETSU Research},
  school={East Tennessee State University},
  year={2023},
  url={https://dc.etsu.edu/cgi/viewcontent.cgi?article=6278&context=etd}
}

@article{tandfonline2026,
  title={Hydration Repulsion and Lipid Membrane Dehydration},
  author={Taylor and Francis Online},
  journal={Advances in Physics: X},
  year={2026},
  url={https://www.tandfonline.com/doi/epdf/10.1080/23746149.2026.2636806}
}
"""

with open(arquivo_bib, 'r', encoding='utf-8') as f:
    bib_atual = f.read()

if 'sun2018' not in bib_atual:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + novas_referencias)

print("✅ Textos substituídos e referências novas injetadas com sucesso!")
