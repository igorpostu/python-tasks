class Company:
    def __init__(self, name: str, email: str, adress: str):
        self.name = name
        self.email = email
        self.adress = adress
    
    def __str__(self):
        return f'{self.name}\n{self.email}\n{self.adress}'

comp1 = Company('PowerIT', 'office@powerit.dev', 'https://powerit.dev')

print(comp1)