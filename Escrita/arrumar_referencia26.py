import re

with open('referencias.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

url_nova = "https://drive.google.com/file/d/1IwxxJoRjG2kfvwcWn2t-hrJo_pSsm_ra/view?usp=drive_link"

# 1. Tenta substituir o campo 'url' se ele já existir (buscando pelo título)
padrao_titulo = r'([^\}]*?F[íi]sica Experimental I: Notas introdut[óo]rias.*?\burl\s*=\s*\{)(.*?)(\})'

if re.search(padrao_titulo, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao_titulo, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 26 (Apostila UFG) atualizada com a URL do Google Drive!")
else:
    # 2. Se o campo 'url' NÃO existir, injeta ele antes de fechar a referência
    padrao_add = r'((?:@[a-zA-Z]+\{)[^@]*?F[íi]sica Experimental I: Notas introdut[óo]rias.*?)(\n\})'
    if re.search(padrao_add, bib, flags=re.DOTALL | re.IGNORECASE):
        bib = re.sub(padrao_add, r'\g<1>,\n  url = {' + url_nova + r'}\g<2>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
        print("✅ Campo URL criado e adicionado à Referência 26 com sucesso!")
    else:
        print("⚠️ Não consegui encontrar a referência 26. Verifique o arquivo .bib.")

with open('referencias.bib', 'w', encoding='utf-8') as f:
    f.write(bib)

