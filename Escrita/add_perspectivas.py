import os

arquivo_alvo = "06_resultados.tex"

texto_perspectivas = r"""

% =====================================================================
% SECÇÃO 4.5 - PERSPECTIVAS FUTURAS E METODOLOGIA
% =====================================================================

\subsection{Perspectivas Futuras: Aprimoramento Paramétrico e Nucleação Assistida (\textit{Seeding})}

Conforme demonstrado nas análises termodinâmicas, o aprisionamento do DSPC em um estado metaestável de líquido super-resfriado não decorre de artefatos na parametrização primária. A análise de publicações recentes voltadas à calibração do lipidoma Martini 3 atesta que o emprego do barostato estocástico \textit{c-rescale} sob regime semi-isotrópico, aliado à desativação da tolerância do \textit{buffer} de Verlet (\texttt{verlet-buffer-tolerance = -1}) e extensão do raio da lista de vizinhos (\texttt{rlist = 1.35} nm), atende rigorosamente ao estado da arte para a prevenção de artefatos espaciais em simulações de membranas \cite{pedersen2024}. A inércia mecânica e a histerese térmica observadas nos protocolos de resfriamento contínuo (\textit{simulated annealing}) são reflexos de uma genuína barreira entálpica de dessolvatação intrínseca aos graus de liberdade do modelo \textit{coarse-grained}.

Para trabalhos futuros, a superação definitiva dessa barreira cinética e a determinação de Temperaturas de Transição Principal ($T_m$) rigorosamente exatas exigem a adoção da metodologia de nucleação assistida (\textit{seeding}). O fluxo de trabalho otimizado para a coexistência de fases deve incorporar as seguintes atualizações estruturais e paramétricas \cite{pedersen2024}:

\begin{enumerate}
    \item \textbf{Evolução na Construção Topológica (\textit{COBY}):} A montagem de caixas de simulação contendo múltiplas fases via \textit{scripts} tradicionais, como o \textit{insane}, apresenta limitações topológicas para domínios densos. Recomenda-se a adoção da recém-desenvolvida ferramenta \textit{Coarse-Grained System Builder} (COBY). O COBY viabiliza a inserção exata de um domínio (\textit{patch}) de lipídios previamente equilibrado na fase gel ($L_\beta$) no centro de uma matriz em fase fluida ($L_\alpha$), gerando uma interface cristal-líquido estável e isenta de sobreposições atômicas destrutivas.
    
    \item \textbf{Equilíbrio Interfacial com Banhos Múltiplos:} A estabilização inicial da semente gel não deve depender de restrições de posição estáticas, mas sim de acoplamento térmico independente. Configuram-se dois grupos de temperatura no GROMACS (\texttt{tc-grps}): a semente gel é mantida a $\approx 30$ K abaixo da sua transição teórica, enquanto a matriz fluida e o solvente circundantes são mantidos a $\approx 30$ K acima.
    
    \item \textbf{Adaptação Transiente de Barostatos:} Um detalhe algorítmico crítico inerente à arquitetura do GROMACS é a incompatibilidade do barostato de alta precisão \textit{c-rescale} com a aplicação de múltiplos banhos térmicos na mesma caixa de simulação. Consequentemente, durante a etapa isolada de relaxamento inicial do \textit{seeding}, o controle de pressão deve ser revertido temporariamente para o barostato de \textbf{Berendsen} ($\tau_p = 4,0$ ps). O \textit{c-rescale} deve ser restabelecido unicamente na amostragem final de produção.
    
    \item \textbf{Amostragem de Produção:} Com o sistema relaxado e unificado sob um único banho térmico alvo, executam-se trajetórias independentes em um gradiente estreito de temperaturas. A termodinâmica ditará o avanço ou recuo da interface geométrica. O patamar isotérmico no qual a Área por Lipídio permanecer contínua determinará a verdadeira $T_m$ do modelo livre de histerese.
\end{enumerate}

A incorporação destas perspectivas metodológicas e o refino no controle de integração computacional consolidam o embasamento necessário para transpor as previsões \textit{in silico} de modelos de membrana para o rigor exigido pela biofísica translacional e ensaios estruturais avançados.
"""

def inserir_perspectivas():
    with open(arquivo_alvo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    if "Aprimoramento Paramétrico e Nucleação Assistida" not in conteudo:
        with open(arquivo_alvo, "a", encoding="utf-8") as f:
            f.write("\n" + texto_perspectivas)
        print("✅ Nova Subseção de Perspectivas Futuras adicionada com sucesso ao final do arquivo 06_resultados.tex!")
    else:
        print("⚠️ A seção de perspectivas já existe no arquivo.")

if __name__ == "__main__":
    inserir_perspectivas()
