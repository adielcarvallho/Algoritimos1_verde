def CadastroAvaliacao():
  avalicao = []

  cadastroavaliacao = False
  while not cadastroavaliacao:
    avaliacao = input ("Qual disciplina séra aplicada a avaliação? ")
    data =input("Qual a data da avaliação? ")
    nota =input("Qual será a valor da avaliação? ")
    descricao =input("Deseja fazer uma descrição, se não aperte [ENTER]")
  
    print ("Avaliação cadastrada.")
    sair = input ("Deseja cadastra outra avaliação? [S/N]")
    if (sair== 'N' or sair == 'n'):
      cadastroavaliacao = True 

  return
