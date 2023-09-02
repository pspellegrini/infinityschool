#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br
import re
senha = creditCryptContext
nome = input("Digite seu email: ")
senha = CryptSenha(schemes=["pbkdf2_sha256"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=50000)
                   

while True:
    senha = input("Digite sua senha com @ ou # ou * ")
    if senha.isalpha():
        print("Tudo letra")
    elif senha.isdecimal():
        print("tudo número")
    elif senha.isalnum():
        print("Número e letras")
    else:
        print(" Vazia ou caractere especial")

            
       
    senha = input("Digite sua senha: ")
print("Login Ok")
