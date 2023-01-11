from model.gasto import Gasto
from csv import writer, reader
from os import listdir


class Contador:
    def __init__(self) -> None:

        self.__gastos : list[Gasto] = []
        self.__gasto = Gasto()
        self.arquivo = False


        for item in listdir('./'):
            if item == 'Gastos.csv':
                self.arquivo = list(reader(open('./Gastos.csv', encoding='utf-8'), delimiter=';', lineterminator='\n'))[1:]
                break
                

        
        if self.arquivo:
            for item in self.arquivo:

                self.__gasto = Gasto()

                self.__gasto.auto_input(item) 

                self.__gastos.append(
                    self.__gasto
                )
         
                
            

        while True:

            match input('\nMenu\n\t1-Cadastrar\n\t2-Sair\n\t3-Somar\n\t4-CSV\n\t5-Exibir\n\n').lower():

                case 'cadastrar' | '1':
                    
                    self.__gasto = Gasto()

                    self.__gasto.manual_input()
                    self.__gastos.append(self.__gasto)

                case 'sair' | '2':
                    print('\nFinalizando...')
                    return
                
                case 'somar' | '3':
                    print(f'Soma total : {self.__somar()}')

                case 'csv' | '4':
                    self.__csv()

                case 'exibir' | '5':
                    self.__exibir()

                case _:
                    print('Resposta inválida')
                    continue


    def __exibir(self) -> None:
        
        print('\nData - Nome - Valor')
        for gasto in self.__gastos:
            print(gasto)

    

    def __somar(self) -> float:
        soma : float = 0

        for gasto in self.__gastos:
            soma += gasto.valor
        
        return soma
    
    
    def __csv(self) -> None:

        with open('./Gastos.csv', mode='w', encoding='utf-8', newline='') as arquivo_fisico:
            csv_writer = writer(arquivo_fisico, delimiter=';', lineterminator='\n')

            csv_writer.writerow(['data', 'nome', 'valor'])
            
            for gasto in self.__gastos:
                csv_writer.writerow([gasto.data, gasto.nome, gasto.valor])

        print('Arquivo salvo na pasta do programa')
    