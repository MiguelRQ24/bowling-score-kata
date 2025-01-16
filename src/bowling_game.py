

class BowlingCard:
    # una clase simpre tine que tener un tipo de dato oculto

    def __init__(self, rolls):
        self.rolls = list(rolls) # propiedad de instancia, encapsular
    # roll tirada 
    # Frame el conjunto de 2 tiradas 
    
    def total_score(self):

        self.frames = self.__separte_in_frames()
        print(self.frames)
        self.total = 0

        return self.total
    
    def __separte_in_frames(self):
        rolls = self.rolls
        frames = []
        for position in range(10):
            if position == 9:
                frames.append(list(rolls))
            elif rolls[0] != "X":
                frames.append([rolls.pop(0), rolls.pop(0)])
            else:
                frames.append([rolls.pop(0)])
        return frames