SW1NativeVLAN=99
SW1NativeVLANrequerida=99
SW1VLAN=[10,20,30]
SW1VLANrequeridas=[10,100,30]
SW2NativeVLAN=200
SW2NativeVLANrequerida=99
SW2VLAN=[40,50,60]
SW2VLANrequeridas=[40,50,60]

print("¿Es la VLAN 99 la VLAN nativa del switch 1?")
if SW1NativeVLAN==SW1NativeVLANrequerida:
    print("La VLAN es igual y cumple con el requerimiento")
else:
    print("La VLAN es diferente y no cumple con el requerimiento")
print("")

print("¿Las VLAN 10, 100 y 30 forman parte del switch 1?")
if SW1VLAN==SW1VLANrequeridas:
    print("Las VLAN son iguales y cumplen con el requerimiento")
else:
    print("Las VLAN son diferentes y no cumplen con el requerimiento")
print("")

print("¿Es la VLAN 99 la VLAN nativa del switch 2?")
if SW2NativeVLAN==SW2NativeVLANrequerida:
    print("La VLAN es igual y cumple con el requerimiento")
else:
    print("La VLAN es diferente y no cumple con el requerimiento")
print("")

print("¿Las VLAN 40, 50 y 60 forman parte del switch 2?")
if SW2VLAN==SW2VLANrequeridas:
    print("Las VLAN son iguales y cumplen con el requerimiento")
else:
    print("Las VLAN son diferentes y no cumplen con el requerimiento")
print("")