class Time:
    def __init__(self,nomeTime:str,cidade:str,mascote:str) -> None:
        self.nomeTime = nomeTime
        self.cidade = cidade
        self.mascote = mascote


class Jogadores(Time):
    def __init__(self, nomeTime: str,nomeJogador:str,numeroCamisa:int) -> None:
        super().__init__(nomeTime, None, None)
        self.nomeJogador = nomeJogador
        self.numeroCamisa = numeroCamisa


class Tecnico(Time):
    def __init__(self,nomeTime:str,cidade:str,nomeTecnico:str,esquema:str) -> None:
        super().__init__(nomeTime, cidade, None)
        self.nomeTecnico = nomeTecnico
        self.esquema = esquema
        
    def dar_coletiva(self):
        return f'{self.nomeTecnico} do time {self.nomeTime} está dando entrevista'
    
    
