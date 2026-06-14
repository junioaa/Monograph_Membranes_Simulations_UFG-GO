import re

with open('00_pre_textuais.tex', 'r', encoding='utf-8') as f:
    pre = f.read()

# Usa expressão regular para apagar tudo desde o título da Dedicatória até os Agradecimentos
pre = re.sub(r'% --- DEDICATÓRIA ---.*?(?=% --- AGRADECIMENTOS ---)', '', pre, flags=re.DOTALL)

with open('00_pre_textuais.tex', 'w', encoding='utf-8') as f:
    f.write(pre)

print("✅ Página de Dedicatória removida com sucesso!")
