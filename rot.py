import os
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def rot(s,toggle):
    i = 0
    s = list(s)

    while i < len(s):
        
        if toggle == 0:
            if(ord(s[i]) + 13) > 126:
                s[i] = chr((ord(s[i]) + 13) - 95)
            else:
                s[i] = chr(ord(s[i]) + 13)

            toggle = 1

        elif toggle == 1:
            if(ord(s[i]) - 13) < 32:
                s[i] = chr((ord(s[i]) - 13) + 95)
            else:
                s[i] = chr(ord(s[i]) - 13)

            toggle = 0

        i += 1
    return ''.join(s)



op = input("\t\tMenu\n\t2.Introduzir.\n\t1.Pesquisar\n\t0.Sair\n\tOpção: ") 
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

while op != "0":
    
    if op == "2":
        p = input("Introduz a plataforma: ")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        s = input("Introduz a pass: ")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        

        file = open(ROOT_DIR + "/store.txt","a")

        os.system( "attrib +h " + ROOT_DIR + "/store.txt")

        L = [p, "\n", rot(s,0),"\n\n"]
        file.writelines(L)

        file.close()

        print("Introduzido com sucesso!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif op == "1":
        p = input("Introduz a plataforma: ")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        file = open(ROOT_DIR + "/store.txt","r")

        os.system( "attrib +h " + ROOT_DIR + "/store.txt")

        line = file.readline()
        found = False
        while line:
            if line == (p + "\n"):
                print("Plataforma: " + line + "Pass: "+ rot(file.readline(), 1)[:-1] + "\n")
                found = True
                break
            line = file.readline()
        
        if found == False:
            print("Não encontrado, tente novamente...\n")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            cont = input("Clique qualquer tecla para continuar...")
            cont = None
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Opção inválida!\n")

    op = input("\t\tMenu\n\t2.Introduzir.\n\t1.Pesquisar\n\t0.Sair\n\tOpção: ") 
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')

