# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

#Test Comment
class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.length = len(word)
        self.mask = "_"*self.length
        self.guesses = []

    def failcheck(self):
        self.remaining_guesses -= 1
        if self.remaining_guesses <0:
            self.status = STATUS_LOSE
                
    def guess(self, char):
        if self.status == STATUS_ONGOING:
            if char in self.guesses:
                self.failcheck()
            else:
                self.guesses.append(char)
                if char in self.word:
                    for inc in range(self.length):
                        if self.word[inc] == char:
                            self.mask = self.mask[:inc]+char+self.mask[inc+1:]
                            if "_" not in self.mask:
                                self.status = STATUS_WIN
                else: 
                    self.failcheck()
        else: 
            raise ValueError("No guesses left!")
                    

                

    def get_masked_word(self):
        return self.mask

    def get_status(self):
        return self.status