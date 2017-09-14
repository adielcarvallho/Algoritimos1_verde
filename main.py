vprint("="*19 + "\n> SEJA BEM-VINDO! <\n" + "="*19 + "\n \n")

user1 = {"acesso": 1, "usuario": "root", "senha": "root"}
user2 = {"acesso": 2, "usuario": "root2", "senha": "root2"}
user3 = {"acesso": 3, "usuario": "root3", "senha": "root3"}

users = []
users.append(user1)
users.append(user2)
users.append(user3)

logado = False

while logado != True:
  print(">>>          LOGIN          <<<")
  print("(1)-ALUNO    (2)-PROF   (3)-ADM")
  nivel = int(input("SEU PERFIL:"))
  user = str(input("USUÁRIO:"))
  senha = str(input("SENHA:"))

  for x in users:
    if(nivel == x["acesso"] and user == x["usuario"] and senha == x["senha"]):
      print("LOGADO")
      logado = True
      print("\n")
      break
    else:
      continue
      print("NÃO LOGADO")
      logado = False
      print("\n")
      
    
if(logado == True):
  menu = ["CADASTRAR PROFESSOR", "CADASTRAR TURMA", "CADASTRAR ALUNO", "CADASTRAR AVALIAÇÃO", "LANÇAR NOTA", "VER BOLETIM"]
  
  for indice, valor in enumerate(menu):
    print(indice,valor)
  
  opcao = int(input("\nEscolha uma opção de menu: "))
  
  if(nivel == 1 and opcao == 5):
    print("OK")
  elif (nivel == 2  and (opcao == 3 or opcao == 4 or opcao == 5)):
    print("OK")
  elif (nivel == 3 and opcao <= 5):
    print("OK")
  else:
    print("NÃO PERMITIDO")
