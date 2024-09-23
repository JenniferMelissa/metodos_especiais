#metodos especiais
#qualquer metodo que criar no python que comeca e terminar com '__' é um metodo especial 
#ex: __init__ (construtor) 
#ex:__name__ (definir o metodo principal do programa)

class Pessoa:
    #metodo construtor
    def __init__(self, nome, idade, email):
        self.__nome  = nome
        self.__idade = idade
        self.__email = email

    #metodos especiais
    #__str__: serve para retornar representac0es de valores que sejam legiveis para as pessoas. Sempre retorna os valores dos meus atributos em forma de string
    def __str__(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é {self.email}.'
    
    #__repr__: é par gerar representacoes que o interpretador Python consegue ler (ou lebantara uma excecao SyntaxError, se não houver sintaxe equivalente)
    def __repr__(self):
        return f'Pessoa({self.nome}, {self.idade}, {self.email}).'
    
    #retorna o comprimento de um objeto 
    def __len__(self):
        return self.nome
    
    #metodo destrutor, destroi o seu objeto dentro do programa, utilizado para limpeza de memoria,pois quando voce fecha o programa ainda fica com sobras na memoria ram
    #voce ganha memoria mas exige mais processamento da sua maquina, perdendo desempenho em memoria também
    def __del__(self):
        print(f'O objeto {self.nome} foi eliminado com sucesso.')