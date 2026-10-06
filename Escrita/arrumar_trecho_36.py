import os
import re

encontrou = False

for file in os.listdir('.'):
    if file.endswith('.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procura os marcadores antigos no arquivo
        if 'Heerklotz e Epand' in content and 'ASAap' in content:
            
            # Expressão regular flexível para capturar o trecho ignorando quebras de linha
            padrao = r'Os cálculos termodinâmicos demonstram que esta sutil substituição de volume reduziu o\s*Cp da mistura metaestável.*?cadeias acílicas \[36\]\.'
            
            # O novo parágrafo impessoal e matematicamente formatado
            novo_paragrafo = r"Os cálculos termodinâmicos demonstram que esta sutil substituição de volume reduziu a capacidade calorífica ($C_{p}$) da mistura metaestável (entre 290 K e 300 K) para $\approx 0,68$ kJ/mol/K. Esta correlação direta entre o encurtamento da cadeia e a queda da capacidade calorífica encontra robusta validação experimental na literatura biocalorimétrica. Estudos baseados em calorimetria isotérmica demonstraram que a entalpia de empacotamento e a capacidade calorífica de fosfolipídios são medidas fenomenológicas estritamente dependentes da Área de Superfície Apolar ($ASA_{ap}$) e do número de grupos metileno das cadeias acílicas [36]."
            
            content_atualizado = re.sub(padrao, lambda m: novo_paragrafo, content, flags=re.DOTALL | re.IGNORECASE)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content_atualizado)
            
            print(f"✅ Trecho da referência [36] (Heerklotz e Epand) atualizado com sucesso no arquivo: {file}")
            encontrou = True

if not encontrou:
    print("⚠️ Não encontrei o trecho. Verifique se ele já não foi alterado.")
