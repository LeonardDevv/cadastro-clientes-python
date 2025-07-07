import json
import re
import os

"""
cadastro-clientes-python
"""

clientes = []
id_atual = 1

if os.path.exists('clientes.json'):
    try:
        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)
            if clientes:
                id_atual = max(cliente['Id'] for cliente in clientes) + 1
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def adicionarCliente():
	global id_atual
	nome_cliente = input("Informe o nome do novo cliente: ")
	idade_cliente = int(input("Informe a idade do novo cliente: "))
	email_cliente = input("Informe o e-mail do novo cliente: ")

	while True:
		pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
		if re.match(pattern, email_cliente):
			break
		else:
			print(f'{email_cliente} is incorrect')
			email_cliente = input("Informe o e-mail do novo cliente: ")
		
	novo_cliente = {
	"Nome": nome_cliente,
	"Idade": idade_cliente,
	"E-mail": email_cliente,
	"Id": id_atual,
	"Status": False
	}
	clientes.append(novo_cliente)
	id_atual += 1
	
	
def listarClientes():
	print(f"{'=' * 30}\nLISTA DE CLIENTES CADASTRADOS\n{'=' * 30}")
	for cliente in clientes:
		print(f"Cliente {cliente['Id']}: \nNome: {cliente['Nome']} \nIdade: {cliente['Idade']} \nE-mail: {cliente['E-mail']} \n{'-' * 10}")
		
def atualizarCliente():
	id = int(input("Informe o número do cliente a ser atualizado: "))
	for cliente in clientes:
		if cliente["Id"] == id:
			novo_nome = input("Informe o nome do cliente: ")
			nova_idade = int(input("Informe a idade do cliente: "))
			novo_email = input("Informe o E-mail do cliente: ")
			cliente["Nome"] = novo_nome
			cliente["Idade"] = nova_idade
			cliente["E-mail"] = novo_email
			
		
		
def deletarCliente():
	global clientes
	id = int(input("Informe o número do cliente a ser deletado: "))
	for cliente in clientes:
		if cliente["Id"] == id:
			cliente["Status"] = True
			print(f"Cliente {cliente['Nome']} do E-mail: {cliente['E-mail']} deletado.")
	clientes = [cliente for cliente in clientes if not cliente["Status"]]
	


	
	
	
def iniciar():
	
	while True:
		inicio = int(input(f"Escolha uma opção abaixo: \n\n[ 1 ] - Adicionar cliente \n[ 2 ] - Listar clientes \n[ 3 ] - Atualizar dados do cliente \n[ 4 ] - Deletar cliente \n[ 5 ] - Sair e salvar dados\n\n"))
		
		if inicio == 1:
			adicionarCliente()
		elif inicio == 2:
			listarClientes()
		elif inicio == 3:
			atualizarCliente()
		elif inicio == 4:
			deletarCliente()
		elif inicio == 5:
			print("Saindo...")
			break


iniciar()




try:
    with open('clientes.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso em clientes.json")
except Exception as e:
    print(f"Ocorreu um erro ao salvar os dados: {e}")