#aqui é onde sera efetuado o cadastro dos professores
#sempre que cadastro for False continuara fazendo o cadastro dos professores!
professor = []
  
cadastro = False
while not cadastro:
    
    flag1 = False
    while not flag1:
      nome = input('Digite o nome completo do professor:')
      if(len(nome) < 6 or len(nome) > 30):
        print('ERRO: O nome do professor deve ser de 5 a 15 caracteres')
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
    decisao = input('Deseja cadastrar outro professor? [S/N]')
    if(decisao =='N' or decisao == 'n'):
      cadastro = True

    
