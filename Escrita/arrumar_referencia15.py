import re

with open('referencias.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

url_nova = "https://pubmed.ncbi.nlm.nih.gov/23924441/"

# Busca a chave venable2013 e substitui apenas o que estiver dentro de url={...}
padrao = r'(venable2013.*?\burl\s*=\s*\{)(.*?)(\})'

if re.search(padrao, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 15 (Venable et al.) atualizada com a URL oficial do PubMed!")
else:
    print("⚠️ Não consegui encontrar a chave 'venable2013'. Verifique se o nome está correto no .bib.")

with open('referencias.bib', 'w', encoding='utf-8') as f:
    f.write(bib)

