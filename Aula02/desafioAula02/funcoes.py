def mediaLista(lista):    
    #Lista VAzia Retorna 0    
    if not lista:        
        return 0    
    #Soma os valores da lista e divide pela quantidade    
    return sum(lista) / len(lista)

def listaSubritaiMedia(lista):    
    if not lista:        
        return 0    
    
    media = mediaLista(lista)    
    desvios = []    
    
    #Percorre a lista subtrai a media e adicona em desvios que o valor de Xi - Media X    
    for x in lista:        
        desvios.append(x - media)    
    
    #Retorna a lista     
    return desvios



