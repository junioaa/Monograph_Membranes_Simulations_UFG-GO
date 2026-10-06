import os
bst_path = os.popen('kpsewhich unsrtnat.bst').read().strip()

with open(bst_path, 'r', encoding='latin-1') as f:
    texto = f.read()

# Ataca a função nativa do unsrtnat e as strings soltas
texto = texto.replace('{ "and"}', '{ "\\&"}')
texto = texto.replace('" and "', '" \\& "')

with open('estilo_ufg.bst', 'w', encoding='latin-1') as f:
    f.write(texto)
