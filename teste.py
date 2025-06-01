from time import sleep 
def dic():
    n = input("Olá com te chamas ? : ")
    return n

def boas(n):
    print(f"Olá {n} seje bem-vindo(a)")

def menu():
    print("======Sistema GFC====== \n ")
    sleep(5)
    nome = dic()
    boas(nome)



if __name__=="__main__":
    menu()



