class Time:
    def __init__(self, nome: str, cidade: str, mascote: str) -> None:
        self.nome = nome
        self.cidade = cidade
        self.mascote = mascote


class Jogadores(Time):
    def __init__(self, nome_jogador: str, nome_time: str, numero_camisa: int):
        super().__init__(nome_time, None, None)
        self.nome_jogador = nome_jogador
        self.numero_camisa = numero_camisa

class Comissão(Time):
    ...

class Tecnico(Time, Comissão)
    def __init__(self, nome_tecnico: str, esq_tatico: str):
        super().__init__(nome_time, None, None)
        self.nome_tecnico = nome_tecnico
        self.esq_tatico = esq_tatico
    
    def coletiva(self):
        return f'O técnico {self.nome_tecnico} está dando uma coletiva de imprensa.'


class Auxiliar(Time, Comissão)
    def __init__(self, nome_auxiliar: str, esq_tatico: str) -> None:
        super().__init__(nome_time, None, None)
        self.nome_auxiliar = nome_auxiliar
        self.esq_tatico = esq_tatico
    
    def coletiva(self):
        return f'O auxiliar {self.nome_auxiliar} está dando uma coletiva de imprensa.'


class Preparador(Time, Comissão)
    def __init__(self, nome_preparador: str, grupo_preparado: str) -> None:
        super().__init__(nome_time)
        self.nome_preparador = nome_auxiliar
        self.esq_tatico = esq_tatico
    
    def coletiva(self):
        return f'O auxiliar {self.nome_auxiliar} está dando uma coletiva de imprensa.'


