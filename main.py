from typing import Deque

ROOT = 'r'

class No:
    def __init__(self, dado):
        self.dado = dado
        self.direita = None
        self.esquerda = None

    #Retornando um nó em string
    def __str__(self):
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self, dado=None, no=None):
        #Essa verificação implica na hora de buscar para retornar uma sub árvore com o nó
        if no:
            self.raiz = no
        
        elif dado:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None
    
    def percurso_em_nivel(self, no=None):
        if no == None:
            no = self.raiz

        fila = Deque()
        fila.append(no)
        while len(fila):
            no = fila.pop()
            if no.esquerda:
                fila.append(no.esquerda)
            if no.direita:
                fila.append(no.direita)
            print(no, end=' |')

class ArvoreBinariaDeBusca(ArvoreBinaria):

    #Inserindo dados
    def inserir(self, valor):
        pai = None
        i = self.raiz
        while(i):
            pai = i
            if valor < i.data:
                i = i.esquerda
            else:
                i = i.direita
        if pai is None:
            self.raiz = No(valor)
        elif valor < pai.dado:
            pai.esquerda = No(valor)
        else:
            pai.direita = No(valor)
    
    #Implica em não precisar definir um valor fixo para no na função _procurar
    def procurar(self, valor):
        return self.procurar_(valor, self.raiz)

    def procurar_(self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreBinariaDeBusca(no)
        if valor < no.dado:
            return self.procurar_(valor, no.esquerda)
        return self.procurar_(valor, no.direita)
    
    def minimo(self, no=ROOT):
        if no == ROOT:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado

    def maximo(self, no=ROOT):
        if no == ROOT:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado

    def remover(self, valor, no=ROOT):
        if no == ROOT:
            no = self.raiz
        
        if no is None:
            return no
        if valor < no.dado:
            no.esquerda = self.remover(valor, no.esquerda)
        elif valor > no.dado:
            no.direita = self.remover(valor, no.direita)
        
        #Achou o valor que queremos
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                #Substituindo os valores, caso o nó removido tenha filhos direito e esquerdo
                substituto = self.minimo(no.direita)
                no.dado = substituto
                no.direita = self.remover(substituto, no.direita)
        
        return no

#Cadastro de clientes de acordo com a quantidade de horas trabalhadas
# Mostrar, inserir e remover algum funcionário
if __name__ == "__main__":
    """ Função usando inserção
    def extended_tree():
        values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
        tree = ArvoreBinariaDeBusca()
        for v in values:
            tree.inserir(v)
        return tree"""

""" Implementando os dados na mão
tree = ArvoreBinariaDeBusca()
tree.inserir(10)
tree.inserir(5)
tree.percurso_em_nivel()"""
