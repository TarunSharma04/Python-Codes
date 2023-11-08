#polymorphism=>it is oops concept
class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot cannot swim")
class penguin:
    def fly(self):
        print("penguin cannot fly")
    def swim(self):
        print("penguin can swim")
def flying_test(bird):
    bird.fly()
blu=parrot()
peggy=penguin()
flying_test(peggy)
flying_test(blu)