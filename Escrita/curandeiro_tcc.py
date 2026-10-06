import os
import re

# 1. RECRIAR OS PRÉ-TEXTUAIS COM A LISTA DE ABREVIATURAS E SÍMBOLOS (Padrão UFG)
pre_textuais = r"""
% --- CAPA ---
\begin{titlepage}
\begin{center}
{\fontsize{12}{14.4}\selectfont \textbf{UNIVERSIDADE FEDERAL DE GOIÁS} \\
\textbf{INSTITUTO DE FÍSICA} \\
\textbf{CURSO DE FÍSICA MÉDICA}} \\

\vspace*{11\baselineskip}

{\fontsize{12}{14.4}\selectfont \textbf{CARLOS JUNIO ALVES DOS SANTOS}} \\

\vspace*{4\baselineskip}

{\fontsize{16}{19.2}\selectfont \textbf{BIOFÍSICA COMPUTACIONAL DE MEMBRANAS LIPÍDICAS: MODELAGEM \textit{COARSE-GRAINED}, TERMODINÂMICA DE FASES E METAESTABILIDADE}} \\

\vfill

{\fontsize{12}{14.4}\selectfont \textbf{GOIÂNIA} \\
\textbf{2026}}
\end{center}
\end{titlepage}

% --- PÁGINA PARA O TECA ---
\newpage
\begin{center}
\vspace*{10cm}
\textit{[Esta página é reservada para a inserção do Termo de Ciência e de Autorização (TECA)]}
\end{center}

% --- FOLHA DE ROSTO ---
\newpage
\begin{center}
{\fontsize{12}{14.4}\selectfont \textbf{CARLOS JUNIO ALVES DOS SANTOS}} \\

\vspace*{4\baselineskip}

{\fontsize{16}{19.2}\selectfont \textbf{BIOFÍSICA COMPUTACIONAL DE MEMBRANAS LIPÍDICAS: MODELAGEM \textit{COARSE-GRAINED}, TERMODINÂMICA DE FASES E METAESTABILIDADE}} \\

\vspace*{2\baselineskip}

\begin{flushright}
\begin{minipage}{8cm}
\fontsize{12}{14.4}\selectfont
Monografia apresentada na disciplina de Trabalho de Conclusão de Curso da graduação em Física Médica do Instituto de Física da Universidade Federal de Goiás.

\vspace{\baselineskip}
Orientador: Prof. Dr. Wesley Bueno Cardoso
\end{minipage}
\end{flushright}

\vfill

{\fontsize{12}{14.4}\selectfont \textbf{GOIÂNIA} \\
\textbf{2026}}
\end{center}

% --- FICHA CATALOGRÁFICA E FOLHA DE APROVAÇÃO ---
\newpage
\begin{center}
\vspace*{10cm}
\textit{[Página reservada para a Ficha Catalográfica]}
\end{center}
\newpage
\begin{center}
\vspace*{10cm}
\textit{[Página reservada para a Folha de Aprovação da Banca]}
\end{center}

% --- DEDICATÓRIA ---
\newpage
\vspace*{20cm}
\begin{flushright}
\textit{Dedico este trabalho à minha família, \\
pelo apoio incondicional em toda a minha jornada, \\
e a todos que impulsionam o avanço da física médica.}
\end{flushright}

% --- AGRADECIMENTOS ---
\newpage
\begin{center}
{\fontsize{17}{20.4}\selectfont \textbf{AGRADECIMENTOS}}
\end{center}
\vspace*{1cm}
Agradeço primeiramente ao meu orientador, Prof. Dr. Wesley Bueno Cardoso, pela confiança e direcionamento ímpar ao longo deste trabalho. Agradeço também ao Instituto de Física da UFG por toda a infraestrutura acadêmica, e ao Mateus, pela parceria e compartilhamento dos recursos computacionais que tornaram estas simulações de Dinâmica Molecular possíveis. 

% --- LISTA DE ABREVIATURAS E SÍMBOLOS ---
\newpage
\begin{center}
{\fontsize{17}{20.4}\selectfont \textbf{LISTA DE ABREVIATURAS E SÍMBOLOS}}
\end{center}
\vspace{18pt}

{\fontsize{12}{14.4}\selectfont \textbf{ABREVIATURAS}} \\
\vspace{6pt}
\begin{tabbing}
\hspace{2cm} \= \kill
APL \> Área por Lipídio \\
CG \> \textit{Coarse-Grained} \\
DM \> Dinâmica Molecular \\
DPPC \> Dipalmitoilfosfatidilcolina \\
DSPC \> Diestearoilfosfatidilcolina \\
EPR \> Ressonância Paramagnética Eletrônica \\
OROV \> Vírus Oropouche
\end{tabbing}

\vspace{12pt}
{\fontsize{12}{14.4}\selectfont \textbf{SÍMBOLOS}} \\
\vspace{6pt}
{\fontsize{12}{14.4}\selectfont \textbf{Letras Arábicas}} \\
\begin{tabbing}
\hspace{2cm} \= \kill
$C_p$ \> Capacidade Calorífica \\
$D_{HH}$ \> Distância pico-a-pico da densidade eletrônica \\
$D_B$ \> Espessura da Bicamada \\
$E_{Tot}$ \> Energia Total \\
$T_m$ \> Temperatura de Transição Principal
\end{tabbing}
\vspace{6pt}

{\fontsize{12}{14.4}\selectfont \textbf{Letras Gregas}} \\
\begin{tabbing}
\hspace{2cm} \= \kill
$L_\alpha$ \> Fase Fluida Desordenada \\
$L_\beta$ \> Fase Gel Sólida \\
$L_o$ \> Fase Líquida-Ordenada
\end{tabbing}
\newpage
"""
with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(pre_textuais)


# 2. VARRER TODOS OS ARQUIVOS .tex E CURAR OS COMANDOS ENGOLIDOS
for arquivo in os.listdir('.'):
    if arquivo.endswith('.tex'):
        with open(arquivo, 'r', encoding='utf-8') as f:
            texto = f.read()

        # Cura dos comandos estruturais do documento principal
        texto = texto.replace('begindocument', r'\begin{document}')
        texto = texto.replace('pagenumberingroman', r'\pagenumbering{roman}')
        texto = texto.replace('pagenumberingarabic', r'\pagenumbering{arabic}')
        texto = texto.replace('input00 pre extuais.tex', r'\input{00_pre_textuais.tex}')
        
        # O regex captura a quebra de seção (ex: "section 0 INTRODUÇÃO") e reconstrói as chaves (\section{INTRODUÇÃO})
        texto = re.sub(r'(?<!\\)\b(section|subsection|subsubsection)\s*0\.?0?\s*(.*?)\n', r'\\\1{\2}\n', texto)
        
        # Cura citações destruídas (" [?]]crippa2023" -> "\cite{crippa2023}")
        texto = re.sub(r'\[\?\]\]\s*([a-zA-Z0-9_]+)', r'\\cite{\1}', texto)

        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(texto)


# 3. INJETAR O PACOTE TITLESEC PARA AS FONTES DA UFG (17pt e 14pt) NO main.tex
with open('main.tex', 'r', encoding='utf-8') as f:
    main_tex = f.read()

if 'titlesec' not in main_tex:
    formatacao_ufg = r"""
\usepackage{titlesec}
\titleformat{\section}{\normalfont\fontsize{17}{20.4}\bfseries\uppercase}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{12pt}{12pt}
\titleformat{\subsection}{\normalfont\fontsize{14}{16.8}\bfseries\uppercase}{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{12pt}{6pt}
\titleformat{\subsubsection}{\normalfont\fontsize{12}{14.4}\itshape}{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{10pt}{6pt}
"""
    # Injeta a formatação logo após a chamada de algum pacote existente
    main_tex = re.sub(r'(\\usepackage.*?)\n', r'\1\n' + formatacao_ufg, main_tex, count=1)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main_tex)

print("✅ TCC Curado! Comandos restaurados, Listas geradas e Formatação da UFG aplicada.")
