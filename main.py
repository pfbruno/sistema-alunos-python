import json

def carregar_dados():
  try:
    with open("alunos.json", "r") as arquivo:
      return json.load(arquivo)
  except FileNotFoundError:
        return []
  
alunos = carregar_dados()


def salvar_dados():
  with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)


def cadastrar():
  nome = input("Digite seu nome: ")
  idade = int(input("Informe sua idade: "))
  curso = input("Informe seu curso: ")
  aluno_dados = {
      "nome": nome,
      "idade": idade,
      "curso": curso
  }
  alunos.append(aluno_dados)
  salvar_dados()

def listar():
  if len(alunos) == 0:
   print ("Nenhum aluno cadastrado.")
  else:
   for aluno in alunos:
     print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nCurso: {aluno['curso']}")
     print("-" * 50)

def buscar():
  nome  = input("Digite o nome do aluno:")
  for aluno in alunos:
    if aluno['nome'] == nome:
      print(aluno)
      return
  print("Aluno não encontrado")

def despedida():
  print("Até logo!")

def remover():
  nome = input("Digite o nome do aluno: ")
  for aluno in alunos:
    if aluno['nome'] == nome:
      alunos.remove(aluno)
      salvar_dados()
      print("Aluno removido com sucesso!")
      return
  print("Aluno não encontrado.")

def menu():
  while True:
   tela_menu = ("1 - Cadastrar aluno \n2 - Listar alunos \n3 - Buscar \n4 - Remover \n5 - Sair")
   print(tela_menu)
   opcoes = input("")
   if opcoes == "1":
     cadastrar()
   elif opcoes == "2":
     listar()
   elif opcoes == "3":
     buscar()
   elif opcoes == "4":
     remover()
   elif opcoes == "5":
     despedida()
     break
   else:
     print("Opção inválida.")

menu()