import re

with open('referencias.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

url_nova = "https://pubmed.ncbi.nlm.nih.gov/41019617/"

# Busca a chave colherinhas2025 e substitui apenas o que estiver dentro de url={...}
padrao_chave = r'(colherinhas2025.*?\burl\s*=\s*\{)(.*?)(\})'
# Fallback: busca pelo título da obra caso a chave seja diferente
padrao_titulo = r'([^\}]*?Insights into antiviral candidates against\s*oropouche virus.*?\burl\s*=\s*\{)(.*?)(\})'

if re.search(padrao_chave, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao_chave, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 20 (Colherinhas & Cardoso) atualizada pela chave com a URL oficial do PubMed!")
elif re.search(padrao_titulo, bib, flags=re.DOTALL | re.IGNORECASE):
    bib = re.sub(padrao_titulo, r'\g<1>' + url_nova + r'\g<3>', bib, flags=re.DOTALL | re.IGNORECASE, count=1)
    print("✅ Referência 20 atualizada pelo título da obra com sucesso!")
else:
    print("⚠️ Não consegui encontrar a referência do Colherinhas. Verifique o arquivo .bib.")

with open('referencias.bib', 'w', encoding='utf-8') as f:
    f.write(bib)

