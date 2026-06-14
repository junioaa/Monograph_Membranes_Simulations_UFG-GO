import re

arquivo_tex = '04_revisao_bibliografica.tex'
with open(arquivo_tex, 'r', encoding='utf-8') as f:
    texto = f.read()

# Procura a seção antiga do Martini 3 até o começo da seção de Biofísica Translacional
texto_antigo_regex = r'\\subsection\{Dinâmica Molecular e o Modelo Coarse-Grained Martini 3\}.*?(?=\\subsection\{Biofísica Translacional)'

# Função para injetar o texto de forma isolada, evitando problemas com barras invertidas
def injetar_texto(match):
    return r"""\subsection{Dinâmica Molecular e os Avanços do Campo de Força Martini 3}

O campo de força Martini representa o arcabouço computacional mais empregado globalmente para a modelagem \textit{Coarse-Grained} de biomembranas. A liberação da iteração Martini 3, seguida pelas extensas reparametrizações conduzidas por Pedersen \textit{et al.} \cite{pedersen2025}, propiciou um nível de precisão sem precedentes no \textit{Lipidome}, expandindo a biblioteca para milhares de modelos lipídicos e solucionando inconsistências mecânicas severas herdadas das versões anteriores.

\subsubsection*{Resolução do Conflito de Mapeamento 4:1 e Topologia}

O desafio histórico do modelo CG era o mapeamento padrão de 4 átomos pesados para 1 \textit{bead}. Sob essa diretriz rígida no Martini 2, as cadeias acílicas de 16 átomos de carbono (como o DPPC) e as de 18 átomos (como o DSPC) frequentemente exibiam ambiguidade paramétrica. Experimentalmente, medições de espalhamento de raios-X e nêutrons atestam que a espessura da distância pico-a-pico da densidade eletrônica ($D_{HH}$) é de $3,46 \pm 0,07$ nm para o DPPC e $4,33 \pm 0,09$ nm para o DSPC a 333 K. O mapeamento antigo possuía dificuldades em reproduzir fielmente esse gradiente geométrico, influenciando o perfil termodinâmico global \cite{martini3_jctc}.

O Martini 3 superou este obstáculo implementando uma estratégia de mapeamento de raios variáveis, diferenciando com precisão lipídios que diferem por apenas dois átomos de carbono. Para as cadeias de 16 carbonos, o modelo emprega esferas de interação de tamanho reduzido (\textit{small beads}, notadamente tipos SC1 e SC2) nas posições adjacentes aos grupos éster e glicerol. Esta redução no raio colisional das partículas diminui o volume de exclusão e o atrito estérico, ao passo que as cadeias estendidas de 18 carbonos são parametrizadas integralmente com \textit{beads} regulares. A correção paramétrica garante o alinhamento rigoroso da espessura transversal simulada com as dispersões de nêutrons. Além disso, o tratamento de ácidos graxos poliinsaturados sofreu refinamento: \textit{beads} que representam 1,5 ligações duplas foram alterados de C4h para o nível de interação superior C5h, calibrando a densidade interfacial em misturas vitais \cite{pedersen2025}.

\subsubsection*{Restauração do Comportamento de Fase em Misturas Ternárias}

A principal motivação subjacente à reparametrização do Martini 3 foi a recuperação das propriedades de separação de fases. O modelo Martini 2 apresentava severas deficiências em induzir a coexistência de fases lamelar fluida ($L_d$) e líquida-ordenada ($L_o$) em diagramas de fase ternários (ex. DPPC/DOPC/Colesterol) a temperaturas biologicamente relevantes, frequentemente resultando em misturas homogeneamente desordenadas.

Para restaurar esta fidelidade, os desenvolvedores realizaram um compromisso consciente durante a otimização paramétrica global (\textit{top-down calibration}). Aceitou-se uma pequena, porém sistemática, subestimação da Área por Lipídio ($\approx 3 \text{ \AA}^2$) na fase fluida para componentes como fosfatidilcolinas (PC), fosfatidilgliceróis (PG) e esfingomielinas (SM). O aumento discreto na compactação interfacial estabiliza as interações intermoleculares e permite que o modelo capture de maneira impecável a formação de microdomínios (\textit{lipid rafts}) dinâmicos \cite{pedersen2025}. Em matrizes DPPC/Colesterol, o Martini 3 é capaz de predizer substruturas ordenadas e a dinâmica local da fase $L_o$, um marco inatingível com a precisão dos modelos precedentes.

\subsubsection*{Histerese e a Precisão das Temperaturas de Transição ($T_m$)}

A calibração das temperaturas de transição (\textit{melting temperatures}, $T_m$) é a métrica definitiva para atestar o sucesso de um campo de força em membranas. Contudo, as barreiras cinéticas introduzem complicações na amostragem. Em simulações de aquecimento ou resfriamento contínuo (\textit{simulated annealing}), o índice de Lindemann e a APL demonstram forte histerese térmica, superestimando a $T_m$ em até 10 K devido à energia de ativação necessária para romper ou formar a rede de empacotamento apolar de maneira espontânea \cite{martini3_jctc}.

Para isolar o artefato cinético do valor termodinâmico autêntico do modelo, protocolos ortogonais de nucleação assistida (\textit{seeding}) são empregados. O método de \textit{seeding} envolve a inserção de uma ``semente'' lamelar já no estado gel no interior de uma membrana fluida, criando uma interface pré-existente e contornando a penalidade da nucleação inicial. A Tabela 1 detalha os desvios entre as métricas, evidenciando como o modelo Martini 3 aproxima-se dos referenciais da calorimetria de varredura diferencial (DSC) com precisão extraordinária sob o protocolo correto \cite{pedersen2025}.

"""

# Aplica a substituição
texto_substituido = re.sub(texto_antigo_regex, injetar_texto, texto, flags=re.DOTALL)

with open(arquivo_tex, 'w', encoding='utf-8') as f:
    f.write(texto_substituido)

# Inserção das novas referências no arquivo bibtex
arquivo_bib = 'referencias.bib'
novas_referencias = """
@article{martini3_jctc,
  title={Martini 3 Coarse-Grained Force Field: Small Molecules},
  author={Souza, Paulo C. T. and others},
  journal={Journal of Chemical Theory and Computation},
  year={2023},
  doi={10.1021/acs.jctc.3c00547},
  url={https://pubs.acs.org/doi/10.1021/acs.jctc.3c00547}
}

@article{pedersen2025,
  title={The Martini 3 Lipidome: Expanded and Refined Parameters Improve Lipid Phase Behavior},
  author={Pedersen, Kasper B. and others},
  journal={ACS Central Science},
  year={2025},
  doi={10.1021/acscentsci.5c00755},
  url={https://pubs.acs.org/doi/10.1021/acscentsci.5c00755}
}
"""

try:
    with open(arquivo_bib, 'r', encoding='utf-8') as f:
        bib_atual = f.read()
except FileNotFoundError:
    bib_atual = ""

# Só injeta se a chave não existir
if 'pedersen2025' not in bib_atual:
    with open(arquivo_bib, 'a', encoding='utf-8') as f:
        f.write("\n" + novas_referencias)

print("✅ Seção do Martini 3 e o Lipidome substituída com sucesso e referências adicionadas!")
