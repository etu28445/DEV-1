text = input("Entrer message ici : ")

d = 0
for a in text:
    if a == "e":
        d += 1
        message = "il y a " + str(d) + " e"
print(message)
''' print("Adrieeeen".count("e"))'''