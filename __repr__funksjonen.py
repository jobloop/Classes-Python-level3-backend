class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

#the objects must have either __str__() or __repr__()

    def __repr__(self):
        return f"{self.name} er en {self.occupation}"

u = User('Svarteper', 'feier')
print('\n*--OOP eksempel--*')
print(f'{u}')