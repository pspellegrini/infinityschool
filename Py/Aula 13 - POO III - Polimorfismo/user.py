class User:
    def apresentar(self):
        ...
    
    def falar(self):
        ...
    
class User2(User):
    def apresentar(self):
        return 'Essa é a classe User 2.'

class User3(User):
    def apresentar(self):
        return 'Essa é a classe User 3.'

user = User2()
user3 = User3()
print(user.apresentar())
print(user3.apresentar())