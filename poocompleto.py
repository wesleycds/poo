import json
from datetime import datetime


class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

class Categoria:
    def __init__(self, id: int, descricao: str):
        self.__id = id
        self.__descricao = descricao

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, idcategoria: int):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idcategoria = idcategoria
        

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idcategoria}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def get_idcategoria(self):
        return self.__idcategoria

    def set_idcategoria(self, idcategoria):
        self.__idcategoria = idcategoria

    
class VendaItem:
    def __init__(self, id: int, quantidade: int, preco: float, idvenda: int, idproduto: int):
        self.__id = id
        self.__quantidade = quantidade
        self.__preco = preco
        self.__idvenda = idvenda
        self.__idproduto = idproduto

    def __str__(self):
        return f"{self.__id} - {self.__quantidade} - {self.__preco} - {self.__idvenda} - {self.__idproduto}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_preco_unitario(self):
        return self.__preco

    def set_preco_unitario(self, preco):
        self.__preco = preco

    def get_id_venda(self):
        return self.__idvenda

    def set_id_venda(self, idvenda):
        self.__idvenda = idvenda

    def get_id_produto(self):
        return self.__id_produto

    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

class Venda:
    def __init__(self, id: int, data: datetime, carrinho: bool, total: float, idcliente: int):
        self.__id = id
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        self.__idcliente = idcliente

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idcliente}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_carrinho(self):
        return self.__carrinho

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total

    def get_id_cliente(self):
        return self.__idcliente

    def set_id_cliente(self, idcliente):
        self.__idcliente = idcliente


class Clientes:
    __objetos = [] 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.__objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.__objetos:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            x.set_nome(obj.get_nome())
            x.set_email(obj.get_email())
            x.set_fone(obj.get_fone())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.__objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass

class Categorias:
    __objetos = []  
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.__objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.__objetos:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            x.set_descricao(obj.get_descricao())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.__objetos.remove(x)
            cls.salvar()
        

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    c = Categoria(obj["_Categoria__id"], obj["_Categoria__descricao"])
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass

class Produtos:
    __objetos = [] 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.__objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.__objetos:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            x.set_descricao(obj.get_descricao())
            x.set_preco(obj.get_preco())
            x.set_estoque(obj.get_estoque())
            x.set_idcategoria(obj.get_idcategoria())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.__objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    p = Produto(obj["_Produto__id"], obj["_Produto__descricao"], obj["_Produto__preco"], obj["_Produto__estoque"], obj["_Produto__idcategoria"])
                    cls.__objetos.append(p)
        except FileNotFoundError:
            pass

class Vendas:
    __objetos = []  

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.__objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.__objetos:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            x.set_data(obj.get_data())
            x.set_carrinho(obj.get_carrinho())
            x.set_total(obj.get_total())
            x.set_idcliente(obj.get_idcliente())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.__objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    v = Venda(obj["_Venda__id"], obj["_Venda__data"], obj["_Venda__carrinho"], obj["_Venda__total"], obj["_Venda__idcliente"])
                    cls.__objetos.append(v)
        except FileNotFoundError:
            pass

class VendaItens:
    __objetos = []  

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.__objetos:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.__objetos:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            x.set_quantidade(obj.get_quantidade())
            x.set_preco_unitario(obj.get_preco_unitario())
            x.set_id_venda(obj.get_id_venda())
            x.set_id_produto(obj.get_id_produto())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.__objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=vars)

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("venda_itens.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    vi = VendaItem(obj["__id"], obj["_VendaItem__quantidade"], obj["_VendaItem__preco_unitario"], obj["_VendaItem__id_venda"], obj["_VendaItem__id_produto"])
                    cls.__objetos.append(vi)
        except FileNotFoundError:
            pass

