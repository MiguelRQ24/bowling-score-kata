

class BowlingCard:

    X_VALUE = 10
    FAIL_VALUE = 0

    def __init__(self, rolls):

        self.rolls = list(rolls)

        self.frames = self.__separte_in_frames()

        self.total = 0

    def get_rolls(self):
        return self.rolls
    
    def get_frames(self):
        return self.frames
    
    def total_score(self):

        self.frames = self.__symbols_to_numbers()

        self.total = self.__calculate_score()

        return self.total
    
    
    def __separte_in_frames(self):

        rolls = self.rolls[:]
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
                    frames[position_frame][position_roll] = BowlingCard.FAIL_VALUE
                elif roll == "X":
                    frames[position_frame][position_roll] = BowlingCard.X_VALUE
                elif roll == '/':
                    frames[position_frame][position_roll] = 10 - int(frames[position_frame][position_roll - 1])
                else:
                    frames[position_frame][position_roll] = int(frames[position_frame][position_roll])
        return frames
    
    
    def __calculate_score(self):

        total = 0
        for position_frame, frame in enumerate(self.frames[:-1]):
            for roll in frame:
                if roll == BowlingCard.X_VALUE:
                    if len(self.frames[position_frame + 1]) > 1:
                        total += BowlingCard.X_VALUE + self.frames[position_frame + 1][0] + self.frames[position_frame + 1][1]
                    else:
                        total += BowlingCard.X_VALUE + self.frames[position_frame + 1][0] + self.frames[position_frame + 2][0]
                elif sum(frame) == 10:
                    total += 10 + self.frames[position_frame + 1][0]
                    break
                else:
                    total += roll       
        return total + sum(self.frames[9])
    
