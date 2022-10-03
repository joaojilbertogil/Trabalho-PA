def inicio():
    print('-' * 49)
    print('------------Bem Vindo a Brunão Lanches-----------')
    print('-' * 49)
    print('')
  
usuario = ''
senha = ''


def cadastrar():
    global usuario
    global senha
    usuario = input("Crie seu usuário: ")
    senha = input("Crie sua senha: ")
    print('-' * 30)

def menu():
    print('\n')
    print('-' * 46)
    print('-----------MENU-----------')
    print('-' * 46)
    print('')
    print("Seu Usuário Atual é: " + usuario) 
    print("Sua Senha Atual é: " + senha)
    print("Para Editar o Usuario digite (1)")
    print("Para Editar a Senha digite (2)")
    print("Para Excluir Usuario e Senha digite (3)")
    print("Para Sair do Sistema digite (4)")
    print("Para entrar na parte dos Clientes digite(5)")
    print("Para entrar na Parte do Estoque digite(6)")
    acao()

def excluir():
    global usuario
    global senha
    usuario = ''
    senha = ''

def alterarSenha():
    global senha
    senha = input("Digite sua nova senha: ")

def alterarUsuario():
    global usuario
    usuario = input("Digite seu novo usuario: ")

matriz = []
i = 0

def verificarIng():
    if matriz == []:
        print("Adicione um ingrediente.")
        addIng()
    
def menuIng():
    print('-' * 26)
    print("Adicionar Ingredientes(1)")
    print("Excluir Ingredientes(2)")
    print("Atualizar Ingredientes(3)")
    print("Ver Ingredientes(4)")
    print("Voltar(5)")
    print('-' * 26)
    acao = input("Digite o que deseja fazer:")
    if acao == '1':
        addIng()
    elif acao == '2':
        excluirIng()
    elif acao == '3':
        atualizarIng()
    elif acao == '4':
        mostrar()
    elif acao == '5':
        menu()
    else:
        acao = input("Ocorreu um erro, deseja voltar ao menu central?")
        print("1- Sim" + "\n" + "2- Não")
        if acao == '1':
            menu()
        elif acao == '2':
            menuIng()
        
def apenasMostrar():
    print('-' * 40)
    print("Ingredientes.")
    j = 0
    for x in matriz:
        print(j, "-",''.join(map(str,matriz[j])))
        j = j + 1

def mostrar():
    print('-' * 40)
    print("Ingredientes.")
    j = 0
    for x in matriz:
        print(j, "-",''.join(map(str,matriz[j])))
        j = j + 1
    menuIng()

def addIng():
    for colunas in range(1):
            linhas = []
            for valor in range(0, 1, 1):
                global i
                ing = input("Digite o Ingrediente: ")
                qnt = input("Quantidade: ")
                    
                linhas.insert(valor, [ing, qnt])
                i = i+1
                break
            matriz.append(linhas)
            print("Matriz Atual." + "\n")
            mostrar()

def excluirIng():
    global matriz
    tam = len(matriz) - 1
    ex = int(input("Qual linha deseja excluir?:"))
    print("(Se deseja voltar, digite um número maior do que", tam, ")")
    if ex <= tam:
        matriz.remove(matriz[ex])
        print("Concluído")
        mostrar()
    else:
        print("1- Central" + "\n" + "2-Ingredientes")
        acao = input("Ocorreu um erro, deseja voltar para qual menu?")
        if acao == '1':
            menu()
        else:
            excluirIng()

def atualizarIng():
    apenasMostrar()
    ex = int(input("\n"+"Qual linha deseja atualizar?: "))
    if ex < len(matriz):
        print("Ocorreu um erro.")
        menuIng()
    for i in matriz:
        if matriz[ex] == i:
            for colunas in range(1):
                linhas = []
                for valor in range(0, 1, 1):
                    ing = input("Digite o Ingrediente: ")
                    qnt = input("Quantidade: ")
                
                    linhas.insert(valor,[ing, qnt])
                    break
                matriz[ex] = linhas
                apenasMostrar()
                menuIng()

def acao(): 
    acao = input("Digite o número do deseja fazer: ")

    if acao == '1':
        print("Digite seu novo Usuário.")
        alterarUsuario()
        print("Seu usuário atual é: " + usuario)
        menu()
    elif acao == '2':
        print("Digite sua nova senha.")
        alterarSenha()
        print("Sua senha atual é: "+ senha)
        menu()
    elif acao == '3':
        excluir()
        print("Seu usuario foi excluido")
        cadastrar()
        menu()
    elif acao == '4':
        inicio()
    elif acao == '5':
        print("Ainda há os clientes")
        #clientola
    elif acao == '6':
        verificarIng()()
    else:
        print("Ocorreu um Erro, digite novamente.")
        acao()

def login():
    teste = bool(False) 
    teste2 = bool(False)
    print('-' * 30)
    print("Vamos Fazer o Login")
    usuarioLocal = input("Usuário: ")
    senhaLocal = input("Senha: ")
    if usuarioLocal == usuario:
        teste = True
    else:
        teste = False
        print("Seu Usuário está incorreto")
    if senhaLocal == senha:
        teste2 = True
    else:
        teste2 = False
        print("Sua Senha está incorreta")

    if teste2 and teste == True:
        print("Login feito com sucesso!")
        menu()
    else:
        print("Ocorreu um erro")
        login()

#Área dos clientes - thur

inicio()
cadastrar()
login()