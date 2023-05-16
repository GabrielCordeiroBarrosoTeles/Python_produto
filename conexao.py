import mysql.connector
conexao = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "mercado",
)
cursor = conexao.cursor()
opcao = int(input("1-Cadastrar \n2-Exibir \n3-Editar \n4-Deletar"))
if(opcao==1):
    descricao = input("informe a descricao do produto: \n")
    marca = input("informe a marca do produto: \n")
    valor_compra = input("informe o valor da compra: \n")
    valor_venda = input("informe o valor da venda: \n")
    n_lote = input("informe o n do lote: \n")
    data_fab = input("informe a data de fabricacao: \n")
    data_val = input("informe a data de validae: \n")
    comando = f"INSERT INTO produtos VALUES(0,'{descricao}','{marca}','{valor_compra}','{valor_venda}','{n_lote}','{data_fab}','{data_val}')"
    cursor.execute(comando)
elif(opcao==2):
    comando2 = 'SELECT * FROM produtos'
    cursor.execute(comando2)
    resultado = cursor.fetchall()
    print(resultado)
elif(opcao==3):
    pesq_id= int(input("Informe o numero do id"))
    new_valor = int(input("Novo valor"))
    comando3 = f'UPDATE produtos SET valor_venda="{new_valor}" WHERE id="{pesq_id}"'
    cursor.execute(comando3)

elif (opcao == 4):
    pesq_id = int(input("Informe o numero do id"))
    comando3 = f'DELETE produtos WHERE id="{pesq_id}"'
    cursor.execute(comando3)


conexao.commit()
cursor.close()
conexao.close()

