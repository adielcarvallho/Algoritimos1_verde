# FUNÇÕES 
    
def login():
  logado = False
  
  user1 = {"acesso": 1, "usuario": "root", "senha": "root"}
  user2 = {"acesso": 2, "usuario": "root2", "senha": "root2"}
  user3 = {"acesso": 3, "usuario": "root3", "senha": "root3"}

  users = []
  users.append(user1)
  users.append(user2)
  users.append(user3)
  
  print(">>>                  LOGIN                 <<<")
  print("(1)-ALUNO    (2)-PROFESSOR   (3)-ADMINISTRADOR")
  print()
  nivel = int(input("SEU PERFIL:"))
  user = str(input("USUÁRIO:"))
  senha = str(input("SENHA:"))
  
  if(not(nivel <= 0) and not(nivel >= 4)):
    for x in users:
      if(nivel == x["acesso"] and user == x["usuario"] and senha == x["senha"]):
        print("LOGADO")
        logado = True
        print("\n")
        break
      else:
        if (x["acesso"] >= 3): # so mostra a mensagem caso todo o dicionario tenha sido percorrido
          print("NÃO LOGADO")
      
  else:
    print("Nível de acesso inválido!")
  
  
  return (logado, nivel)
  
def Menu(perfilEscolhido):
  if(perfilEscolhido == 1):
    menu = ["VER BOLETIM", "SAIR"]
  elif (perfilEscolhido == 2):
    menu = ["CADASTRAR AVALIAÇÃO","LANÇAR NOTA", "VER BOLETIM", "SAIR"]
  else:
    menu = ["CADASTRAR PROFESSOR", "CADASTRAR TURMA", "CADASTRAR ALUNO", "CADASTRAR AVALIAÇÃO", "LANÇAR NOTA", "VER BOLETIM", "SAIR"]
    
  return menu
  
# SISTEMA

print("="*19 + "\n> SEJA BEM-VINDO! <\n" + "="*19 + "\n \n")

validado = False
perfil = 0

# ENQUANTO VALIDADO FOR FALSO CONTINUA PEDINDO AS INFORMAÇÕES DE LOGIN
while not validado:
  # FUNÇÃO login RETORNA VALORES PARA AS VARIAVEIS
  (validado, perfil) = login() 
  # SE O USUARIO FOR VALIDADO MOSTRA O MENU
  if(validado == True):
    for indice, valor in enumerate(Menu(perfil)):
      print(indice+1, valor)
    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))
    if((perfil == 1 and op == 2) or (perfil == 2 and op == 4) or (perfil == 3 and op == 7)):
      print("TCHAU!!!")
