

class BowlingCard:
    # una clase simpre tine que tener un tipo de dato oculto

    def __init__(self, rolls):
        self.rolls = list(rolls) # propiedad de instancia, encapsular
    # roll tirada 
    # Frame el conjunto de 2 tiradas 
    
    def total_score(self):

        self.frames = self.__separte_in_frames()
        # print(self.frames)
        self.frames = self.__symbols_to_numbers()
        # print(self.frames)

        self.total = self.__calculate_score()
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
    
    def __symbols_to_numbers(self):
        frames = self.frames
        for position_frame, frame in enumerate(frames):
            for position_roll, roll in enumerate(frame):
                if roll == '-':
                    frames[position_frame][position_roll] = 0
                elif roll == "X":
                    frames[position_frame][position_roll] = 10
                elif roll == '/':
                    frames[position_frame][position_roll] = 10 - int(frames[position_frame][position_roll - 1])
                else:
                    frames[position_frame][position_roll] = int(frames[position_frame][position_roll])
        return frames
    
    def __calculate_score(self):
        total = 0
        for position_frame, frame in enumerate(self.frames[:-1]):
            for roll in frame:
                if roll == 10:
                    if len(self.frames[position_frame + 1]) > 1:
                        total += 10 + self.frames[position_frame + 1][0] + self.frames[position_frame + 1][1]
                    else:
                        total += 10 + self.frames[position_frame + 1][0] + self.frames[position_frame + 2][0]
                elif sum(frame) == 10:
                    total += 10 + self.frames[position_frame + 1][0]
                    break
                else:
                    total += roll       
        return total + sum(self.frames[9])