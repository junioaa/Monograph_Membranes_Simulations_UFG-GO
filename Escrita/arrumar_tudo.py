import os
import re

# 1. Caça e substitui todos os estilos fantasmas no main.tex
with open('main.tex', 'r', encoding='utf-8') as f:
    texto_tex = f.read()
texto_tex = re.sub(r'\\bibliographystyle\{[^}]+\}', r'\\bibliographystyle{estilo_ufg}', texto_tex)
with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(texto_tex)

# 2. Puxa o estilo original e injeta o E comercial blindado
bst_path = os.popen('kpsewhich unsrtnat.bst').read().strip()
with open(bst_path, 'r', encoding='latin-1') as f:
    texto_bst = f.read()
texto_bst = texto_bst.replace('" and "', '" \\& "')
with open('estilo_ufg.bst', 'w', encoding='latin-1') as f:
    f.write(texto_bst)
