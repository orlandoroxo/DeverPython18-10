# Aluno: Orlando da Silva Roxo
# Pré-requisitos: psycopg2 (PostgreSQL Driver) - pip install psycopg2
# Para compilar e executar: python pythonCrud.py

import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="meubanco",
        user="orlando",
        password="orlando2552"
    )

def inserir_dados_arquivo_txt():
    with open('dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            nome, idade, cidade = linha.strip().split(',')
            inserir(nome, idade, cidade)

def inserir(nome, idade, cidade):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO dados (nome, idade, cidade) VALUES (%s, %s, %s)", (nome, idade, cidade))
    con.commit()
    cursor.close()
    con.close()

def listar():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dados")
    registros = cursor.fetchall()
    cursor.close()
    con.close()
    return registros

def atualizar(id, nome, idade, cidade):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("UPDATE dados SET nome=%s, idade=%s, cidade=%s WHERE id=%s", (nome, idade, cidade, id))
    con.commit()
    cursor.close()
    con.close()

def remover(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM dados WHERE id=%s", (id,))
    con.commit()
    cursor.close()
    con.close()

def menu():
    print("Menu de Opções:")
    print("1 - Inserir dados do arquivo TXT")
    print("2 - Listar registros")
    print("3 - Atualizar registro")
    print("4 - Remover registro")
    print("5 - Sair")
    return int(input("Escolha uma opção: "))

if __name__ == '__main__':
    while True:
        opcao = menu()

        if opcao == 1:
            inserir_dados_arquivo_txt()
            print("Dados inseridos a partir do arquivo TXT.")

        elif opcao == 2:
            registros = listar()
            print("\nDados registrados:")
            for registro in registros:
                print(registro)

        elif opcao == 3:
            id = int(input("Digite o ID do registro a ser atualizado: "))
            nome = input("Digite o novo nome: ")
            idade = input("Digite a nova idade: ")
            cidade = input("Digite a nova cidade: ")
            atualizar(id, nome, idade, cidade)
            print("Registro atualizado.")

        elif opcao == 4:
            id = int(input("Digite o ID do registro a ser removido: "))
            remover(id)
            print("Registro removido.")

        elif opcao == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
