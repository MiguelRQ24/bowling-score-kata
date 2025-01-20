

class BowlingCard:

    X_VALUE = 10
    FAIL_VALUE = 0

    def __init__(self, pins):

        self.rolls = list(pins)

        self.frames = self.__separte_in_frames()

        self.total = self.__calculate_score()

    def get_rolls(self):
        return ''.join(self.rolls)
    
    def get_frames(self):
        return self.frames
    
    def get_total_score(self):
        return self.total
    
    '''
    def total_score(self):

        # self.frames = self.__symbols_to_numbers()

        self.total = self.__calculate_score()

        return self.total
    '''
    
    def __separte_in_frames(self):

        rolls = self.rolls[:]
        frames = []
        for position in range(10):
            if position == 9:
                frames.append(self.__symbols_to_numbers(list(rolls)))
            elif rolls[0] != "X":
                frames.append(self.__symbols_to_numbers([rolls.pop(0), rolls.pop(0)]))
            else:
                frames.append(self.__symbols_to_numbers([rolls.pop(0)]))
        return frames
    
    '''
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
        '''
    
    @staticmethod
    def __symbols_to_numbers(frame):
        only_numbers_frame = frame[:]
        for position_roll, roll in enumerate(frame):
            if roll == '-':
                only_numbers_frame[position_roll] = BowlingCard.FAIL_VALUE
            elif roll == "X":
                only_numbers_frame[position_roll] = BowlingCard.X_VALUE
            elif roll == '/':
                only_numbers_frame[position_roll] = 10 - int(only_numbers_frame[position_roll - 1])
            else:
                only_numbers_frame[position_roll] = int(only_numbers_frame[position_roll])
        return only_numbers_frame

    def __calculate_score(self):

        total = 0
        for position_frame, frame in enumerate(self.frames[:-1]):
            for roll in frame:
                if roll == BowlingCard.X_VALUE:
                    total += self.__value_X_frame(self.frames, position_frame)
                elif sum(frame) == 10:
                    total += 10 + self.frames[position_frame + 1][0]
                    break
                else:
                    total += roll       
        return total + sum(self.frames[9])
    
    @staticmethod
    def __value_X_frame(frames, position_frame):
            if len(frames[position_frame + 1]) > 1:
                return BowlingCard.X_VALUE + frames[position_frame + 1][0] + frames[position_frame + 1][1]
            else:
                return BowlingCard.X_VALUE + frames[position_frame + 1][0] + frames[position_frame + 2][0]