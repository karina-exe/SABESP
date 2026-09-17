#Input. ♡

tipo_de_imovel = input("₊˚✩Digite o tipo de imóvel: ")
consumo_mensal = float(input("₊˚✩Digite o consumo mensal em m³: "))

#Processamento e saída. ♡

if tipo_de_imovel == "comercial":
    print("Tarifa comercial aplicada — consulte o plano corporativo.")
    import sys
    sys.exit()

elif tipo_de_imovel == "apartamento" and consumo_mensal <= 10:
    print("Consumo econômico — excelente consumo de água! ｡ﾟ+.ﾟ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ﾟ.+ﾟ｡")

if not consumo_mensal > 25:
    print("Consumo moderado — dentro do padrão residencial. (◕‿◕)")

else:
    print("Consumo excessivo — adote medidas de economia e verifique vazamentos. (｡•́︿•̀｡)")





