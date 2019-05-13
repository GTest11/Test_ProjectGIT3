
class class_name:
    aa = 0
    def a(self):
        self.aa = 1

    def b(self):
        self.aa = 2
        print self.aa
        # return aa

    def c(self):
        print self.aa

a = class_name()
a.a()
a.c()