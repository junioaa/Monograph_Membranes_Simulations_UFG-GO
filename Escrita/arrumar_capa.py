import os

conteudo = r"""% --- CAPA ---
\thispagestyle{empty}
\begin{center}
{\fontsize{12}{13.8}\selectfont
UNIVERSIDADE FEDERAL DE GOIÁS \\
\textsc{Instituto de Física} \\
\textsc{Curso de Física Médica}\par}

\vspace*{11\baselineskip}

{\fontsize{12}{13.8}\selectfont CARLOS JUNIO ALVES DOS SANTOS\par}

\vspace*{4\baselineskip}

{\fontsize{16}{18.4}\selectfont \textbf{BIOFÍSICA COMPUTACIONAL DE MEMBRANAS LIPÍDICAS: MODELAGEM \textit{COARSE-GRAINED}, TERMODINÂMICA DE FASES E METAESTABILIDADE}\par}

\vspace*{\fill}

{\fontsize{14}{16.1}\selectfont \textsc{Trabalho de Conclusão de Curso}\par}

\vspace*{5\baselineskip}

{\fontsize{12}{13.8}\selectfont
\textsc{Goiânia} \\
2026\par}
\end{center}

% --- PÁGINA PARA O TECA ---
\newpage
\begin{center}
\vspace*{10cm}
\textit{[Esta página é reservada para a inserção do Termo de Ciência e de Autorização (TECA)]}
\end{center}

% --- FOLHA DE ROSTO ---
\newpage
\begin{center}
{\fontsize{12}{13.8}\selectfont
UNIVERSIDADE FEDERAL DE GOIÁS \\
\textsc{Instituto de Física} \\
\textsc{Curso de Física Médica}\par}

\vspace*{9\baselineskip}

{\fontsize{12}{13.8}\selectfont CARLOS JUNIO ALVES DOS SANTOS\par}

\vspace*{4\baselineskip}

{\fontsize{16}{18.4}\selectfont \textbf{BIOFÍSICA COMPUTACIONAL DE MEMBRANAS LIPÍDICAS: MODELAGEM \textit{COARSE-GRAINED}, TERMODINÂMICA DE FASES E METAESTABILIDADE}\par}

\vspace*{\baselineskip}

\vspace*{1cm}
\noindent\hspace*{7cm}
\begin{minipage}{\dimexpr\textwidth-7cm\relax}
\fontsize{12}{13.8}\selectfont
Monografia apresentada na disciplina de Trabalho de Conclusão de Curso da graduação em Física Médica do Instituto de Física da Universidade Federal de Goiás.

\vspace{\baselineskip}
Orientador: Prof. Dr. Wesley Bueno Cardoso
\end{minipage}

\vspace*{\fill}

{\fontsize{12}{13.8}\selectfont \textsc{Goiânia} \\ 2026\par}
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
\vspace*{\fill}
\begin{flushright}
\fontsize{11}{13.2}\selectfont\itshape
Dedico este trabalho à minha família, \\
pelo apoio incondicional em toda a minha jornada, \\
e a todos que impulsionam o avanço da física médica.
\end{flushright}
\vspace*{2cm}

% --- AGRADECIMENTOS ---
\newpage
\begin{center}
{\fontsize{17}{20.4}\selectfont \textbf{AGRADECIMENTOS}}
\end{center}
\vspace*{1cm}
Agradeço primeiramente ao meu orientador, Prof. Dr. Wesley Bueno Cardoso, pela confiança e direcionamento ímpar ao longo deste trabalho. Agradeço também ao Instituto de Física da UFG por toda a infraestrutura acadêmica, e ao Mateus, pela parceria e compartilhamento dos recursos computacionais que tornaram estas simulações de Dinâmica Molecular possíveis.
\newpage
"""

with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(conteudo)

print("✅ Capa e Folha de Rosto atualizadas com as fontes Versaletes e Maiúsculas do padrão UFG!")
