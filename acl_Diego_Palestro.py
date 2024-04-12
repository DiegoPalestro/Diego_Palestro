ACL=int(input("Ingrese el número de ACL: "))
if ACL >= 1 and ACL <=99:
    print("Esta ACL es una ACL estándar")
elif ACL >= 100 and ACL <=199:
    print("Esta ACL es una ACL extendida")
else:
    print("Número de ACL fuera de rango")