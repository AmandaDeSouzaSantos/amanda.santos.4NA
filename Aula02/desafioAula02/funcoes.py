def mediaLista(lista):    
    #Soma os valores da lista e divide pela quantidade    
    return sum(lista) / len(lista)

def listaSubritaiMedia(lista):    
   
    media = mediaLista(lista)    
    desvios = []    
    
    #Percorre a lista subtrai a media e adicona em desvios que o valor de Xi - Media X    
    for x in lista:        
        desvios.append(x - media)    
    
    #Retorna a lista     
    return desvios

#Calcula media lista
def mediaLista(lista):
    #Soma os valores da lista e divide pela quantidade e retorna
    return sum(lista) / len(lista)

# Calcula desvios Xi - media
def calculaDesvio(lista):
    #Usa funcao media
    media = mediaLista(lista)

    #Cria lista para guardar desvios
    desvios = []
    #Percorre a lista subtrai a media e adiciona em desvios
    for x in lista:
        desvios.append(x - media)

    #Retorna a lista
    return desvios

#Pega as listas dos desvios X * desvios Y
def calculaDesviosXPorDesviosY(desviox, desvioy):
    #Lista para guardar resultado
    desviosMultiplicados = []
    #Percorre ambas as listas e multiplica os valores correspondentes em cada indice
    #range utiliza o tamanho de uma das listas como referência
    #gerando a sequência de indices correta
    for i in range(len(desvioy)):
        desviosMultiplicados.append(desvioy[i] * desviox[i])
    return desviosMultiplicados

# Eleva desvios de X ao quadrado
def desvioXEleva2(desviox):
    desviosXQuadrado = []
    for x in desviox:
        desviosXQuadrado.append(x ** 2)
    return desviosXQuadrado

#Calcula B1
def calculaB1(desviosMultiplicados, desviosXQuadrado):
    return sum(desviosMultiplicados) / sum(desviosXQuadrado)

#Calcula B0
def calculaB0(b1, mediax, mediay):
    #O B0 e a media y - b1 * media x
    return mediay - (b1 * mediax)

#Funcao principal para nao ficar um monte de import no main
def calculaRegressaoLinear(x, y):
    print("\nRegressão Linear\n")
    
    mediax = mediaLista(x)
    mediay = mediaLista(y)
    print(f"Media X: {mediax}")
    print(f"Media Y: {mediay}")

    desviox = calculaDesvio(x)
    desvioy = calculaDesvio(y)
    print(f"Desvios X: {desviox}")
    print(f"Desvios Y: {desvioy}")

    desviosMultiplicados = calculaDesviosXPorDesviosY(desviox, desvioy)
    print(f"Desvios X * Desvios Y: {desviosMultiplicados}")

    desviosXQuadrado = desvioXEleva2(desviox)
    print(f"Desvios de X ao quadrado: {desviosXQuadrado}")

    b1 = calculaB1(desviosMultiplicados, desviosXQuadrado)
    print(f"B1 calculado: {b1}")

    b0 = calculaB0(b1, mediax, mediay)
    print(f"B0 calculado: {b0}")

    return b0, b1





