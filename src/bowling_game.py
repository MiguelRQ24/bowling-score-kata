

class BowlingCard:
    # una clase simpre tine que tener un tipo de dato oculto

    def __init__(self, rolls):
        self.rolls = list(rolls) # propiedad de instancia, encapsular
    # roll tirada 
    # Frame el conjunto de 2 tiradas 
    
    def total_score(self):
        self.total = 0
        return self.total