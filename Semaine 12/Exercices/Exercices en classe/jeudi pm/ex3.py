message = input("Message : ")

# 3 des solutions possibles
if "@" in message:
    print("Signal spécial détecté !")

if message.count("@") > 0:
    print("Signal spécial détecté !")

if message.find("@") != -1:
    print("Signal spécial détecté !")

