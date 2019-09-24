t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
t3 = []

a = 0
while a < len(t1):
    t3.append(t2[a])
    t3.append(t1[a])
    a+=1

print(t3)