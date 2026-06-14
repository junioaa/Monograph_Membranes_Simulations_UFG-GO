import re

with open('00_pre_textuais.tex', 'r', encoding='utf-8') as f:
    pre = f.read()

novo_agradecimento = r"""\begin{center}
{\fontsize{17}{20.4}\selectfont \textbf{AGRADECIMENTOS}}
\end{center}
\vspace*{1cm}

Agradeço primeiramente ao meu orientador, Prof. Dr. Wesley Bueno Cardoso, pela confiança e direcionamento ímpar ao longo deste trabalho.

Agradeço ao Instituto de Física da UFG por toda a infraestrutura acadêmica, bem como a todos os professores da universidade com os quais tive o privilégio de aprender, não me restringindo apenas aos do Instituto. Estendo essa gratidão a todos os meus antigos professores, que foram fundamentais na minha formação desde o início da minha caminhada escolar.

Expresso também minha profunda reverência aos grandes pensadores e sábios que nos antecederam, que desbravaram um mundo muito diferente do nosso e cujas descobertas pavimentaram o caminho para que pudéssemos desfrutar da ciência e da tecnologia no mundo contemporâneo.

À minha família, pelo amor e apoio incondicional em todas as etapas desta jornada, e aos meus amigos, pela parceria e por estarem sempre ao meu lado.

Por fim, agradeço a todos que viabilizaram os recursos computacionais que tornaram estas simulações de Dinâmica Molecular possíveis.

\newpage"""

# A função 'lambda m:' impede o Python de tentar traduzir as barras invertidas
pre = re.sub(
    r'\\begin\{center\}\n\{\\fontsize\{17\}\{20\.4\}\\selectfont \\textbf\{AGRADECIMENTOS\}\}.*?\\newpage', 
    lambda m: novo_agradecimento, 
    pre, 
    flags=re.DOTALL
)

with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(pre)

print("✅ Agradecimentos atualizados com sucesso e blindados contra o Python!")
