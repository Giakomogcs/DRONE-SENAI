import csv
import pandas as pd

filename = "workbook.csv"
header = ("Produto", "Local")
data = [211299991, "Gioivan21"]
'''
with open (filename, "w", newline = "") as csvfile: #apaga tudo e escreve
    file = csv.writer(csvfile)
    file.writerow(header)
    #file.writerow(data)
    csvfile.close()

'''
    
    


'''
with open (filename, "a", newline = "") as csvfile:  #adiciona conteudo em arquivo sem apagar
    file = csv.writer(csvfile)
    
    file.writerow(data)
    csvfile.close()


work = pd.read_excel(r"workbook.xlsx")
work.to_csv (r"workbook.csv", index=False)
'''


'''
with open (filename, "w", newline = "") as csvfile: #apaga tudo e escreve
    file = csv.writer(csvfile)
    file.writerow(header)
    #file.writerow(data)
    csvfile.close()
'''


'''
'''
try: 
    filtered_prod = pd.read_csv("workbook.csv", usecols=["Produto"]) #gera tabela true e false
    if filtered_prod.columns == "Produto":
        with open (filename, "a", newline = "") as csvfile:  #adiciona conteudo em arquivo sem apagar
            file = csv.writer(csvfile)
            
            file.writerow(data)
            csvfile.close()

except:
    with open (filename, "w", newline = "") as csvfile: #apaga tudo e escreve
        file = csv.writer(csvfile)
        file.writerow(header)
        #file.writerow(data)
        csvfile.close()

        with open (filename, "a", newline = "") as csvfile:  #adiciona conteudo em arquivo sem apagar
            file = csv.writer(csvfile)
            
            file.writerow(data)
            csvfile.close()




'''
try:
    work.query('Produto') #gera tabela true e false
    #filtroBoolP = (filtroP[0] == True)  #saber se tem mesmo true
    nullProd = False
    print(work)
    print(nullProd)

except:
    nullProd = True
    print(nullProd)
'''

'''
with open (filename, "a", newline = "") as csvfile:  #adiciona conteudo em arquivo sem apagar
    file = csv.writer(csvfile)
    
    file.writerow(data)
    csvfile.close()
'''


