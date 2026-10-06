import os
import re

arquivo_metodologia = "05_metodologia.tex"

texto_novo = r"""O rigor na configuração dos algoritmos de integração e controle termodinâmico baseou-se estritamente nas diretrizes recentes estabelecidas por Pedersen \textit{et al.} para a estabilidade do lipidoma Martini 3 \cite{pedersen2024}. O controle de pressão \textbf{semi-isotrópico} (desacoplando as flutuações do plano lateral XY em relação ao eixo transversal Z) foi mantido a 1 bar utilizando o barostato estocástico \textit{cell-rescaling} (\textit{c-rescale}) acoplado a uma constante de tempo de 4,0 ps e compressibilidade de $3\times10^{-4}\text{ bar}^{-1}$. A adoção do controle semi-isotrópico é mandatória para bicamadas lipídicas, garantindo a livre flutuação mecânica da área transversal da membrana. Além disso, a escolha do \textit{c-rescale} em detrimento do clássico algoritmo de Parrinello-Rahman justifica-se por sua propriedade de relaxamento exponencial, que previne ressonâncias acústicas severas e a fratura artificial da caixa de simulação (\textit{crystal breaking}) quando a matriz assume características sólidas e inelásticas na fase \textit{gel} ($L_\beta$) \cite{pedersen2024}.

Adicionalmente, para mitigar artefatos de pressão irreais e a violação da isotropia espacial inerentes ao cálculo computacional da lista de vizinhos (\textit{neighbor list}) em simulações \textit{coarse-grained}, a tolerância do \textit{buffer} de Verlet foi explicitamente desativada (\texttt{verlet-buffer-tolerance = -1}) e o raio de corte da lista estendido para 1,35 nm (\texttt{rlist = 1.35}), assegurando a reprodutibilidade estrutural e a integridade da tensão superficial \cite{pedersen2024}. O banho térmico foi rigorosamente controlado via termostato \textit{velocity-rescaling} (\textit{v-rescale}) com constante de relaxamento $\tau_{t}=1,0$ ps."""

def atualizar_metodologia():
    if not os.path.exists(arquivo_metodologia):
        print(f"Erro: O arquivo {arquivo_metodologia} não foi encontrado no diretório atual.")
        return

    # Faz um backup do arquivo antes de editá-lo
    os.system(f"cp {arquivo_metodologia} {arquivo_metodologia}.backup_mdp")
    
    with open(arquivo_metodologia, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Regex que captura o parágrafo original sobre barostato/termostato
    padrao = re.compile(
        r"O controle de pressão isotrópica.*?\\tau_\{?t\}?\s*=\s*1,0\s*(?:~|\\ )?ps\.", 
        re.DOTALL
    )
    
    if padrao.search(conteudo):
        conteudo_atualizado = padrao.sub(texto_novo, conteudo)
        with open(arquivo_metodologia, "w", encoding="utf-8") as f:
            f.write(conteudo_atualizado)
        print("✅ Metodologia atualizada com sucesso!")
        print("✅ A correção para 'semi-isotrópico' e as fundamentações de Pedersen et al. foram inseridas perfeitamente.")
    elif "pedersen2024" in conteudo and "c-rescale" in conteudo:
        print("⚠️ A metodologia aparentemente já possui o texto atualizado.")
    else:
        print("❌ Não foi possível localizar automaticamente o parágrafo. O texto pode ter sofrido alterações recentes de formatação.")

if __name__ == "__main__":
    atualizar_metodologia()
