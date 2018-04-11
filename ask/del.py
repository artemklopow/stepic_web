class A:
    def new(self):
        pass
    def popular(self):
        pass


class B:
    objects = A()

m =B.objects

print(isinstance(B.objects, A))