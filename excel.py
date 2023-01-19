import pandas as pd


global ProdExist, LocExist

x = pd.read_excel(r"C:\Users\Giovani\OneDrive - SESISENAISP - Corporativo\Área de Trabalho\Drone\codigos_GS1_v2.xlsx", engine='openpyxl')
#print(x)

data = '0107890000000062'
nullPL = 0

if data.isdigit():
    dataMod = int(data)
    print(type(dataMod))
else:
    dataMod = str(data)
    print(type(dataMod))


try:
    filtroP = x['Produto'] == dataMod #gera tabela true e false
    filtroPi = (x[filtroP].iloc[0,2])
    #filtroBoolP = (filtroP[0] == True)  #saber se tem mesmo true
    nullPL = 1
    print(filtroPi)

except:
    filtroL = x['Local'] == dataMod #gera tabela true e false
    filtroLi = (x[filtroL].iloc[0,0])
    #filtroBoolL = (filtroL[0] == True)  #saber se tem mesmo true
    nullPL = 2
    print(filtroLi)


print(nullPL)

