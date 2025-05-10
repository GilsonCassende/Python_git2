conj1 = {1,2,3,4}
conj2 = {3,4,5,6}

print("O conjunto 1 é ",conj1)
print("O conjunto 2 é ",conj2)

uniao = conj1.union(conj2)
defer = conj1.difference(conj2)
interc = conj1.intersection(conj2)

print("A união do conjunto é : ",uniao)
print("A diferença do conjunto é : ",defer)
print("A intercessão do conjunto é : ",interc)

