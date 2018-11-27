class Random_class():
    class_var = 0

    def __init__(self):
        self.__class__.class_var += 1
        self.instance_var = 1

    def __str__(self):
        return(f'Class Var is {self.__class__ .class_var} and instance is {self.instance_var}')


test1_class = Random_class()
print(test1_class)
test2_class = Random_class()
print(test2_class)

