class A:
    def m1(self):
        print(f'this m from class A')


class B(A):
    def m1(self):
        print(f'this m from class B')


class C(A):
    def m1(self):
        print(f'this m from class C')


class D(B, C):
    # def m1(self):
    #     print(f'this m from class D')
    #     B.m1(self)
    #     C.m1(self)
    #     A.m1(self)

    def m2(self):
        self.m1()


def main():
    x = D()
    x.m2()


if __name__ == '__main__':
    main()
