import os

link_oficial = "https://github.com/junioaa/TCC_Membranes_UFG"
encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verifica se os links antigos/provisórios estão neste arquivo
        if "https://github.com/carlosjunio/tcc-membranas-cg" in content or "https://github.com/SEU-USUARIO/SEU-REPOSIT" in content:
            
            # Faz a substituição
            content = content.replace("https://github.com/carlosjunio/tcc-membranas-cg", link_oficial)
            content = content.replace("https://github.com/SEU-USUARIO/SEU-REPOSIT", link_oficial)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Link oficial do GitHub cravado com sucesso no arquivo: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ Não encontrei os links provisórios. Se o link antigo era diferente, me avise!")
