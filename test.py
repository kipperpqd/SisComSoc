class Person():
    def __init__(self, nome, sexo):
        self.nome = nome 
        self.sexo = sexo
        
class Military(Person):
    def __init__(self, nome, sexo, pg):
        super().__init__(nome, sexo)
        self.pg = pg
        
        
class Comander(Person):
    def __init__(self, nome, sexo, om):
        self.om = om
        super().__init__(nome, sexo)
        
        
mil = Military(nome = "Kipper",
               pg = "2º Sgt", 
               sexo = "M"),

cmt = Comander(nome="Torres", 
               sexo="M", 
               om="Pq R Mnt/10",
)

cmt.om = "23 BC"

print(mil.nome)
print(cmt.om)
        