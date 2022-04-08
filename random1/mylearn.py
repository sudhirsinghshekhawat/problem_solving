class Mylearn:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def check_length(self,i):
        return i > len(self)

if __name__ == '__main__':
    mylearn = Mylearn()


    print(mylearn.check_length(5))
    print(mylearn.check_length(-5))
    print(len(mylearn))