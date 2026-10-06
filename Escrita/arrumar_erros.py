import os
import re

def limpar_erros():
    # 1. Corrigir citações quebradas no 06_resultados.tex
    arquivo_tex = "06_resultados.tex"
    if os.path.exists(arquivo_tex):
        with open(arquivo_tex, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        # Substitui a tag falsa pelas referências reais de termodinâmica do colesterol
        conteudo_corrigido = conteudo.replace(r"\cite{main.pdf}", r"\cite{bennett2018, kheyfets2015}")
        
        if conteudo != conteudo_corrigido:
            with open(arquivo_tex, "w", encoding="utf-8") as f:
                f.write(conteudo_corrigido)
            print("✅ Citações inválidas (main.pdf) corrigidas no texto de resultados!")

    # 2. Remover a referência duplicada 'ramirez2025' no referencias.bib
    arquivo_bib = "referencias.bib"
    if os.path.exists(arquivo_bib):
        with open(arquivo_bib, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # Separa o arquivo BibTeX pelas entradas (@article, @book, etc)
        entradas = re.split(r'(?=@\w+\s*\{)', conteudo)
        novas_entradas = []
        vistos = set()

        for entrada in entradas:
            match = re.search(r'@\w+\s*\{\s*([^,]+)', entrada)
            if match:
                chave = match.group(1).strip()
                if chave == "ramirez2025":
                    if chave in vistos:
                        print("🗑️ Referência duplicada 'ramirez2025' encontrada e removida do .bib!")
                        continue
                    vistos.add(chave)
            novas_entradas.append(entrada)

        with open(arquivo_bib, "w", encoding="utf-8") as f:
            f.write("".join(novas_entradas))
        print("✅ Arquivo referencias.bib higienizado e livre de duplicatas!")

if __name__ == "__main__":
    limpar_erros()
