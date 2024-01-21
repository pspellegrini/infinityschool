from validacoes import (
    valid_email,
    valid_name,
)

users = {}

def cad_user(
    name: str,
    age: int,
    email: str,
    adress: str,
    password: str) -> dict:
    
    if valid_name(name) and valid_email(email):
        user = {
            "name": name,
            "age": age,
            "email": email,
            "adress": adress,
            "password": password
        }
        
        users[email] = user
        
        print(f'Valores inseridos com sucesso.')
        
        return users
    return 'Um ou mais valores estão errados.'

def get_user(email: str):
    if email in users:
        return users[email]
    return f'O email {email} informado não existe.'

def get_password(password: str):
    if password in users:
        return users[password]
    return f'A senha não confere com a cadastrada!'