# Input. ♡

print("Como parte do nosso programa de conscientização, a SABESP-サベスピ- desenvolveu um sistema"
      " de análise do consumo mensal de água.")
print("Nosso sistema converte o metro cúbico (m³) em litros, com a finalidade de"
      " trazer consciência em relação a quantidade de água utilizada.")
print("Desse modo, a SABESP-サベスピ- tem como objetivo incentivar o consumo responsável.")

tipo_de_imovel = input("₊˚✩Digite o tipo de imóvel (casa, apartamento ou comercial): ")
consumo_mensal = float(input("₊˚✩Digite o consumo mensal em metros cúbicos (m³): "))

# Processamento (conversão de m³ em litros) e saída de informações através das condicionais. ♡

def volume():
    return consumo_mensal * 1000
resultado = volume()
print(f"Seu consumo mensal é de {volume()}ℓ (litros).⋆.౨ৎ˚.⟡˖ ࣪")

if tipo_de_imovel == "comercial":
    print("Tarifa comercial aplicada — consulte o plano corporativo.")

elif tipo_de_imovel == "apartamento" and consumo_mensal < 10:
    print("Consumo econômico — excelente consumo de água! ｡ﾟ+.ﾟ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ﾟ.+ﾟ｡")


elif consumo_mensal <= 25 and tipo_de_imovel == "casa" or tipo_de_imovel == "apartamento":
     print("Consumo moderado — dentro do padrão residencial. (◕‿◕)")

else:
    print("Consumo excessivo — adote medidas de economia e verifique vazamentos. (｡•́︿•̀｡)"
          " Para mais informações, entre em contato através do canal de atendimento.")


exit()