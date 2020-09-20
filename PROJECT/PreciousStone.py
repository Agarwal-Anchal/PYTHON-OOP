class PreciousStone:
    def __init__(self):
        self.val=[]
    def add(self,new_stone):
        self.val.append(new_stone)
        if(len(self.val)>5):
            self.val.remove(self.val[0])
stone=PreciousStone()
stone.add(1)
print(stone.val)
stone.add(2)
print(stone.val)
stone.add(3)
print(stone.val)
stone.add(4)
print(stone.val)
stone.add(5)
print(stone.val)
stone.add(6)
print(stone.val)
stone.add(7)
print(stone.val)
