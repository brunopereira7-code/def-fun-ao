import os 
os.system("cls")
import time

def limpa_tela():
    time.sleep(3)
    os.system("cls") 

def calcular_media(n1,n2):
    calcular=(n1+n2) / 2
    return calcular

    # return n1+n2
    #calcular=n1+n2
    #return calcular

def mostrar_resultado(media):
    print(f"Resultado:{media}") 
    if media >=7:
        print(f"Aprovado")
    else:
        print(f"Reprovado")


#codigo principal 
#funçao sem retorno
limpa_tela() 

primeiro_numero=int(input("Digite seu primeiro numero")) 
segundo_numero=int(input("Digite seu segundo numero")) 

#funçao com parametro e com retorno
media=calcular_media(primeiro_numero,segundo_numero)
#funçao com parametro e sem retorno
mostrar_resultado(media)
