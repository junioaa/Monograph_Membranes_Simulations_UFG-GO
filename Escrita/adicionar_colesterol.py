import os

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modificado = False
        
        # Injeta Colesterol no Resumo em Português
        if 'Palavras-chave:' in content and 'DPPC. DSPC.' in content:
            if 'Colesterol.' not in content:
                content = content.replace('DPPC. DSPC.', 'Colesterol. DPPC. DSPC.')
                modificado = True
        
        # Injeta Cholesterol no Abstract em Inglês
        if 'Keywords:' in content and 'DPPC. DSPC.' in content:
            if 'Cholesterol.' not in content:
                content = content.replace('DPPC. DSPC.', 'Cholesterol. DPPC. DSPC.')
                modificado = True
                
        if modificado:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Palavras-chave atualizadas com sucesso no arquivo: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ As palavras-chave já foram atualizadas ou não foram encontradas.")
