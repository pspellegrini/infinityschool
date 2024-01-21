import re

def valid_email(email: str) -> bool:
    if '@' in email:
        return True
    return False

def valid_name(name: str) -> bool:
    if len(name) > 10:
        return True
    return False

def valid_password(password: str) -> bool:
    while not (re.search(r'.{8,}', password) and   
           re.search(r'[A-Z]', password) and 
           re.search(r'\d', password) and   
           re.search(r'[!@#$%¨&*]', password))
    
'''https://pt.stackoverflow.com/questions/519132/como-fazer-valida%C3%A7%C3%A3o-de-senha-em-python'''