import re

with open('referencias.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

# URL antiga que estava no PDF
url_antiga = "https://eprints.soton.ac.uk/499235/1/Chol_AIP_JCP_rev_2_clean.pdf"
url_nova = "https://pubmed.ncbi.nlm.nih.gov/39873279/"

# Tenta a substituição direta
if url_antiga in bib:
    bib = bib.replace(url_antiga, url_nova)
    print("✅ Referência 6 atualizada com a URL oficial do PubMed!")
else:
    # Se a URL estiver ligeiramente diferente no .bib, usa um regex blindado para a chave sawdon2025
    bib = re.sub(r'(?<=sawdon2025.*?)url\s*=\s*\{.*?\}', r'url = {' + url_nova + '}', bib, flags=re.DOTALL)
    print("✅ Referência 6 atualizada via Regex!")

with open('referencias.bib', 'w', encoding='utf-8') as f:
    f.write(bib)

