aluno = input("Qual é o nome do Aluno : \n")
n0 = float(input("AVALIAÇÃO CONTINUA : \n"))
n1 = float(input("PROVA DOS PROFESSORES : \n"))
n2 = float(input("PROVA TRIMESTRARL : \n"))

media = float((n0 + n1 +n2)  / 3)

print(f"A Media do {aluno} é : {media}")