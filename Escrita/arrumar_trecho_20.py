import re

with open('04_revisao_bibliografica.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# Expressão regular para capturar o trecho antigo, não importando como o LaTeX quebrou as linhas ou palavras
trecho_antigo = r'Colherinhas e Cardoso \(2025\) executaram simulações.*?coordenadas energéticas sofreram\s*metamorfose\.'

# O novo texto impessoal, limpo e com a tipografia correta
trecho_novo = r"Simulações de espectro atomístico pareadas foram conduzidas para testar a inibição competitiva da glicoproteína celular Gc do envelope viral do OROV, utilizando acervos de retrovirais classicamente prescritos contra proteases do HIV [20]. Abordagens teóricas conservadoras pautadas em ancoragem computacional rígida (\textit{Molecular Docking}) posicionaram erroneamente o fármaco Saquinavir no topo do escalonamento de afinidade. Todavia, quando o complexo ligante-proteína foi mergulhado e submetido aos fluxos solvatados ininterruptos da modelagem molecular de longa duração, as coordenadas energéticas sofreram metamorfose."

# Substituição blindada
texto_atualizado = re.sub(trecho_antigo, lambda m: trecho_novo, texto, flags=re.DOTALL | re.IGNORECASE)

if texto != texto_atualizado:
    with open('04_revisao_bibliografica.tex', 'w', encoding='utf-8') as f:
        f.write(texto_atualizado)
    print("✅ Trecho da referência [20] reescrito para o formato impessoal com sucesso!")
else:
    print("⚠️ Não encontrei o trecho exato. Verifique se ele já não foi alterado.")

