from datetime import date
from model.data import Data

class Gasto:
    def __init__(self) -> None:
        
        self.valor : float = self.__set_valor()
        self.nome : str = self.__set_nome()
        self.data : date = self.__set_data()
    

    def __str__(self) -> str:
        return f'{self.data} - {self.nome} - {self.valor}'
    

    def __set_valor(self) -> float:

        valor : str = ''

        while True:
            try:
                valor = input('Digite o valor : ')
                return float(valor)

            except ValueError:
                print(f'{valor} não pode ser convertido para ponto flutuante.')
                continue

    
    def __set_nome(self) -> str:
        return input('Digite o nome: ')
    

    def __set_data(self) -> date:
        return Data().input_data()


