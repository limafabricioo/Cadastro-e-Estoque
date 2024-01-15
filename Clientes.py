#Exemplificando a criação de objeto por parâmetro
class Produto:
    def __init__(self, descricao=None, preco=None): #Descrição por paramêtro
        #Atributos == Variáveis da classe: Atributos representam as características do objeto.
        self.descricao = descricao
        self.preco = preco

    def cadastrar_produto(self):
        self.descricao = input("Digite o produto atual: ")
        self.preco = float(input("Digite o preço do produto: "))

    def mostrar_dados(self):
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R${self.preco}")

    def atualizar_dados(self):
        self.cadastrar_produto()

    def __str__(self): #Verificar
        return "<class Produto>"

    def get_descricao(self): #Retorna a informação desejada
        return self.descricao

    def set_descricao(self, nova_descricao):
        self.descricao = nova_descricao

#prod = Produto()
#prod.cadastrar_produto()
#prod.mostrar_dados()
estoque = []
for i in range(3):
  produto = Produto()
  produto.cadastrar_produto()
  produto.mostrar_dados()
  estoque.append(produto)

print("---MOSTRAR---")
for produto in estoque:
  produto.mostrar_dados()