import re

with open('04_revisao_bibliografica.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# Expressão regular para encontrar o texto antigo, ignorando as quebras de linha que o LaTeX possa ter
trecho_antigo = r'A calibração das temperaturas de transição \(melting temperatures, Tm\) é a métrica definitiva para atestar o sucesso de um campo de força em membranas\..*?maneira espontânea \[18\]\.'

trecho_novo = r"A calibração das temperaturas de transição (\textit{melting temperatures}, $T_{m}$) constitui a métrica definitiva para atestar a precisão termodinâmica de um campo de força aplicável a biomembranas. Contudo, as barreiras cinéticas inerentes a esses sistemas introduzem severas complicações na amostragem. Observa-se que, em simulações de aquecimento ou resfriamento contínuo (\textit{simulated annealing}), o índice de Lindemann e a Área por Lipídio (APL) exibem forte histerese térmica. Esse fenômeno resulta em uma superestimação da $T_{m}$ em até 10 K, consequência direta da elevada energia de ativação necessária para romper ou reestruturar espontaneamente a rede de empacotamento apolar [18]."

# Aplica a substituição blindada
texto = re.sub(trecho_antigo, lambda m: trecho_novo, texto, flags=re.DOTALL | re.IGNORECASE)

with open('04_revisao_bibliografica.tex', 'w', encoding='utf-8') as f:
    f.write(texto)

print("✅ Trecho da referência [18] reescrito, formatado com itálicos e modo matemático, e atualizado com sucesso!")
