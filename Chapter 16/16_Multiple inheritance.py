# Multiple inheritance

class A:
    def class_a_method(self):
        return "Hey, I'm just class A method"

    def hello(self):
        return "Hello class A methods"

class B:
    def class_b_method(self):
        return "Hey, I'm just class B method"

    def hello(self):
        return "Hello class B methods"

class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
print(help(instance_c))