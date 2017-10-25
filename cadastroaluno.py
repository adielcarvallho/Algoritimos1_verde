#aqui é onde sera efetuado o cadastro dos alunos
#sempre que cadastro for False continuara fazendo o cadastro dos alunos!
aluno1 = []
  
alunocadastro = False
while not alunocadastro:
    
    flag1 = False
    while not flag1:
      nome = input('Digite o nome completo do aluno:')
      if(len(nome) < 6 or len(nome) > 30):
        print('ERRO: O nome do aluno deve ser de 5 a 15 caracteres')
      else:
        flag1 = True
    print()
    
    flag1 = False
    while not flag1:
      data = input('Informe a data de nascimento do aluno:')
      if(len(data) < 6 or len(nome) > 8):
        print('ERRO: A data de nascimento deve conter  de 6 a 8 caracteres')
      else:
        flag1 = True
    print()
    
    flag1 = False
    while not flag1:
      login = input('Informe o login de acesso:')
      if(len(login) < 5 or len(login) > 15):
        print('ERRO: O "login" deve ser de 5 a 15 caracteres')
      else:
        flag1 = True
    print()
        
    flag1 = False
    while not flag1:
      senha = str(input('Informe a senha de acesso:'))
      senha1 = str(input('Informe a senha novamente:'))
      if(senha != senha1):
        print('ERRO: As senhas devem ser iguais')
      else:
        flag1 = True
    print()
  
    Email = input('Informe o Email para efetuar o cadastro: ')
    print()
   
    print('Cadastro efetuado com sucesso')
    decisao = input('Deseja cadastrar outro aluno? [S/N]')
    if(decisao =='N' or decisao == 'n'):
      cadastro = True

    
