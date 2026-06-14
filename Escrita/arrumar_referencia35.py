import re

with open('referencias.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

url_nova = "https://pubmed.ncbi.nlm.nih.gov/21430953/"

# 1. Tenta substituir o campo 'url' se ele já existir (por chave ou por título)
padrao_chave = r'(raudino2011.*?\burl\s*=\s*\{)(.*?)(\})'
padrao_titulo = r'([^\}]*?The thermodynamics of\s*simple biomembrane mimetic systems.*?\burl\s*=\s*\{)(.*?)(\})'

if re.search(padrao_chave, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao_chave, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 35 (Raudino et al.) atualizada pela chave com a URL do PubMed!")
elif re.search(padrao_titulo, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao_titulo, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 35 atualizada pelo título da obra com sucesso!")
else:
    # 2. Se o campo 'url' NÃO existir, injeta ele antes de fechar a referência
    padrao_add = r'((?:@[a-zA-Z]+\{)[^@]*?The thermodynamics of\s*simple biomembrane mimetic systems.*?)(\n\})'
    if re.search(padrao_add, bib, flags=re.DOTALL | re.IGNORECASE):
        bib = re.sub(padrao_add, r'\g<1>,\n  url = {' + url_nova + r'}\g<2>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
        print("✅ Campo URL criado e adicionado à Referência 35 com sucesso!")
    else:
        print("⚠️ Não consegui encontrar a referência 35. Verifique o arquivo .bib.")

with open('referencias.bib', 'w', encoding='utf-8') as f:
    f.write(bib)

