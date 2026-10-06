import os
import re

def arrumar_tudo():
    # 1. Limpar referencias.bib (Exterminar a duplicata ramirez2025)
    bib_file = "referencias.bib"
    if os.path.exists(bib_file):
        with open(bib_file, "r", encoding="utf-8") as f:
            conteudo_bib = f.read()
        
        # Expressão regular para remover a segunda aparição de ramirez2025
        padrao_duplicata = re.compile(r"(@\w+\{ramirez2025.*?)(@\w+\{ramirez2025.*?\n\})", re.DOTALL)
        if padrao_duplicata.search(conteudo_bib):
            conteudo_bib = re.sub(r"(@\w+\{ramirez2025.*?)\n@\w+\{ramirez2025.*?\n\}", r"\1", conteudo_bib, flags=re.DOTALL)
            with open(bib_file, "w", encoding="utf-8") as f:
                f.write(conteudo_bib)
            print("✅ Duplicata 'ramirez2025' eliminada do referencias.bib!")
    
    # 2. Arrumar 06_resultados.tex (Citação falsa e Perspectivas)
    res_file = "06_resultados.tex"
    if os.path.exists(res_file):
        with open(res_file, "r", encoding="utf-8") as f:
            res_content = f.read()
        
        # Corrigir a citação "main.pdf" quebrada
        res_content = res_content.replace(r"\cite{main.pdf}", r"\cite{pedersen2024}")
        
        perspectivas = r"""
% =====================================================================
% SECÇÃO 4.5 - PERSPECTIVAS FUTURAS E SEEDING
% =====================================================================

\subsection{Perspectivas Futuras: Aprimoramentos Paramétricos e Nucleação Assistida (\textit{Seeding})}

Conforme demonstrado nas análises termodinâmicas, o aprisionamento do DSPC em um estado metaestável não decorre de artefatos de simulação, mas de uma autêntica barreira entálpica de dessolvatação intrínseca ao modelo \textit{coarse-grained}. A inércia estrutural observada nos protocolos de resfriamento contínuo (\textit{simulated annealing}) corrobora estudos recentes do lipidoma Martini 3, que atestam uma histerese significativa neste tipo de amostragem térmica \cite{pedersen2024}. 

Para investigações futuras que demandem a determinação exata e livre de histerese da temperatura de transição ($T_m$), sugere-se a aplicação metodológica da nucleação assistida (\textit{seeding}). Com base nas configurações validadas por Pedersen \textit{et al.} \cite{pedersen2024}, o refinamento topológico e termodinâmico no GROMACS deve seguir as seguintes diretrizes:

\begin{enumerate}
    \item \textbf{Substituição do \textit{Insane} pelo \textit{COBY}:} A montagem de membranas heterogêneas contendo ilhas sólidas (fase gel) inseridas em matrizes líquidas encontra severas limitações no clássico \textit{script insane}. Recomenda-se a ferramenta \textit{Coarse-Grained System Builder} (COBY), projetada especificamente para viabilizar a inserção de um \textit{patch} lamelar estruturado ($L_\beta$) no núcleo da membrana fluida ($L_\alpha$) sem provocar sobreposições destrutivas.
    \item \textbf{O Paradoxo dos Barostatos no Equilíbrio:} A estabilização da semente geométrica exige dois banhos térmicos independentes na mesma topologia (e.g., semente gel 30 K abaixo da $T_m$ teórica e matriz 30 K acima). Contudo, devido a uma limitação arquitetural do GROMACS, o barostato estocástico \textit{c-rescale} não suporta múltiplos grupos de acoplamento térmico (\texttt{tc-grps}). Portanto, é obrigatório o uso temporário do barostato de \textbf{Berendsen} ($\tau_p = 4,0$ ps) unicamente durante o relaxamento da interface de coexistência \cite{pedersen2024}.
    \item \textbf{Amorstragem de Produção:} Com a interface estabilizada, o controle de temperatura é unificado e o sistema deve obrigatoriamente retornar ao barostato \textit{c-rescale} semi-isotrópico para a execução das trajetórias de varredura térmica que ditarão a $T_m$ exata.
\end{enumerate}

A adoção destas configurações assegura o mais estrito alinhamento ao estado da arte do campo de força Martini 3, garantindo alta exatidão física e reprodutibilidade exigidas na modelagem avançada de membranas lipídicas.
"""
        # Atualizando a seção de Perspectivas
        if "\\subsection{Perspectivas Futuras:" in res_content:
            res_content = re.sub(r"\\subsection\{Perspectivas Futuras:.*", perspectivas.strip(), res_content, flags=re.DOTALL)
        else:
            res_content += "\n\n" + perspectivas.strip() + "\n"
            
        with open(res_file, "w", encoding="utf-8") as f:
            f.write(res_content)
        print("✅ Citações fantasmas corrigidas e Perspectivas alinhadas com o artigo inseridas!")

    # 3. Atualizar a Metodologia (05_metodologia.tex) justificando a pressão
    met_file = "05_metodologia.tex"
    if os.path.exists(met_file):
        with open(met_file, "r", encoding="utf-8") as f:
            met_content = f.read()
        
        texto_metodologia = r"""Os parâmetros de integração algorítmica e o controle termodinâmico adotados neste trabalho fundamentam-se nas diretrizes do estado da arte validadas por Pedersen \textit{et al.} para a estabilidade do lipidoma Martini 3 \cite{pedersen2024}. O controle de pressão \textbf{semi-isotrópico} foi empregado visando a dilatação e contração autônoma do plano lateral da membrana (eixos X e Y) desvinculada do eixo transversal (Z), condição mecânica exigida para bicamadas lipídicas. 

A pressão foi mantida a 1 bar pelo barostato estocástico \textit{cell-rescaling} (\textit{c-rescale}), utilizando constante de tempo $\tau_p = 4,0$ ps e compressibilidade de $3\times10^{-4}\text{ bar}^{-1}$. A escolha do \textit{c-rescale} em detrimento do algoritmo de Parrinello-Rahman suprime oscilações ou ressonâncias severas que provocam a quebra artificial da caixa de simulação (\textit{crystal breaking}), fenômeno crítico quando o modelo condensa para a alta rigidez da fase gel ($L_\beta$) ou líquida-ordenada ($L_o$) \cite{pedersen2024}.

Para assegurar o cálculo preciso da lista de vizinhos (\textit{neighbor list}) e suprimir pressões artificiais causadoras de ondulações irreais e violação da isotropia espacial no modelo \textit{coarse-grained}, a tolerância do \textit{buffer} de Verlet foi desativada (\texttt{verlet-buffer-tolerance = -1}) acoplada a um raio de corte estendido para 1,35 nm, corroborando com as otimizações paramétricas do GROMACS exigidas pelo Martini 3 \cite{pedersen2024}. O banho térmico foi rigorosamente estabilizado via termostato \textit{velocity-rescaling} (\textit{v-rescale}) com constante de relaxamento $\tau_t = 1,0$ ps."""

        padrao = re.compile(r"O controle de press[aã]o isotr[oó]pica.*?\\tau_\{?t\}?\s*=\s*1,0\s*(?:~|\\ |)ps\.", re.DOTALL)
        if padrao.search(met_content):
            met_content = padrao.sub(texto_metodologia, met_content)
            with open(met_file, "w", encoding="utf-8") as f:
                f.write(met_content)
            print("✅ Metodologia justificada solidamente com base no Pedersen et al. 2024!")
        else:
            print("⚠️ Parágrafo da metodologia não encontrado (pode já estar atualizado).")

if __name__ == "__main__":
    arrumar_tudo()
