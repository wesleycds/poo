
from view import View


class UI:
    @staticmethod
    def menu():
        print("\nMenu Principal")
        print("  1 - Listar Clientes")
        print("  2 - Inserir Cliente")
        print("  3 - Atualizar Cliente")
        print("  4 - Excluir Cliente")
        print("  5 - Listar Produtos")
        print("  6 - Inserir Produto")
        print("  7 - Atualizar Produto")
        print("  8 - Excluir Produto")
        print("  9 - Listar Categoria")
        print("  10 - Inserir Categoria")
        print("  11 - Atualizar Categoria")
        print("  12 - Excluir Categoria")
        print("  20 - Finalizar")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 20:
            op = UI.menu()
            if op == 1: UI.listar_clientes()
            if op == 2: UI.inserir_cliente()
            if op == 3: UI.atualizar_cliente()
            if op == 4: UI.excluir_cliente()
            if op == 5: UI.listar_produtos()
            if op == 6: UI.inserir_produto()
            if op == 7: UI.atualizar_produto()
            if op == 8: UI.excluir_produto()
            if op == 9: UI.listar_categoria()
            if op == 10: UI.inserir_categoria()
            if op == 11: UI.atualizar_categoria()
            if op == 12: UI.excluir_categoria()


#CATEGORIA
    @staticmethod
    def listar_categoria():
        
        for categoria in View.categoria_listar():
            print(categoria)

    @staticmethod
    def inserir_categoria():

        descricao = input("informe a descricao da categoria: ")
        View.categoria_inserir(descricao)

    @staticmethod
    def atualizar_categoria():
        UI.listar_categoria()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("informe a nova descricao: ")
        View.categoria_atualizar(id, descricao)


    @staticmethod
    def excluir_categoria():
        UI.listar_categoria()
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.categoria_excluir(id)


#CLIENTE      
    @staticmethod
    def listar_clientes():
        
        for cliente in View.cliente_listar():
            print(cliente)

    @staticmethod
    def inserir_cliente():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        View.cliente_inserir(nome, email, fone)

    @staticmethod
    def atualizar_cliente():
        UI.listar_clientes()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        View.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def excluir_cliente():
        UI.listar_clientes()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id,)

#PRODUTO     

    @staticmethod
    def listar_produtos(): 
        for produto in View.produto_listar():
         print(produto)

    @staticmethod
    def inserir_produto():
        descricao = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço do produto: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idcategoria = int(input("Informe o ID da categoria: "))
        View.produto_inserir(descricao, preco, estoque, idcategoria)

    @staticmethod
    def atualizar_produto():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe a nova quantidade em estoque: "))
        idcategoria = int(input("Informe o novo ID da categoria: "))
        View.produto_atualizar(id, descricao, preco, estoque, idcategoria)

    @staticmethod
    def excluir_produto():
        UI.listar_produtos()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.produto_excluir(id)


UI.main()