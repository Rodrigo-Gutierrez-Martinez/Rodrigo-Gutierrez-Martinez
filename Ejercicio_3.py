print("Dame la temperatura")
temp=float(input())
print("La temeperatura esta en celcius o Fahrenheit")
tipo=input()
if tipo=="celsius":
    print("Convirtiendo temperatura a Fahrenheit")
    conv=(temp*9/5)+32
    print(f"La conversion a {tipo} es {conv}")
elif tipo=="Fahrenheit":
    print("Convirtiendo temperatura a Celsius")
    conv=(temp-32)*5/9
    print(f"La conversion {tipo} es {conv}")
else:
    print("Ese tipo de conversion no es valida")

