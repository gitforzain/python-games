from random import choice

def counter():
   
    with open("Mchine_Errors/files1.txt", "r") as onc_pro:
        contio = onc_pro.read()
    
    with open("Mchine_Errors/files2.txt", "r") as oni_prp:
        contero = oni_prp.read()
    
    with open("Mchine_Errors/files3.txt", "r") as ona_pro:
        cnoeto = ona_pro.read()

    with open("Mchine_Errors/files4.txt", "r") as onai_pro:
        contro = onai_pro.read()

    with open("Mchine_Errors/files5.txt", "r") as ono_pro:
        conuio = ono_pro.read()
    

    choice_pip = choice([contio, contero, cnoeto, contro , contio , conuio])
    return choice_pip

outer = counter()
print(outer)