import mysql.connector

conexao = mysql.connector.connect(
    host = 'sql812.main-hosting.eu',
    user = 'u274908554_713A',
    password = 'INbd713A',
    database = 'u274908554_713A'
)

cursor = conexao.cursor()

class Usuario:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def nova_senha(self, nova_senha: str) -> None:
        self.__senha = nova_senha

#Métodos de CRUD#

    def pegar_usuario(self, email: str):
        query = f'SELECT * FROM sheep_usuarios WHERE email = "{email}"'
        cursor.execute(query)
        return cursor.fetchall()
    
    def inserir_usuario(self):
        query = f'INSERT INTO sheep_usuarios (nome_user, email, senha) VALUES ("{self.nome}", "{self.email}", "{self.senha}")'
        cursor.execute(query)
        return conexao.commit()
    
    def update_usuario(self, nome: str = None, email: str = None, senha: str = None):
        if nome != None:
            query = f'UPDATE sheep_usuarios SET nome_user = {nome} WHERE email = {self.email}'
            cursor.execute(query)
        if email != None:
            query = f'UPDATE sheep_usuarios SET email = {email} WHERE email = {self.email}'
            cursor.execute(query)
        if senha != None:
            query = f'UPDATE sheep_usuarios SET senha = {senha} WHERE email = {self.email}'
            cursor.execute(query)
        return conexao.commit
    
    def deletar_usuario(self, email: str):
        query = f'DELETE FROM sheep_usuarios WHERE email = "{email}"'
        cursor.execute(query)
        return conexao.commit