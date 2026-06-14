import os

arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

texto_novo = r"""\subsection{Termodinâmica e Cinética das Transições de Fase Lipídica}

A estabilidade estrutural das bicamadas lipídicas é regida pelo balanço termodinâmico contínuo entre as forças repulsivas de hidratação na interface polar e as forças de dispersão atrativas de van der Waals (energias de Lennard-Jones) atuantes no núcleo hidrofóbico. Fosfolipídios saturados homólogos, como a dipalmitoilfosfatidilcolina (DPPC) e a diestearoilfosfatidilcolina (DSPC), exibem transições de fase termotrópicas bem documentadas, onde a matriz lamelar transita de um estado sólido ou gel ($L_{\beta}$), com cadeias acílicas altamente empacotadas, para uma fase fluida desordenada ($L_{\alpha}$) quando a energia térmica do sistema supera a temperatura de transição principal ($T_m$) \cite{sun2018}.

\subsubsection*{Metaestabilidade e a Armadilha dos Líquidos Super-resfriados}

O estudo computacional do resfriamento termotrópico revela fenômenos cinéticos complexos, notoriamente a formação de estados metaestáveis que se manifestam como líquidos super-resfriados ou vidros em escala nanométrica \cite{olmsted_membranes}. Na mecânica estatística clássica, a transição da fase fluida para a fase gel requer a nucleação cooperativa de domínios ordenados. Em simulações de Dinâmica Molecular com resfriamento contínuo, as cadeias lipídicas desordenadas frequentemente perdem sua capacidade de cristalizar, quebrando a ergodicidade do sistema e caindo em um poço de potencial local.

Para o lipídio DSPC (18 átomos de carbono) simulado sob alta hidratação (45 moléculas de água por lipídio), observações com o campo de força CG revelam uma inércia profunda. Ao ser resfriado abaixo da sua $T_m$ experimental, o sistema falha em formar a fase gel espontaneamente, mantendo uma Área por Lipídio (APL) artificialmente dilatada de aproximadamente $61,5 \text{ \AA}^2$. A assinatura termodinâmica desse estado é revelada pela capacidade calorífica ($C_p$). O decréscimo perfeitamente linear da energia de dispersão global gera um $C_p \approx 1,14$ kJ/mol/K para o DSPC retido, ausente da quebra abrupta associada ao calor latente de cristalização, configurando a assinatura incontestável de um líquido super-resfriado.

\subsection{A Barreira Entálpica da Dessolvatação Interfacial}

A origem física desta metaestabilidade reside na forte penalidade energética associada à dessolvatação. Durante a fase fluida expandida, o volume livre interfacial permite que as moléculas de água ocupem os interstícios das cabeças polares (zwitteriônicas ou carregadas), estabelecendo interações de hidrogênio e eletrostáticas favoráveis \cite{etsu_etd, tandfonline2026}. Para que a cristalização cooperativa e a condensação lateral ocorram (atingindo uma APL típica de gel $\approx 45 \text{ \AA}^2$), a membrana deve expulsar mecanicamente esta água da camada de solvatação primária, um evento denominado como barreira de repulsão por hidratação. 

Cálculos extraídos de modelos sob hidratação restrita validam esta premissa. Quando o grau de hidratação do sistema é reduzido artificialmente, a blindagem dielétrica diminui e a barreira de dessolvatação é suprimida, induzindo a cristalização espontânea e cooperativa em toda a matriz. A inércia observada para o DSPC em simulações contrasta com o DPPC (16 carbonos), que devido ao menor atrito estérico interno de suas caudas mais curtas, consegue utilizar a energia térmica flutuante ($k_B T$) para formar o núcleo crítico de gelificação de maneira muito mais célere. Este fenômeno evidencia a sensibilidade aguda da cinética de fase à dependência estrutural do comprimento da cadeia acílica e ao volume de solvente confinado.

\subsection{O Papel Modulador do Colesterol e o Modelo de Cordas Flexíveis}

No estado fluido, as cadeias hidrocarbônicas apresentam elevado grau de liberdade conformacional, com frequentes isomerizações do tipo \textit{trans-gauche}. Do ponto de vista da mecânica estatística, esse comportamento pode ser descrito pelo modelo de cordas flexíveis (\textit{Flexible Strings Model}), onde as caudas lipídicas oscilam lateralmente impulsionadas pela energia térmica, gerando um volume livre que resulta em maiores valores de Área por Lipídio (APL) \cite{kheyfets2015}.

A introdução do colesterol altera fundamentalmente esse balanço. Devido à sua estrutura de anéis tetracíclicos fundidos, o colesterol atua como uma haste rígida (rigid rod) quando intercalado na bicamada \cite{kheyfets2015}. A presença do esterol suprime os graus de liberdade vibracionais das cadeias alquílicas adjacentes, impondo um ordenamento estérico que estira as caudas fosfolipídicas para a conformação \textit{all-trans} \cite{bennett2018}. Este fenômeno, conhecido como efeito condensador, resulta na diminuição da APL e no aumento da espessura da membrana, induzindo a formação da fase líquida-ordenada ($L_o$) \cite{leeb2018}. Termodinamicamente, o rearranjo promovido pelo colesterol compensa a perda de entropia conformacional através da otimização dos contatos atrativos no núcleo apolar \cite{bennett2018}.
"""

# Identifica exatamente onde o bloco entra (sem usar regex, para não ter chance de errar)
inicio = texto.find(r'\subsection{Termodinâmica e Cinética das Transições de Fase Lipídica}')
fim = texto.find(r'\subsection{Interações Interfaciais: Hidratação e Efeitos Iônicos}')

if inicio != -1 and fim != -1:
    texto_final = texto[:inicio] + texto_novo + "\n\n" + texto[fim:]
    with open(arquivo_tex, 'w', encoding='utf-8') as f:
        f.write(texto_final)
    print("✅ Restauração concluída: Textos novos inseridos e o colesterol recuperado intacto!")
else:
    print("❌ Erro: Não foi possível localizar as subseções de âncora no arquivo.")
