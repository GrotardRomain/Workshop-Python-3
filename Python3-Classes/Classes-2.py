class Animal():
    name = "Amy"
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers body"
    def get_color(self, abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_color("red")
dog.make_noise

abc ="new string"
def some_func(arg_1, arg_2, kwarg_1=None, kwarg_2=None):
    print(arg_1, arg_2)
    if kwarg_1 != None:
        print(kwarg_1)
        # return arg_1
some_func("abc", "car", kwarg_1='Not a big deal')