aluno = input("Qual é o nome do Aluno : \n")
n0 = float(input("AVALIAÇÃO CONTINUA : \n"))
n1 = float(input("PROVA DOS PROFESSORES : \n"))
n2 = float(input("PROVA TRIMESTRARL : \n"))

media = float((n0 + n1 +n2)  / 3)
if(media >= 10):
    print(f"A Media do {aluno} é : {media}  ")
    print("APROVADO COM SUCESSO")
    
if media <=9 and media >= 5 :
    print(f" A media do {aluno} é: {media: .2f} ")
    print("EXAME")
if media <5 :
    print(f"A media do {aluno} é {media : .2f}")
    print("REPROVADO")
    