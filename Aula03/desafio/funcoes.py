def acuracia(tp,fp,fn,tn):

    return (tp + tn) / (tp + fp + tn + fn)

def precisao(tp, fp):
    
    return (tp / (tp + fp))

def recall(tp, fn):
 
    return (tp / (tp + fn))

def f1Score(precisao, recall):

    return 2 * ((precisao*recall) / (precisao+recall))


def principal(tp, fp, tn, fn):
    print(tp)
    print(fp)
    print(tn)
    print(fn)
    acu = acuracia(tp, fp, tn, fn)
    print(acu)

    preci = precisao(tp, fp)
    print(preci)

    rec = recall(tp, fn)
    print(rec)
    
    f1 = f1Score( preci, rec)
    print(f1)

    print('Resultado')
    print(f1)
