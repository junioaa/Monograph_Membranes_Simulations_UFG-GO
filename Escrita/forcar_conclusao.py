import re

with open('main.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

# 1. Varre e destrói qualquer chamada antiga ou comentada da conclusão
texto = re.sub(r'[ \t]*%?[ \t]*\\input\{07_conclusao\.tex\}\n*', '', texto)
texto = re.sub(r'[ \t]*%?[ \t]*\\include\{07_conclusao\}\n*', '', texto)

# 2. Força a injeção da conclusão no lugar absoluto (antes da bibliografia)
texto_atualizado = re.sub(r'(\\bibliography\{|\\printbibliography|\\section\*?\{Referências\}|\\chapter\*?\{Referências\}|\\input\{anexos)', 
                          r'\\input{07_conclusao.tex}\n\n\1', 
                          texto, count=1)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(texto_atualizado)

print("✅ main.tex limpo e Conclusão cravada no lugar exato!")
