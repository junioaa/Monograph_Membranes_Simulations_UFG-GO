import re
import os

def fix_files():
    # 1. CORRIGIR O ARQUIVO DE REFERÊNCIAS (.bib)
    bib_content = """@article{pedersen2024,
  author = {Pedersen, Kasper B. and others},
  title = {The Martini 3 Lipidome: Expanded and Refined Parameters Improve Lipid Phase Behavior},
  journal = {ACS Central Science},
  volume = {11},
  number = {9},
  pages = {1598-1610},
  year = {2024},
  doi = {10.1021/acscentsci.5c00755}
}

@article{lu2017,
  author = {Lu, Tao and ten Hagen, Timo L. M.},
  title = {Inhomogeneous crystal grain formation in DPPC-DSPC based thermosensitive liposomes determines content release kinetics},
  journal = {Journal of Controlled Release},
  volume = {247},
  pages = {64-72},
  year = {2017},
  doi = {10.1016/j.jconrel.2016.12.020}
}

@article{ramirez2025,
  author = {Ramirez-Echemendia, Daniel P. and others},
  title = {Gradient-Based Optimization of Force Field Parameters for Martini Lipid Models},
  journal = {ChemRxiv},
  year = {2025},
  doi = {10.26434/chemrxiv-2025-dtt4k}
}"""
    
    with open('referencias.bib', 'w') as f:
        f.write(bib_content)
    print("✅ Arquivo referencias.bib atualizado com as 3 referências.")

    # 2. CORRIGIR O ARQUIVO PRINCIPAL (.tex)
    if not os.path.exists('main.tex'):
        print("❌ Erro: main.tex não encontrado!")
        return

    with open('main.tex', 'r') as f:
        content = f.read()

    # Corrigir o erro de citação [?] e remover citações inexistentes
    content = content.replace('\\cite{pedersen2024martini}', '\\cite{pedersen2024}')
    content = content.replace('\\cite{main_pdf}', '')
    
    # Corrigir a legenda quebrada da Figura 8 (Runaway Argument)
    pattern_caption = r'\\caption\{Efeito da hidratação na área por lipídio para sistemas de DPPC puro \(100:0\)\. As cores seguem o padrão visual de identificação: 15 \$W/.*\}'
    fixed_caption = r'\\caption{Efeito da hidratação na área por lipídio para sistemas de DPPC puro (100:0). As cores seguem o padrão visual: 15 $W/L$ (azul), 27 $W/L$ (vermelho), 40 $W/L$ (verde) e 45 $W/L$ (amarelo).}'
    content = re.sub(r'\\caption\{Efeito da hidratação na área por lipídio para sistemas de DPPC puro \(100:0\)\. As cores seguem o padrão visual de identificação: 15 \$W/.*\}', fixed_caption, content)

    # Remover a SEGUNDA definição da figura (evitar Label Multiply Defined)
    # Procuramos o bloco da figura do sal e removemos a segunda ocorrência
    figure_blocks = re.findall(r'\\begin\{figure\}.*?fig:grafico_salt.*?\\end\{figure\}', content, re.DOTALL)
    if len(figure_blocks) > 1:
        # Mantemos apenas a primeira e substituímos a segunda por um comentário
        content = content.replace(figure_blocks[1], "% Figura duplicada removida automaticamente")

    with open('main.tex', 'w') as f:
        f.write(content)
    print("✅ Arquivo main.tex corrigido (Legendas, Citações e Labels).")

if __name__ == "__main__":
    fix_files()
