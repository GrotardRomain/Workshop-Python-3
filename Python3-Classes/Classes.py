class Animal():
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise
dog = Animal()
dog.make_noise()
dog.size = "Small"
dog.color = "black"
dog.hair = "hairless"
class Dog(Animal):
    name= 'Jon'
jon = Dog()
jon.color = 'white'
jon.name = 'Jon Snow'