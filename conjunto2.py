g1 = {"Carlos", "Josiel", "Jandira", "Aline"}
g2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

print("O primeiro gruppo é composto por : ",g1)
print("O segundo grupo é composto por : ",g2)

pr_em_1g = g1 ^ g2

uniao = g1.union(g2)
print("Conjuntos dos membros que  pertencem num só grupo : ",pr_em_1g)
print("Todos Membros dos grupos sem repetir ninguem :",uniao)