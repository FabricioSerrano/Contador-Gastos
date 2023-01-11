from datetime import date

class Data:
    def __init__(self) -> None:
        self.dia : int
        self.mes : int
        self.ano : int
        self.__data_final : date


    def input_data(self) -> date:

        print('Data da compra:')
        self.dia : int = self.__set_dia()
        self.mes : int = self.__set_mes()
        self.ano : int = self.__set_ano()

        self.__testar_data()

        while True:

            match input(f'\tA data foi {str(self)} ? (sim / não) ').lower():
                
                case 'sim' | 's':
                    return self.__data_final

                case 'não' | 'nao' | 'n' :
                    print('\nNeste caso, vamos pedir que digite a data novamente.')
                    return self.input_data()

                case _:
                    print('\n\tResposta inválida')
                    continue

        
    def auto_input_data(self, data : str) -> date:

        __data : list[str] = data.split('-')

        self.ano = int(__data[0])
        self.mes = int(__data[1])
        self.dia = int(__data[2])
        
        self.__testar_data()

        return self.__data_final



    def __str__(self) -> str:
        return f'{self.dia}/{self.mes}/{self.ano}'
    

    def __set_dia(self) -> int:

        dia : int = 1

        while True:

            try:
                dia = int(input('\tdia: '))
                return dia
            
            except ValueError:
                print(f'\t{dia} não pode ser convertido para inteiro')
                continue


    def __set_mes(self) -> int:

        mes : int = 1

        while True:

            try:
                mes = int(input('\tmês: '))
                return mes
            
            except ValueError:
                print(f'\t{mes} não pode ser convertido para inteiro')
                continue


    def __set_ano(self) -> int:

        ano : int = 1

        while True:

            try:
                ano = int(input('\tano: '))
                return ano
            
            except ValueError:
                print(f'\t{ano} não pode ser convertido para inteiro')
                continue


    def __testar_data(self) -> None | date:
        try:
            self.__data_final =  date(
                self.ano,
                self.mes,
                self.dia
            )
        except ValueError:
            print('\tData inválida. ')
            return self.input_data()