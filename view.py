from poocompleto import Cliente, Clientes, Categoria, Categorias, Produto, Produtos


class View:

    #cliente
    @staticmethod
    def cliente_inserir(nome, email, fone):
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)
    @staticmethod

    def cliente_excluir(id):
        a = Cliente(id, "","", "")
        Clientes.excluir(a)

    #categoria

    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    
    @staticmethod
    def categoria_inserir(descricao):
        a = Categoria(0, descricao)
        Categorias.inserir(a)

    @staticmethod
    def categoria_atualizar(id, descricao):
        a = Categoria(id, descricao)
        Categorias.atualizar(a)

    @staticmethod
    def categoria_excluir(id):
        a = Categoria(id, "")
        Categorias.excluir(a)

    #produto

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    
    @staticmethod
    def produto_inserir(descricao, preco, estoque, idcategoria):
        a = Produto(0, descricao, preco, estoque, idcategoria)
        Produtos.inserir(a)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idcategoria):
        a = Produto(id, descricao, preco, estoque, idcategoria)
        Produtos.atualizar(a)

    @staticmethod
    def produto_excluir(id):
        a = Produto(id, "",0,0,0)
        Produtos.excluir(a)
        




