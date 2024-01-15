class Dog:
    kind = "canine"
    tricks = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def addtrick(self, trick):
        self.tricks.append(trick)



yuyo = Dog("yuyo", 10)
dixie = Dog("Dixie", 10)

print(yuyo.getname())
print(yuyo.getage())

print(yuyo.tricks)

yuyo.addtrick("runs_fast")
yuyo.addtrick("rolls")

print(yuyo.tricks)