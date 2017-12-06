# FUNÇÕES 

# FUNÇAO PARA FAZER LOGIN NO SISTEMA
def Login():
  logado = False

  while not logado:  
    print(">>>                  LOGIN                 <<<")
    print("(1)-ALUNO    (2)-PROFESSOR   (3)-ADMINISTRADOR")
    print()
    nivel = int(input("SEU PERFIL: "))
    user = str(input("USUÁRIO: "))
    senha = str(input("SENHA: "))

    cursor.execute(''' SELECT * FROM usuarios ''')
    rs = cursor.fetchall()
    
    if(not(nivel <= 0) and not(nivel >= 4)):
      if(nivel == 3 and user == "adm" and senha == "adm"):
        logado = True
      else:
        for x in rs:
          if(nivel == x[3] and user == x[1] and senha == x[2]):
            logado = True
            break
          else:
            print("Usuário ou senha inválido!\n")
        
    else:
      print("Nível de acesso inválido!\n")

  os.system('cls')
  return nivel

# FUNCAO PARA MONTAR O MENU  
def Menu(perfilEscolhido):
  print("\n>>>MENU PRINCIPAL<<<\n")
  if(perfilEscolhido == 1):
    menu = ["VER BOLETIM", "SAIR"]
  elif (perfilEscolhido == 2):
    menu = ["GERENCIAR AVALIAÇÃO","LANÇAR NOTA", "VER BOLETIM", "SAIR"]
  else:
    menu = ["GERENCIAR PROFESSOR", "GERENCIAR TURMA", "GERENCIAR ALUNO", "GERENCIAR AVALIAÇÃO", "LANÇAR NOTA", "VER BOLETIM", "SAIR"]
    
  return menu

# FUNÇAO PARA CRIAR ALUNOS
def CadastrarAluno():
  retornaSubMenu = False

  while not retornaSubMenu:
    print('\n>>>MÓDULO DE ALUNO<<<\n')
    subMenuTurma = ["CADASTRAR","ALTERAR", "EXCLUIR", "VINCULAR ALUNOxTURMA", "VOLTAR"]

    for indice, valor in enumerate(subMenuTurma):
      print("\t", indice+1, valor)

    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    flag1 = False
    while not flag1:
      if(op == 1):
        print('\n>>>CADASTRAR ALUNOS<<<\n')
            
        nome = input('Digite o nome completo do aluno: ')
        data = input('Informe a data de nascimento do aluno: ')
        login = input('Informe o login de acesso: ')
        
        cursor.execute(''' SELECT Usuario FROM usuarios ''')
        rs = cursor.fetchall()

        # VERIFICA SE JA EXISTE O USUARIO
        if rs:
          duplicado = False
          while not duplicado:
            for x, y in enumerate(rs):
              if(y[0] == login):
                 print("Esse usuário ja está sendo utilizado, escolha outro.")
                 login = input('Informe o login de acesso novamente: ')
                 break
              else:
                if(x+1 == len(rs)):
                   duplicado = True
                 
        # VERIFICA SE AMBAS AS SENHAS SÃO IGUAIS
        flag = False
        while not flag:
          senha = str(input('Informe a senha de acesso: '))
          senha1 = str(input('Informe a senha novamente: '))
          if(senha != senha1):
            print('\nERRO: As senhas devem ser iguais.')
          else:
            flag = True

        email = input('Informe o e-mail para efetuar o cadastro: ')

        cursor.execute(''' INSERT INTO alunos (NomeAluno, DataNascimento, Email, Usuario) VALUES (?,?,?,?) ''',(nome, data, email, login,))
        cursor.execute(''' INSERT INTO usuarios (Usuario, Senha, Acesso) VALUES (?,?,?) ''',(login, senha, 1,))
        conexao.commit()

        print('\nCadastro efetuado com sucesso!')
        input('Pressione qualquer tecla para sair.')
        
      elif(op == 2):
        print('\n>>>ALTERAR ALUNO<<<\n')

        cursor.execute(''' SELECT * FROM alunos ''')
        rsAluno = cursor.fetchall()
      
        print('LISTA DE ALUNO(S)')
        for indice, valor in enumerate(rsAluno):
          print("\t", indice+1, valor[1], "|", valor[4])

        cod = int(input('\nEscolha o código para alterar: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsAluno))):
            nomeNovo = input('Informe o novo nome: ')
            dataNova = input('Informe a nova data de nascimento: ')
            emailNovo = input('Informe o novo email: ')
            
            decisao = input('\nDeseja alterar a senha de usuário? [S] Sim / [N] Não ')
            if(decisao == 'S' or decisao == 's'):
              cursor.execute(''' SELECT Senha FROM usuarios WHERE Usuario = ? ''', (valor[4],))
              rs = cursor.fetchall()
              
              senhaAntiga = input('Digite a senha antiga: ')

              flag0 = False
              while not flag0:
                if(senhaAntiga != rs[0][0]):
                  senhaAntiga = input('Senha inválida, digite novamente: ')
                else:
                  flag0 = True
                
              # VERIFICA SE AMBAS AS SENHAS SÃO IGUAIS
              flag1 = False
              while not flag1:
                senha = str(input('Informe a nova senha de acesso: '))
                senha1 = str(input('Informe a nova senha novamente: '))
                if(senha != senha1):
                  print('\nERRO: As senhas devem ser iguais.')
                else:
                  flag1 = True

            cursor.execute('UPDATE alunos SET NomeAluno = ?, DataNascimento = ?, Email = ? WHERE CodAluno = ?', (nomeNovo, dataNova, emailNovo, int(rsAluno[cod-1][0])))
            if(decisao == 'S' or decisao == 's'):
              cursor.execute('UPDATE usuarios SET Senha = ? WHERE Usuario = ?', (senha, valor[4]))
            conexao.commit()
            print('\nCadastro alterado com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))
      elif(op == 3):
        print('\n>>>EXCLUIR ALUNO<<<\n')

        cursor.execute(''' SELECT * FROM alunos ''')
        rsAluno = cursor.fetchall()

        print('LISTA DE ALUNO(S)')
        for indice, valor in enumerate(rsAluno):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para excluir: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsAluno))):
            cursor.execute('DELETE FROM alunos WHERE CodAluno = ?', (int(rsAluno[cod-1][0]),))
            cursor.execute('DELETE FROM alunoXturma WHERE CodAluno = ?', (int(rsAluno[cod-1][0]),))
            cursor.execute('DELETE FROM usuarios WHERE Usuario = ?', (rsAluno[cod-1][4],))
            conexao.commit()
            print('Cadastro excluído com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))

      elif(op == 4):
        print('\n>>>VINCULAR ALUNOxTURMA<<<\n')

        # LISTA ALUNOS
        cursor.execute(''' SELECT * FROM alunos ''')
        rsAluno = cursor.fetchall()
      
        print('\nLISTA DE ALUNO(S)')
        for indice, valor in enumerate(rsAluno):
          print("\t", indice+1, valor[1], "|", valor[4])
          
        # LISTA OS PROFESSORES
        cursor.execute(''' SELECT * FROM turma ''')
        rsTurma = cursor.fetchall()
      
        print('\nLISTA DE TURMA(S)')

        for indice, valor in enumerate(rsTurma):
          print("\t", indice+1, valor[1])

        escolha = False

        if(not rsAluno or not rsTurma):
          escolha = True
          print('\nNão existe dados o suficiente para realizar a operação.')
          input('Pressione qualquer tecla para sair.')

        while not escolha:
          opAluno = int(input('\nInforme o código do aluno: '))
          opTurma = int(input('Informe o código da turma: '))

          # ESTA COM BUG
          if((not(opAluno <= 0) and not(opAluno > len(rsAluno))) and ((not(opTurma <= 0) and not(opTurma > len(rsTurma))))):
            cursor.execute(''' SELECT * FROM alunoXturma WHERE CodAluno =  ? ''', (opAluno-1,))
            rs = cursor.fetchall()
            
            if(not(rs)):
              print('Esse aluno já está cadastrado em uma turma, escolha outro.')
              
            else:
              cursor.execute(''' INSERT INTO alunoXturma (CodAluno, CodTurma) VALUES (?,?) ''',(int(rsAluno[opAluno-1][0]), int(rsTurma[opTurma-1][0])),)
              conexao.commit()

              print('\nAluno vinculado com sucesso!')
              input('Pressione qualquer tecla para sair.')

              escolha = True

          else:
            print('As escolhas não são válidas!')
            
      elif(op == 5):
        retornaSubMenu = True

      else:
        print('Opção inválida!')

      flag1 = True
      os.system('cls')
    
  return

# CADASTRO DE PROFESSORES
def CadastrarProfessor():
  retornaSubMenu = False

  while not retornaSubMenu:
    print('\n>>>MÓDULO DE PROFESSOR<<<\n')
    subMenuTurma = ["CADASTRAR","ALTERAR", "EXCLUIR", "VOLTAR"]

    for indice, valor in enumerate(subMenuTurma):
      print("\t", indice+1, valor)

    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    flag1 = False
    while not flag1:
      if(op == 1):
        print('\n>>>CADASTRO DE PROFESSOR<<<\n')
        nome = input('Digite o nome completo do professor: ')
            
        login = input('Informe o login de acesso: ')

        cursor.execute(''' SELECT Usuario FROM usuarios ''')
        rs = cursor.fetchall()

        # VERIFICA SE JA EXISTE O USUARIO
        if rs:
          duplicado = False
          while not duplicado:
            for x, y in enumerate(rs):
              if(y[0] == login):
                 print("\nEsse usuário ja está sendo utilizado, escolha outro.")
                 login = input('Informe o login de acesso novamente: ')
                 break
              else:
                if(x+1 == len(rs)):
                   duplicado = True
            
        flag1 = False
        while not flag1:
          senha = str(input('Informe a senha de acesso: '))
          senha1 = str(input('Informe a senha novamente: '))
          if(senha != senha1):
            print('\nERRO: As senhas devem ser iguais.')
          else:
            flag1 = True

        email = input('Informe o e-mail para efetuar o cadastro: ')
        
        cursor.execute(''' INSERT INTO professor (NomeProfessor, Email, Usuario) VALUES (?,?,?) ''',(nome, email, login,))
        cursor.execute(''' INSERT INTO usuarios (Usuario, Senha, Acesso) VALUES (?,?,?) ''',(login, senha, 2,))
        conexao.commit()

        print('\nCadastro efetuado com sucesso!')
        input('Pressione qualquer tecla para sair.')

      elif(op == 2):
        print('\n>>>ALTERAR PROFESSOR<<<\n')

        cursor.execute(''' SELECT * FROM professor ''')
        rsProf = cursor.fetchall()
      
        print('LISTA DE PROFESSOR')
        for indice, valor in enumerate(rsProf):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para alterar: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsProf))):
            nomeNovo = input('Informe o novo nome do professor: ')
            emailNovo = input('Informe o novo email do professor: ')

            decisao = input('\nDeseja alterar a senha de usuário? [S] Sim / [N] Não ')
            if(decisao == 'S' or decisao == 's'):
              cursor.execute(''' SELECT Senha FROM usuarios WHERE Usuario = ? ''', (valor[3],))
              rs = cursor.fetchall()
              
              senhaAntiga = input('Digite a senha antiga: ')

              flag0 = False
              while not flag0:
                if(senhaAntiga != rs[0][0]):
                  senhaAntiga = input('Senha inválida, digite novamente: ')
                else:
                  flag0 = True
                
              # VERIFICA SE AMBAS AS SENHAS SÃO IGUAIS
              flag1 = False
              while not flag1:
                senha = str(input('Informe a nova senha de acesso: '))
                senha1 = str(input('Informe a nova senha novamente: '))
                if(senha != senha1):
                  print('\nERRO: As senhas devem ser iguais.')
                else:
                  flag1 = True
                  
            cursor.execute('UPDATE professor SET NomeProfessor = ?, Email = ? WHERE CodProfessor = ?',(nomeNovo, emailNovo, int(rsProf[cod-1][0])))
            if(decisao == 'S' or decisao == 's'):
              cursor.execute('UPDATE usuarios SET Senha = ? WHERE Usuario = ?', (senha, valor[3]))
            conexao.commit()

            print('\nCadastro alterado com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))
      elif(op == 3):
        print('\n>>>EXCLUIR PROFESSOR<<<\n')

        cursor.execute(''' SELECT * FROM professor ''')
        rsProf = cursor.fetchall()

        print('LISTA DE PROFESSOR')
        for indice, valor in enumerate(rsProf):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para excluir: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsProf))):
            cursor.execute('DELETE FROM professor WHERE CodProfessor = ?', (int(rsProf[cod-1][0]),))
            cursor.execute('DELETE FROM professorXturma WHERE CodProfessor = ?', (int(rsProf[cod-1][0]),))
            cursor.execute('DELETE FROM usuarios WHERE Usuario = ?', (rsProf[cod-1][3]),)
            conexao.commit()
            print('\nCadastro excluído com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))
            
      elif(op == 4):
        retornaSubMenu = True
        
      else:
        print('Escolha uma opção válida!')
        op = int(input("\nINFORME A OPÇÃO NOVAMENTE: "))

      os.system('cls')  
      flag1 = True

    # sair submenu
  
  return

# CADASTRAR TURMAS VINCULANDO PROFESSOR
def CadastrarTurmas():
  retornaSubMenu = False

  while not retornaSubMenu:
    print('\n>>>MÓDULO DE TURMAS<<<\n')
    subMenuTurma = ["CADASTRAR","ALTERAR", "EXCLUIR", "VINCULAR PROFESSORxTURMA", "VOLTAR"]

    for indice, valor in enumerate(subMenuTurma):
      print("\t", indice+1, valor)

    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    flag1 = False
    while not flag1:
      if(op == 1):
        print('\n>>>CADASTRAR TURMAS<<<\n')
        nome = str(input('Informe o nome da turma: '))
        cursor.execute(''' INSERT INTO turma (NomeTurma) VALUES (?) ''', (nome,))
        conexao.commit()
        print('\nCadastro efetuado com sucesso!')
        input('Pressione qualquer tecla para sair.')
        
      elif(op == 2):
        # ALTERAR TURMAS
        print('\n>>>ALTERAR TURMAS<<<\n')

        cursor.execute(''' SELECT * FROM turma ''')
        rsTurma = cursor.fetchall()
      
        print('LISTA DE TURMAS')
        for indice, valor in enumerate(rsTurma):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para alterar: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsTurma))):
            nomeNovo = input('Informe o novo nome da turma: ')

            cursor.execute('UPDATE turma SET NomeTurma = ? WHERE CodTurma = ?',(nomeNovo,int(rsTurma[cod-1][0])))
            conexao.commit()
            print('\nCadastro alterado com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))
          #FIM ALTERAR TURMAS
            
      elif(op == 3):
        #EXCLUIR TURMAS
        print('\n>>>EXCLUIR TURMAS<<<\n')

        cursor.execute(''' SELECT * FROM turma ''')
        rsTurma = cursor.fetchall()

        print('LISTA DE TURMAS')
        for indice, valor in enumerate(rsTurma):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para excluir: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsTurma))):
            cursor.execute('DELETE FROM turma WHERE CodTurma = ?', (int(rsTurma[cod-1][0]),))
            cursor.execute('DELETE FROM professorXturma WHERE CodTurma = ?', (int(rsTurma[cod-1][0]),))
            conexao.commit()
            print('\nCadastro excluído com sucesso!')
            input('Pressione qualquer tecla para sair.')
            flag2 = True
            
          else:
            cod = int(input('Opção inválida, escolha outra: '))
        # FIM EXCLUIR TURMAS
      elif(op == 4):
        # LISTA AS TURMAS
        cursor.execute(''' SELECT * FROM turma ''')
        rsTurma = cursor.fetchall()
      
        print('\nLISTA DE TURMAS')
        for indice, valor in enumerate(rsTurma):
          print("\t", indice+1, valor[1])
          
        # LISTA OS PROFESSORES
        cursor.execute(''' SELECT * FROM professor ''')
        rsProf = cursor.fetchall()
      
        print('\nLISTA DE PROFESSORES')

        for indice, valor in enumerate(rsProf):
          print("\t", indice+1, valor[1])

        escolha = False

        if(not rsProf or not rsTurma):
          escolha = True
          print('\nNão existe dados o suficiente para realizar a operação.')
          input('Pressione qualquer tecla para sair.')

        while not escolha:
          opProf = int(input('\nInforme o código do professor: '))
          opTurma = int(input('Informe o código da turma: '))
          
          if((not(opProf <= 0) and not(opProf > len(rsProf))) and ((not(opTurma <= 0) and not(opTurma > len(rsTurma))))):
            cursor.execute(''' INSERT INTO professorXturma (CodProfessor, CodTurma) VALUES (?,?) ''',(int(rsProf[opProf-1][0]), int(rsTurma[opTurma-1][0])),)
            conexao.commit()

            print('\nTurma vinculada com sucesso!')
            input('Pressione qualquer tecla para sair.')
            
            escolha = True
          else:
            print('As escolhas não são válidas!')
            
      elif(op == 5):
        retornaSubMenu = True
        
      else:
        print('Escolha uma opção válida!')
        op = int(input("\nINFORME A OPÇÃO NOVAMENTE: "))

      os.system('cls')  
      flag1 = True
  
  return

# CADASTRO DE AVALIAÇÃO
def CadastrarAvaliacao():
  retornaSubMenu = False

  while not retornaSubMenu:
    print('\n>>>MÓDULO DE AVALIAÇÃO<<<\n')

    subMenuAv = ["CADASTRAR","ALTERAR", "EXCLUIR", "VOLTAR"]

    for indice, valor in enumerate(subMenuAv):
      print("\t", indice+1, valor)

    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    flag1 = False
    while not flag1:
      if(op == 1):
        print('\n>>>CADASTRO DE AVALIAÇÃO<<<\n')
        disciplina = input ("Qual disciplina será aplicada a avaliação? ")
        data = input("Qual a data da avaliação? ")
        valor = input("Qual será o valor da avaliação? ")
        descricao = input("Descrição: ")
      
        cursor.execute(''' INSERT INTO avaliacao (Disciplina, Descricao, Valor, DataAplicacao) VALUES (?, ?, ?, ?) ''', (disciplina, descricao, valor, data))
        conexao.commit()

        print('\nCadastro efetuado com sucesso!')
        input('Pressione qualquer tecla para sair.')

      elif(op == 2):
        print('\n>>>ALTERAR AVALIAÇÃO<<<\n')

        cursor.execute(''' SELECT * FROM avaliacao ''')
        rsAv = cursor.fetchall()
        
        print('LISTA DE AVALIAÇÃO')
        for indice, valor in enumerate(rsAv):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para alterar: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsAv))):
            disciplina = input ("Qual disciplina será aplicada a avaliação? ")
            data = input("Qual a data da avaliação? ")
            valor = input("Qual será o valor da avaliação? ")
            descricao = input("Descrição: ")

            cursor.execute('UPDATE avaliacao SET Disciplina = ?, Descricao = ?, Valor = ?, DataAplicacao = ? WHERE CodAvaliacao = ?',(disciplina, descricao, valor, data, int(rsAv[cod-1][0])))
            conexao.commit()
            
            print('\nCadastro alterado com sucesso!')
            input('Pressione qualquer tecla para sair.')

            flag2 = True
          else:
            cod = int(input('\nOpção inválida, escolha o código novamente: '))
            
      elif(op == 3):
        print('\n>>>EXCLUIR AVALIAÇÃO<<<\n')

        cursor.execute(''' SELECT * FROM avaliacao ''')
        rsAv = cursor.fetchall()
        
        print('LISTA DE AVALIAÇÃO')
        for indice, valor in enumerate(rsAv):
          print("\t", indice+1, valor[1])

        cod = int(input('\nEscolha o código para excluir: '))

        flag2 = False
        while not flag2:
          if(not(cod <= 0) and not(cod > len(rsAv))):
            cursor.execute('DELETE FROM avaliacao WHERE CodAvaliacao = ?', (int(rsAv[cod-1][0]),))
            conexao.commit()
            
            print('\nCadastro excluído com sucesso!')
            input('Pressione qualquer tecla para sair.')

            flag2 = True
          else:
            cod = int(input('\nOpção inválida, escolha o código novamente: '))
      elif(op == 4):
        retornaSubMenu = True
        
      flag1 = True
      os.system('cls')

  return

def LancarNota():
  print('\n>>>LANÇAR NOTAS<<<\n')

  cursor.execute(''' SELECT * FROM turma ''')
  rsTurma = cursor.fetchall()
      
  print('LISTA DE TURMAS')
  for indice, valor in enumerate(rsTurma):
    print("\t", indice+1, valor[1])

  # LISTA OS PROFESSORES
  cursor.execute(''' SELECT * FROM avaliacao ''')
  rsAv = cursor.fetchall()

  print('\nLISTA DE AVALIAÇÃO')

  for indice, valor in enumerate(rsAv):
    print("\t", indice+1, valor[1])

  flag1 = False
  if(not rsAv or not rsTurma):
    flag1 = True
    print('\nNão existe dados o suficiente para realizar a operação.')
    input('Pressione qualquer tecla para sair.')

  codTurma = int(input('\nInforme o código da turma: '))
  codAv = int(input('Informe o código da avaliação: '))

  flag1 = False
  while not flag1:
    if((not(codTurma <= 0) and not(codTurma > len(rsTurma))) and (not(codAv <= 0) and not(codAv > len(rsAv)))):
      cursor.execute(''' SELECT CodAluno FROM alunoXturma WHERE CodTurma = ?''',(codTurma, ))
      rs = cursor.fetchall()
      if rs:
        print("\n<<<LISTA DE ALUNO(S)>>>\n")
        for i in rs:
          cursor.execute(''' SELECT * FROM alunos WHERE CodAluno = ?''',(i[0], ))
          rs2 = cursor.fetchone()
          print('Aluno: ', rs2[1], '\nAvaliação: ', rsAv[codAv-1][1])
          nota = float(input('Nota: '))
          print()
          
          cursor.execute(''' INSERT INTO nota (CodAluno, CodAvaliacao, Nota) VALUES (?,?,?) ''',(int(rs2[0]), codAv, nota,))
          conexao.commit()

          os.system('cls')
          
      else:
        print('Não existe registro.')
	
      print('Lançamento de notas finalizado!')
      input('Pressione qualquer tecla para sair.')
	
      flag1 = True

    else:
      codTurma = int(input('Informe o código da turma novamente: '))
      codAv = int(input('Informe o código da avaliação novamente: '))

    os.system('cls')
  return
  
# SISTEMA

import os
import sqlite3

# CRIANDO OU ABRINDO BANCO DE DADOS
conexao = sqlite3.connect("escola.sqlite")
cursor = conexao.cursor()

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS turma (
                      CodTurma integer PRIMARY KEY AUTOINCREMENT,
                      NomeTurma text
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS usuarios (
                      CodUsuario integer PRIMARY KEY AUTOINCREMENT,
                      Usuario text,
                      Senha text,
                      Acesso integer
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS alunos (
                      CodAluno integer PRIMARY KEY AUTOINCREMENT,
                      NomeAluno text,
                      DataNascimento text,
                      Email text,
                      Usuario text
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS professor (
                      CodProfessor integer PRIMARY KEY AUTOINCREMENT,
                      NomeProfessor text,
                      Email text,
                      Usuario text
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS avaliacao (
                      CodAvaliacao integer PRIMARY KEY AUTOINCREMENT,
                      Disciplina text,
                      Descricao text,
                      Valor integer,
                      DataAplicacao text
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS professorXturma (
                      CodProfessor integer,
                      CodTurma integer
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS alunoXturma (
                      CodAluno integer,
                      CodTurma integer
                      ) ''')

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS nota (
                      CodAluno integer,
                      CodAvaliacao integer,
                      Nota real
                      ) ''')

print("="*19 + "\n> SEJA BEM-VINDO! <\n" + "="*19 + "\n \n")

validado = False
perfil = 0

# ENQUANTO VALIDADO FOR FALSO CONTINUA PEDINDO AS INFORMAÇÕES DE LOGIN
while not validado:
  # FUNÇÃO login RETORNA VALORES PARA AS VARIAVEIS
  perfil = Login()
  
  # SE O USUARIO FOR VALIDADO MOSTRA O MENU
  ativo = True

  while ativo:
    for indice, valor in enumerate(Menu(perfil)):
      print(indice+1, valor)
    op = int(input("\nINFORME A OPÇÃO DESEJADA: "))

    obj = []

    # ADMIN CADASTRA PROFESSOR
    if(perfil == 3 and op == 1):
      CadastrarProfessor()
      
    elif(perfil == 3 and op == 2):
      CadastrarTurmas()
      
    elif(perfil == 3 and op == 3):
      # ADMIN CADASTRA ALUNO
      CadastrarAluno()
      
    elif(perfil == 2 and op == 1):
      # PROFESSOR CADASTRA AVALIAÇÃO
      CadastrarAvaliacao()

    elif(perfil == 2 and op == 2):
      # PROFESSOR LANÇA NOTA
      LancarNota()
      
    elif((perfil == 1 and op == 2) or (perfil == 2 and op == 4) or (perfil == 3 and op == 7)):
      # SAIR
      print("TCHAU!!!\n")
      ativo = False
    else:
      print('Você não possui acesso a esse módulo do sistema.')     
