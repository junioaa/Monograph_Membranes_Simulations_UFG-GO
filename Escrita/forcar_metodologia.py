import os
import re

def forcar_metodologia():
    arquivo = "05_metodologia.tex"
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo {arquivo} não encontrado.")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        met = f.read()

    texto_novo = r"""Os parâmetros de integração algorítmica e o controle termodinâmico adotados neste trabalho fundamentam-se nas diretrizes do estado da arte validadas por Pedersen \textit{et al.} para a estabilidade do lipidoma Martini 3 \cite{pedersen2024}. O controle de pressão \textbf{semi-isotrópico} foi empregado visando a dilatação e contração autônoma do plano lateral da membrana (eixos X e Y) desvinculada do eixo transversal (Z), condição mecânica exigida para bicamadas lipídicas. 

A pressão foi mantida a 1 bar pelo barostato estocástico \textit{cell-rescaling} (\textit{c-rescale}), utilizando constante de tempo $\tau_p = 4,0$ ps e compressibilidade de $3\times10^{-4}\text{ bar}^{-1}$. A escolha do \textit{c-rescale} em detrimento do algoritmo clássico de Parrinello-Rahman suprime ressonâncias mecânicas que provocam a quebra artificial da caixa de simulação (\textit{crystal breaking}), um fenômeno crítico quando o modelo condensa para a alta rigidez da fase gel ($L_\beta$) ou líquida-ordenada ($L_o$) \cite{pedersen2024}.

Para assegurar o cálculo preciso da lista de vizinhos (\textit{neighbor list}) e suprimir pressões artificiais causadoras de ondulações irreais e violação da isotropia espacial no modelo \textit{coarse-grained}, a tolerância do \textit{buffer} de Verlet foi desativada (\texttt{verlet-buffer-tolerance = -1}) e acoplada a um raio de corte estendido para 1,35 nm, corroborando com as otimizações paramétricas do GROMACS exigidas pelo Martini 3 \cite{pedersen2024}. O banho térmico foi rigorosamente estabilizado via termostato \textit{velocity-rescaling} (\textit{v-rescale}) com constante de relaxamento $\tau_t = 1,0$ ps."""

    # Expressão hiper tolerante que ignora quebras de linha e formatações ocultas do LaTeX
    # Pega de "O controle de press" até a palavra "ps." passando por tudo no meio
    padrao = re.compile(r"O controle de press.*?1,0.*?ps\.", re.DOTALL | re.IGNORECASE)
    
    if padrao.search(met):
        met = padrao.sub(texto_novo, met)
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(met)
        print("✅ Sucesso! A Metodologia foi reescrita e blindada com base no artigo de 2024.")
    else:
        print("❌ Texto original não encontrado. Abra o arquivo '05_metodologia.tex' e faça a substituição manualmente.")

if __name__ == "__main__":
    forcar_metodologia()
