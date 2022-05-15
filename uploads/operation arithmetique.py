i=0
while i < 10:
    a=input("donnez valeur a: ")
    b=input("donnez valeur b: ")
    s=float(a)+float(b)
    p=float(a)*float(b)
    so=float(a)-float(b)
    d=float(a)/float(b)
    m=float(a)//float(b)
    pu=float(a)**float(b)
    print("Les Operation Arithmetiques")
    print("Somme de",a,"+",b,"=", s)
    print("Produit de",a,"*",b,"=", p)
    print("Soustraction de",a,"-",b,"=", so)
    print("Division de",a,"/",b,"=", d)
    print("[] de",a,"//",b,"=", m)
    print("Puissance de",a,"**",b,"=", pu)
    while True:
        inp = input("If you want to calulate again, type yes: ")
        if inp != "yes":
            i+=11
        break