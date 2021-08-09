class ClassA:
    def my_lovely_method(self):
        print("my_lovely_method() method from class A")


class ClassB(ClassA):
    def my_lovely_method(self):
        print("my_lovely_method() method from class B")


object_a = ClassA()
object_b = ClassB()
object_a.my_lovely_method()
object_b.my_lovely_method()
