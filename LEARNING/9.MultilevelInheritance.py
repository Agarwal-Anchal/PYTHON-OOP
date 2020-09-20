#class at lower level has access to all upper level
class MusicalInstruments:
    noOfMajorKeys=12
class StringInstruments(MusicalInstruments):
    typeOfWord='Tone word'
class Guitar(StringInstruments):
    def __init__(self):
        self.noOfStrings=6
        print(self.noOfStrings,self.typeOfWord,self.noOfMajorKeys)
guitar=Guitar()
