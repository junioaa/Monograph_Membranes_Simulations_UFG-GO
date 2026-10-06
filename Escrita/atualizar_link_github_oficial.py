import re

with open('03_metodologia.tex', 'r', encoding='utf-8') as f:
    texto = f.read()

link_oficial = "https://github.com/junioaa/TCC_Membranes_UFG"

# Substitui tanto o link de placeholder genérico quanto o link hipotético do script anterior
texto = texto.replace("https://github.com/carlosjunio/tcc-membranas-cg", link_oficial)
texto = texto.replace("https://github.com/SEU-USUARIO/SEU-REPOSIT", link_oficial)

with open('03_metodologia.tex', 'w', encoding='utf-8') as f:
    f.write(texto)

print(f"✅ Link oficial do GitHub cravado na Metodologia: {link_oficial}")
