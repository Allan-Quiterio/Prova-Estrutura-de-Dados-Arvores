import os
from typing import Deque

ROOT = 'root'

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
    
    def percurso_em_nivel(self, no=ROOT):
        if no == ROOT:
            no = self.raiz

        fila = Deque()
        fila.append(no)
        while len(fila):
            # Pai -> Nó esquerdo -> Nó direito
            no = fila.popleft()
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
            #Verifica se o novo valor é maior ou menor que o valor que já está na árvore
            pai = i
            if valor < i.dado:
                i = i.esquerda
            else:
                i = i.direita
        #Valor vira raiz
        if pai is None:
            self.raiz = No(valor)
        #Armazenando o novo valor
        elif valor < pai.dado:
            pai.esquerda = No(valor)
        else:
            pai.direita = No(valor)
    
    #Implica em não precisar definir um valor fixo para no na função _procurar
    def pesquisar(self, valor):
        return self.pesquisar_(valor, self.raiz)

    def pesquisar_(self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreBinariaDeBusca(no)
        if valor < no.dado:
            return self.pesquisar_(valor, no.esquerda)
        return self.pesquisar_(valor, no.direita)
    
    #Menor nó da raiz
    def menor(self, no=ROOT):
        if no == ROOT:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado

    #Maior nó da raiz
    def maior(self, no=ROOT):
        if no == ROOT:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.dado

    def remover(self, valor, no=ROOT):
        #Valor padrão, a partir da raiz
        if no == ROOT:
            no = self.raiz
        
        #Ramo nulo
        if no is None:
            return no
        
        #Menor ou maior
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
                x = self.menor(no.direita)
                no.dado = x
                no.direita = self.remover(x, no.direita)

        return no

if __name__ == "__main__":
    arvore = ArvoreBinariaDeBusca()

    print('-'*60)
    print("Seja bem vindo ao cadastro de matrículas!")
    while True:
        print('-'*60)
        print('[1] Adicionar uma nova matrícula ao sistema\n[2] Ver a árvore de matrículas cadastradas')
        print('[3] Matrícula mais antiga\n[4] Matrícula mais recente\n[5] Procurar por matrícula')
        print('[6] Remover uma matrícula\n[7]Sair')
        print('-'*60)
        
        resp = int(input('Opção: '))
        os.system('cls')
        
        if resp < 1 or resp > 7:
            print("Opção não encontrada, digite um valor válido")

        elif resp == 7:
            print('Saindo...')
            break

        elif resp == 1:
            num = input(("Digite a matrícula do funcionário para incluirmos em nosso banco de dados: "))
            arvore.inserir(num)

        elif resp == 2:
            arvore.percurso_em_nivel()
            print('\n')

        elif resp == 3:
            print(arvore.menor())

        elif resp == 4:
            print(arvore.maior())

        elif resp == 5:
            procura = input('Digite a matrícula a ser procurada no banco de dados: ')
            r = arvore.pesquisar(procura)
            if r is None:
                print("Matrícula", procura,"não encontrada")
            else:
                print(procura, 'está no nosso sistema')

        else:
            rem = input('Qual item você quer remover: ')
            r = arvore.pesquisar(rem)   
            if r is None:
                print('Essa matrícula não se encontra em nosso banco')
            else:
                arvore.remover(rem)