class get_and_print:
    def getString(self):
        self.word = input()

    def printString(self):
        print(self.word.upper)
    

gap = get_and_print()
gap.getString()
gap.printString()