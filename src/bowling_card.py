

class BowlingCard:

    X_VALUE = 10
    FAIL_VALUE = 0
    MAX_PINS_POINTS = 10
    TOTAL_FRAMES = 10
    LAST_FRAME_POSITION = 9

    def __init__(self, pins):

        self.pins = pins

        self.rolls = list(pins)

        self.frames = self.__separte_in_frames()

        self.total = self.__calculate_score()
    
    def get_pins(self):
        return self.pins

    def get_rolls(self):
        return self.rolls
    
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
    
    
    def __separte_in_frames(self):

        rolls = self.get_rolls()
        frames = []
        for position in range(self.TOTAL_FRAMES):
            if position == self.LAST_FRAME_POSITION:
                frames.append(self.__symbols_to_numbers(list(rolls)))
            elif rolls[0] != "X":
                frames.append(self.__symbols_to_numbers([rolls.pop(0), rolls.pop(0)]))
            else:
                frames.append(self.__symbols_to_numbers([rolls.pop(0)]))
        return frames
    
    @classmethod
    def __symbols_to_numbers(cls, frame):
        
        only_numbers_frame = frame[:]
        for position_roll, roll in enumerate(frame):
            if roll == '-':
                only_numbers_frame[position_roll] = BowlingCard.FAIL_VALUE
            elif roll == "X":
                only_numbers_frame[position_roll] = BowlingCard.X_VALUE
            elif roll == '/':
                only_numbers_frame[position_roll] = cls.MAX_PINS_POINTS - int(only_numbers_frame[position_roll - 1])
            else:
                only_numbers_frame[position_roll] = int(only_numbers_frame[position_roll])
        return only_numbers_frame

    def __calculate_score(self):

        total = 0
        for position_frame, frame in enumerate(self.get_frames()[:-1]):
            for roll in frame:
                if roll == BowlingCard.X_VALUE:
                    total += self.__value_X_frame(self.get_frames(), position_frame)
                elif sum(frame) == self.MAX_PINS_POINTS:
                    total += self.MAX_PINS_POINTS + self.get_frames()[position_frame + 1][0]
                    break
                else:
                    total += roll       
        return total + sum(self.get_frames()[self.LAST_FRAME_POSITION])
    
    @staticmethod
    def __value_X_frame(frames, position_frame):

            if len(frames[position_frame + 1]) > 1:
                return BowlingCard.X_VALUE + frames[position_frame + 1][0] + frames[position_frame + 1][1]
            else:
                return BowlingCard.X_VALUE + frames[position_frame + 1][0] + frames[position_frame + 2][0]
    