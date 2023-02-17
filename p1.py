class Army:
    def __init__(self, n):
        self.name = n
        # self.g = self.Gun()

    def show(self):
        print("Name :", self.name)

    class Gun():
        def __init__(self, t):
            self.type = t

        def disp(self):
            print("Type :", self.type)


a = Army('A-1')
g = a.Gun('AK47')
a.show()
g.disp()
