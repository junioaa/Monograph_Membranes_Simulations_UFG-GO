import re

with open('main.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# Verifica se a conclusão já foi inserida para evitar duplicação
if '07_conclusao.tex' not in texto and '07_conclusao' not in texto:
    # Procura a declaração da bibliografia e insere a conclusão ANTES dela
    # Expressão regular ajustada para capturar \bibliography, \printbibliography, ou a seção de anexos
    texto_atualizado = re.sub(r'(\\bibliography\{|\\printbibliography|\\section\*?\{Referências\}|\\chapter\*?\{Referências\}|\\input\{anexos)', 
                              r'\\input{07_conclusao.tex}\n\n\1', 
                              texto)
    
    with open('main.tex', 'w', encoding='utf-8') as f:
        f.write(texto_atualizado)
    print("✅ Chamada da Conclusão inserida no main.tex!")
else:
    print("⚠️ A chamada da Conclusão já existe no main.tex.")
