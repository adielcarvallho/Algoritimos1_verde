# FUNÇÕES 

# FUNÇAO PARA FAZER LOGIN NO SISTEMA
def login(users):
  logado = False

  while not logado:  
    print(">>>                  LOGIN                 <<<")
    print("(1)-ALUNO    (2)-PROFESSOR   (3)-ADMINISTRADOR")
    print()
    nivel = int(input("SEU PERFIL: "))
    user = str(input("USUÁRIO: "))
    senha = str(input("SENHA: "))
    contador = 0
    
    if(not(nivel <= 0) and not(nivel >= 4)):
      for x in users:
        contador += 1
        if(nivel == x["acesso"] and user == x["usuario"] and senha == x["senha"]):
          logado = True
          break
        else:
          if (contador == len(users)): # so mostra a mensagem caso todo o dicionario tenha sido percorrido
            print("Usuário ou senha inválido!\n")
        
    else:
      print("Nível de acesso inválido!\n")
    
  return nivel

# FUNCAO PARA MONTAR O MENU  
def Menu(perfilEscolhido):
  print("\n>>>MENU PRINCIPAL<<<\n")
  if(perfilEscolhido == 1):
    menu = ["VER BOLETIM", "SAIR"]
  elif (perfilEscolhido == 2):
    menu = ["CADASTRAR AVALIAÇÃO","LANÇAR NOTA", "VER BOLETIM", "SAIR"]
  else:
    menu = ["CADASTRAR PROFESSOR", "CADASTRAR TURMA", "CADASTRAR ALUNO", "CADASTRAR AVALIAÇÃO", "LANÇAR NOTA", "VER BOLETIM", "SAIR"]
    
  return menu

# FUNÇAO PARA CRIAR ALUNOS
def CadastrarAluno(turma,users):
  aluno = {}
  usuarioAluno = {}
  #aqui é onde sera efetuado o cadastro dos alunos
  #sempre que cadastro for False continuara fazendo o cadastro dos alunos!

  print('\n>>>CADASTRO DE ALUNOS<<<\n')
#  cadastro = False
#  while not cadastro:
      
  flag1 = False
  while not flag1:
    nome = input('Digite o nome completo do aluno: ')
    if(len(nome) < 6 or len(nome) > 30):
      print('ERRO: O nome do aluno deve ser de 5 a 15 caracteres')
    else:
      flag1 = True
  
  data = input('Informe a data de nascimento do aluno: ')
  
  login = input('Informe o login de acesso: ')

  # VERIFICA SE JA EXISTE O USUARIO
  # PQP QUE DESGRAÇA D FAZE
  duplicado = False
  while not duplicado:
    for x, y in enumerate(users):
      if(users[x]["usuario"] == login):
         print("Esse usuário ja está sendo utilizado, escolha outro.")
         login = input('Informe o login de acesso novamente: ')
         break
      else:
         if(x+1 == len(users)):
           duplicado = True

  # VERIFICA SE AMBAS AS SENHAS SÃO IGUAIS
  flag1 = False
  while not flag1:
    senha = str(input('Informe a senha de acesso: '))
    senha1 = str(input('Informe a senha novamente: '))
    if(senha != senha1):
      print('ERRO: As senhas devem ser iguais.')
    else:
      flag1 = True

  email = input('Informe o e-mail para efetuar o cadastro: ')

  print('\nLISTA DE TURMAS')
  for indice, valor in enumerate(turma):
    print("     ", indice+1, valor["nome"])

  escolha = False
  # PEDE AO USUARIO QUE ESCOLHA UMA TURMA PARA VINCULAR A UM ALUNO
  while not escolha:
    op = int(input('Informe uma turma para o aluno: '))
    if(not(op <= 0) and not(op > len(turma))):
      aluno = {"login": login, "senha": senha, "nome": nome, "email": email, "data": data, "turma": turma[op-1]["nome"]}
      usuarioAluno = {"acesso": 1, "usuario": login, "senha": senha}
      escolha = True
    else:
      print('Escolha uma opção válida!')
  
  
  
  
  print('\nCadastro efetuado com sucesso!')
  '''
  decisao = input('Deseja cadastrar outro aluno [S/N]? ')
  if(decisao =='N' or decisao == 'n'):
    cadastro = True
    '''

  return (aluno, usuarioAluno)

# CADASTRO DE PROFESSORES
def CadastrarProfessor(users):
  print('\n>>>CADASTRO DE PROFESSOR<<<\n')
#cadastro = False
#while not cadastro:
  flag1 = False
  while not flag1:
    nome = input('Digite o nome completo do professor: ')
    if(len(nome) <= 4 or len(nome) > 30):
      print('ERRO: O nome do professor deve ser de 5 a 15 caracteres')
    else:
      flag1 = True
      
  login = input('Informe o login de acesso: ')

  # VERIFICA SE JA EXISTE O USUARIO
  duplicado = False
  while not duplicado:
    for x, y in enumerate(users):
      if(users[x]["usuario"] == login):
         print("Esse usuário ja está sendo utilizado, escolha outro.")
         login = input('Informe o login de acesso novamente: ')
         break
      else:
         if(x+1 == len(users)):
           duplicado = True
      
  flag1 = False
  while not flag1:
    senha = str(input('Informe a senha de acesso: '))
    senha1 = str(input('Informe a senha novamente: '))
    if(senha != senha1):
      print('ERRO: As senhas devem ser iguais.')
    else:
      flag1 = True

  email = input('Informe o e-mail para efetuar o cadastro: ')
  professor = {"login": login, "senha": senha, "nome": nome, "email": email}
  usuarioProf = {"acesso": 2, "usuario": login, "senha": senha}
 
  print('\nCadastro efetuado com sucesso!')
  '''
  decisao = input('Deseja cadastrar outro professor [S/N]? ')
  if(decisao =='N' or decisao == 'n'):
    cadastro = True
    '''
      
  return (professor, usuarioProf)

# CADASTRAR TURMAS VINCULANDO PROFESSOR
def CadastrarTurmas(professores):
  print('\n>>>CADASTRO DE TURMAS<<<\n')
  nome = str(input('Informe o nome da turma: '))
  print('\nLISTA DE PROFESSORES')
  for indice, valor in enumerate(professores):
    print("     ", indice+1, valor["nome"])

  escolha = False
  while not escolha:
    op = int(input('Informe o professor responsável: '))
    if(not(op <= 0) and not(op > len(professores))):
      turma = {"nome": nome, "reponsavel": professores[op-1]["nome"]}
      escolha = True
    else:
      print('Escolha uma opção válida!')

  print('\nCadastro efetuado com sucesso!')
  
  return turma

def CadastrarAvaliacao():
 # cadastroavaliacao = False
 #while not cadastroavaliacao:
  print('\n>>>CADASTRO DE AVALIAÇÃO<<<\n')
  disciplina = input ("Qual disciplina séra aplicada a avaliação? ")
  data =input("Qual a data da avaliação? ")
  valor =input("Qual será o valor da avaliação? ")
  descricao =input("Descrição: ")

  print ("\nAvaliação cadastrada.")
  '''
  sair = input ("Deseja cadastra outra avaliação [S/N]? ")
  if (sair== 'N' or sair == 'n'):
    cadastroavaliacao = True
  '''
  
  avaliacao = {"disciplina": disciplina, "data": data, "valor": valor, "descricao": descricao}

  return avaliacao
  
# SISTEMA

import os

# VARIAVES DOS DADOS PRINCIPAIS DO SISTEMA usuarios, alunos, professores, alunos, avaliacoes, turmas
usuarios = []
alunos = []
professor = []
turmas = []
avaliacao = []

# CRIAÇAO DO USUARIO ADMINISTRADOR
user = {"acesso": 3, "usuario": "adm", "senha": "adm"}
usuarios.append(user)

print("="*19 + "\n> SEJA BEM-VINDO! <\n" + "="*19 + "\n \n")

validado = False
perfil = 0

# ENQUANTO VALIDADO FOR FALSO CONTINUA PEDINDO AS INFORMAÇÕES DE LOGIN
while not validado:
  # FUNÇÃO login RETORNA VALORES PARA AS VARIAVEIS
  perfil = login(usuarios) 
  # SE O USUARIO FOR VALIDADO MOSTRA O MENU
  
  ativo = True

  while ativo:
    for indice, valor in enumerate(Menu(perfil)):
      print(indice+1, valor)
    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    obj = []

    # ADMIN CADASTRA PROFESSOR
    if(perfil == 3 and op == 1):
      (obj, user) = CadastrarProfessor(usuarios)
      professor.append(obj)
      usuarios.append(user)
    elif(perfil == 3 and op == 2):
      # ADMIN CADASTRA TURMA
      if(not professor == []):
        obj = CadastrarTurmas(professor)
        turmas.append(obj)
      else:
        print('Não existe professor cadastrado para poder vincular uma turma a ele.')
    elif(perfil == 3 and op == 3):
      # ADMIN CADASTRA ALUNO
      if(not turmas == []):
        (obj, user) = CadastrarAluno(turmas, usuarios)
        alunos.append(obj)
        usuarios.append(user)
      else:
        print('Não existe turma cadastrada para poder vincular um aluno a ela.')
    elif(perfil == 2 and op == 1):
      # PROFESSOR CADASTRA AVALIAÇÃO
      obj = CadastrarAvaliacao()
      avaliacao.append(obj)
      print(avaliacao)
    elif((perfil == 1 and op == 2) or (perfil == 2 and op == 4) or (perfil == 3 and op == 7)):
      # SAIR
      print("TCHAU!!!\n")
      ativo = False
    else:
      print('Você não possui acesso a esse módulo do sistema.')     
