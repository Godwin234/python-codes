import numpy as np

print("This program is designed to solve Matrix addition, subtraction, multiplication and Determinant matrix.\n"
      " It also contains a class that can solve simultaneous equation.\n"
      "Below are the starting code to solve problems on the program.\n"
      "For matrix,\n"
      "1. 'do addition' : for addition matrix .\n"
      "2. 'do multiplication' : for multiplication matrix.\n"
      "3. 'do subtraction': for subtraction matrix.\n"
      "4. 'do determinant': for finding the determinant of a matrix.\n"
      "5. 'do scalar': for multiplication with a scalar.\n"
      "6. 'solve equation': for solving simultaneous equation.\n"
      "7. 'close app' : for closing the application.\n"
      "")


class Matrix:
    class_name = ""

    objects = {}

    def __init__(self, name):
        self.name = name
        Matrix.objects[self.class_name] = self

    def solve_matrix(self):
        return Matrix.objects[self.class_name].solve()

    def close_matrix(self):
        return Matrix.objects[self.class_name].close()

    def m2x3_m3x2_matrix(self):
        return Matrix.objects[self.class_name].m2x3_m3x2()

    def m2x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m2x3_m3x3()

    def m2x3_m3x1_matrix(self):
        return Matrix.objects[self.class_name].m2x3_m3x1()

    def m3x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m3x3m()

    def m3x2_m2x3_matrix(self):
        return Matrix.objects[self.class_name].m3x2_m2x3()

    def m3x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m3x2_m2x2()

    def m3x2_m2x1_matrix(self):
        return Matrix.objects[self.class_name].m3x2_m2x1()

    def m1x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m1x3_m3x3()

    def m1x3_m3x2_matrix(self):
        return Matrix.objects[self.class_name].m1x3_m3x2()

    def m1x3_m3x1_matrix(self):
        return Matrix.objects[self.class_name].m1x3_m3x1()

    def m2x1_m1x3_matrix(self):
        return Matrix.objects[self.class_name].m2x1_m1x3()

    def m2x1_m1x2_matrix(self):
        return Matrix.objects[self.class_name].m2x1_m1x2()

    def m1x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m1x2_m2x2()

    def m1x2_m2x3_matrix(self):
        return Matrix.objects[self.class_name].m1x2_m2x3()

    def m3x1_m1x2_matrix(self):
        return Matrix.objects[self.class_name].m3x1_m1x2()

    def m3x1_m1x3_matrix(self):
        return Matrix.objects[self.class_name].m3x1_m1x3()

    def m1x2_m2x1_matrix(self):
        return Matrix.objects[self.class_name].m1x2_m2x1()

    def m2x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m2x2m()

    def am2x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m2x2a()

    def am3x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m3x3a()

    def sm2x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m2x2s()

    def sm3x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m3x3s()

    def detm2x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m2x2det()

    def detm3x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m3x3det()

    def scm2x2_m2x2_matrix(self):
        return Matrix.objects[self.class_name].m2x2scalar()

    def scm3x3_m3x3_matrix(self):
        return Matrix.objects[self.class_name].m3x3scalar()


class Addition(Matrix):
    def __init__(self, name):
        self.class_name = "addition"
        super().__init__(name)

    def m3x3a(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        g = int(input("enter g for matrix A: "))
        h = int(input("enter h for matrix A: "))
        i = int(input("enter i for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        p = int(input("enter g for matrix B: "))
        q = int(input("enter h for matrix B: "))
        r = int(input("enter i for matrix B: "))
        y = np.array([[a,b,c],[d,e,f],[g,h,i]])
        z = np.array([[j,k,l],[m,n,o],[p,q,r]])
        print("the resulting Matrix is : ")
        return y + z

    def m2x2a (self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter a for matrix B: "))
        f = int(input("enter b for matrix B: "))
        g = int(input("enter c for matrix B: "))
        h = int(input("enter d for matrix B: "))
        y = np.array([[a, b], [c, d]])
        z = np.array([[e, f], [g, h]])
        return y + z


addition = Addition("addition")


class Subtraction(Matrix):
    def __init__(self, name):
        self.class_name = "subtraction"
        super().__init__(name)

    def m2x2s(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter a for matrix B: "))
        f = int(input("enter b for matrix B: "))
        g = int(input("enter c for matrix B: "))
        h = int(input("enter d for matrix B: "))
        y = np.array([[a, b], [c, d]])
        z = np.array([[e, f], [g, h]])
        print("The resulting Matrix is")
        return y - z

    def m3x3s(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        g = int(input("enter g for matrix A: "))
        h = int(input("enter h for matrix A: "))
        i = int(input("enter i for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        p = int(input("enter g for matrix B: "))
        q = int(input("enter h for matrix B: "))
        r = int(input("enter i for matrix B: "))
        y = np.array([[a, b, c], [d, e, f], [g, h, i]])
        z = np.array([[j, k, l], [m, n, o], [p, q, r]])
        return y - z


subtraction = Subtraction("subtraction")


class Multiplication (Matrix):
    def __init__(self, name):
        self.class_name = "multiplication"
        super().__init__(name)

    def m2x2m(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        a1 = ((a * j) + (b * l))
        b1 = ((a * k) + (b * m))
        c1 = ((c * j) + (d * l))
        d1 = ((c * k) + (d * m))
        y = np.array([[a1, b1], [c1, d1]])
        print("The resulting Matrix is")
        return y

    def m3x3m(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        g = int(input("enter g for matrix A: "))
        h = int(input("enter h for matrix A: "))
        i = int(input("enter i for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        p = int(input("enter g for matrix B: "))
        q = int(input("enter h for matrix B: "))
        r = int(input("enter i for matrix B: "))
        a1 = ((a * j) + (b * m) + (c * p))
        b1 = ((a * k) + (b * n) + (c * q))
        c1 = ((a * l) + (b * o) + (c * r))
        d1 = ((d * j) + (e * m) + (f * p))
        e1 = ((d * k) + (e * n) + (f * q))
        f1 = ((d * l) + (e * o) + (f * r))
        g1 = ((g * j) + (h * m) + (i * p))
        h1 = ((g * k) + (h * n) + (i * q))
        i1 = ((g * l) + (h * o) + (i * r))
        y = np.array([[a1, b1, c1], [d1, e1, f1], [g1, h1, i1]])

        print("The resulting Matrix is : ")
        return y

    def m2x3_m3x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        p = int(input("enter g for matrix B: "))
        q = int(input("enter h for matrix B: "))
        r = int(input("enter i for matrix B: "))
        a1 = ((a*j) + (b*m) + (c*p))
        b1 = ((a*k) + (b*k) + (c*q))
        c1 = ((a*l) + (b*o) + (c*r))
        d1 = ((d*j) + (e*m) + (f*p))
        e1 = ((d*k) + (e*n) + (f*q))
        f1 = ((d*l) + (e*o) + (f*r))
        z = np.array([[a1, b1, c1], [d1, e1, f1]])
        print("The resulting  Matrix is")
        return z

    def m2x3_m3x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        a1 = ((a * j) + (b * l) + (c * n))
        b1 = ((a * k) + (b * m) + (c * o))
        c1 = ((d * j) + (e * l) + (f * n))
        d1 = ((d * k) + (e * m) + (f * o))
        z = np.array([[a1, b1], [c1, d1]])
        print("The resulting  Matrix is")
        return z

    def m1x2_m2x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        a1 = ((a*j) + (b*l))
        b1 = ((a*k) + (b*m))
        y = np.array([[a1, b1]])
        print("The resulting  Matrix is")
        return y

    def m1x2_m2x1(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        a1 = ((a * j) + (b * k))
        y = np.array([[a1]])
        print("The resulting  Matrix is")
        return y

    def m3x2_m2x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        a1 = ((a * j) + (b * m))
        b1 = ((a * k) + (b * n))
        c1 = ((a * l) + (b * o))
        d1 = ((c * j) + (d * m))
        e1 = ((c * k) + (d * n))
        f1 = ((c * l) + (d * o))
        g1 = ((e * j) + (f * m))
        h1 = ((e * k) + (f * n))
        i1 = ((e * l) + (f * o))
        z = np.array([[a1, b1, c1], [d1, e1, f1], [g1, h1,i1 ]])
        print("The resulting  Matrix is")
        return z

    def m2x3_m3x1(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))

        a1 = ((a * j) + (b * k) + (c * l))

        d1 = ((d * j) + (e * k) + (f * l))
        z = np.array([[a1], [d1]])
        print("The resulting  Matrix is")
        return z

    def m3x2_m2x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))

        a1 = ((a * j) + (b * l))
        b1 = ((a * k) + (b * m))
        c1 = ((c * j) + (d * l))
        d1 = ((c * k) + (d * m))
        e1 = ((e * j) + (f * l))
        f1 = ((e * k) + (f * m))

        z = np.array([[a1, b1], [c1, d1], [e1, f1 ]])
        print("The resulting  Matrix is")
        return z

    def m3x2_m2x1(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))

        a1 = ((a * j) + (b * k))

        c1 = ((c * j) + (d * k))

        e1 = ((e * j) + (f * k))

        z = np.array([[a1], [c1], [e1]])
        print("The resulting  Matrix is")
        return z

    def m1x3_m3x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        p = int(input("enter g for matrix B: "))
        q = int(input("enter h for matrix B: "))
        r = int(input("enter i for matrix B: "))
        a1 = ((a * j) + (b * m) + (c * p))
        b1 = ((a * k) + (b * n) + (c * q))
        c1 = ((a * l) + (b * o) + (c * r))

        z = np.array([[a1, b1, c1]])
        print("The resulting  Matrix is")
        return z

    def m1x3_m3x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))

        a1 = ((a * j) + (b * l) + (c * n))
        b1 = ((a * k) + (b * m) + (c * o))

        z = np.array([[a1, b1]])
        print("The resulting  Matrix is")
        return z

    def m1x3_m3x1(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        a1 = ((a * j) + (b * k) + (c * l))

        z = np.array([[a1]])
        print("The resulting  Matrix is")
        return z

    def m2x1_m1x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))

        a1 = a*j
        b1 = a*k
        c1 = a*l
        d1 = b*j
        e1 = b*k
        f1 = b*l
        z = np.array([[a1, b1], [c1, d1], [e1, f1]])
        print("The resulting  Matrix is")
        return z

    def m2x1_m1x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        a1 = a * j
        b1 = a * k
        d1 = b * j
        e1 = b * k

        z = np.array([[a1, b1], [d1, e1]])
        print("The resulting  Matrix is")
        return z

    def m1x2_m2x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        m = int(input("enter d for matrix B: "))
        n = int(input("enter e for matrix B: "))
        o = int(input("enter f for matrix B: "))
        a1 = ((a * j) + (b * m))
        b1 = ((a * k) + (b * n))
        c1 = ((a * l) + (b * o))
        z = np.array([[a1, b1, c1]])
        print("The resulting  Matrix is")
        return z

    def m3x1_m1x2(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))

        a1 = a * j
        b1 = a * k
        c1 = b * j
        d1 = b * k
        e1 = c * j
        f1 = c * k

        z = np.array([[a1, b1, c1], [d1, e1, f1]])
        print("The resulting  Matrix is")
        return z

    def m3x1_m1x3(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        j = int(input("enter a for matrix B: "))
        k = int(input("enter b for matrix B: "))
        l = int(input("enter c for matrix B: "))
        a1 = a * j
        b1 = a * k
        c1 = a * l
        d1 = b * j
        e1 = b * k
        f1 = b * l
        g1 = c * j
        h1 = c * k
        i1 = c * l
        y = np.array([[a1, b1, c1], [d1, e1, f1], [g1, h1, i1]])

        print("The resulting Matrix is : ")
        return y


multi = Multiplication("multiplication")


class Scalar (Matrix):
    def __init__(self, name):
        self.class_name = "scalar"
        super().__init__(name)

    def m3x3scalar(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        g = int(input("enter g for matrix A: "))
        h = int(input("enter h for matrix A: "))
        i = int(input("enter i for matrix A: "))
        m = int(input("enter the multiplying scalar number"))
        y = np.array([[a, b, c], [d, e, f], [g, h, i]])
        print("The resulting  Matrix is")
        return y * m

    def m2x2scalar(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter the multiplying scalar number"))
        y = np.array([[a, b], [c, d]])
        print("The resulting  Matrix is")
        return y * e


scalar = Scalar("scalar")


class Determinant (Matrix):
    def __init__(self, name):
        self.class_name = "determinant"
        super().__init__(name)

    def m3x3det(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        e = int(input("enter e for matrix A: "))
        f = int(input("enter f for matrix A: "))
        g = int(input("enter g for matrix A: "))
        h = int(input("enter h for matrix A: "))
        i = int(input("enter i for matrix A: "))
        det = (a*((e*i) - (h*f))) - (b*((d*i) - (f*g))) + (c*((d*h) - (g*e)))
        print("The determinant of the Matrix is")
        return det

    def m2x2det(self):
        a = int(input("enter a for matrix A: "))
        b = int(input("enter b for matrix A: "))
        c = int(input("enter c for matrix A: "))
        d = int(input("enter d for matrix A: "))
        det = ((a*d) - (b*c))
        print("The determinant of the Matrix is")
        return det


determinant = Determinant("determinant")


class Equation (Matrix):
    def __init__(self, name):
        self.class_name = "equation"
        super().__init__(name)

    def solve(self):
        a = int(input("enter first x variable: "))
        b = int(input("enter first y variable: "))
        c = int(input("enter first constant: "))
        a2 = int(input("enter second x variable: "))
        b2 = int(input("enter second y variable: "))
        c2 = int(input("enter second constant: "))

        e1 = a * a2
        d1 = b * a2
        g1 = c * a2
        e2 = a2 * a
        d2 = b2 * a
        g2 = c2 * a
        h1 = d1 - d2
        h2 = g1 - g2
        y = h2 / h1
        x = (c - (b * y)) / a

        print("the value of x is: ")
        print(x)
        print("the value of y is: ")
        print(y)
        return


equation = Equation("equation")


class App (Matrix):
    def __init__(self, name):
        self.class_name = "app"
        super().__init__(name)

    def close(self):
        exit()


app = App("app")


def solve(noun):
    if noun in Matrix.objects:
        return Matrix.objects[noun].solve_matrix()
    else:
        return "There is no {} here.".format(noun)


def close(noun):
    if noun in Matrix.objects:
        return Matrix.objects[noun].close_matrix()
    else:
        return "There is no {} here.".format(noun)


def do(noun):
    if noun in Matrix.objects:
        if noun == "scalar" or noun == "determinant":
            mtrA = input("Enter the dimension of the matrix: ")
            if mtrA == "3x3" and noun == "determinant":
                print("you are about to calculate determinant 3x3")
                return Matrix.objects[noun].detm3x3_m3x3_matrix()
            elif mtrA == "2x2" and noun == "determinant":
                print("you are about to calculate determinant 2x2")
                return Matrix.objects[noun].detm2x2_m2x2_matrix()
            elif mtrA == "3x3" and noun == "scalar":
                print("you are about to calculate 3x3 multiply by a scalar")
                return Matrix.objects[noun].scm3x3_m3x3_matrix()
            elif mtrA == "2x2" and noun == "scalar":
                print("you are about to calculate 2x2 multiply by a scalar")
                return Matrix.objects[noun].scm2x2_m2x2_matrix()
            else:
                return "There is no {} here.".format(noun)

        elif noun == "multiplication" or noun == "addition" or noun == "subtraction":
            mtrA = input("Enter the dimension of matrix A: ")
            mtrB = input("Enter the dimension of matrix B: ")
            if mtrA == "2x3" and mtrB == "3x3" and noun == "multiplication":
                print("you are about to calculate 2x3 multiplied by 3x3")
                return Matrix.objects[noun].m2x3_m3x3_matrix()
            elif mtrA == "2x3" and mtrB == "3x2" and noun == "multiplication":
                print("you are about to calculate 2x3 multiplied by 3x2")
                return Matrix.objects[noun].m2x3_m3x2_matrix()
            elif mtrA == "3x3" and mtrB == "3x3" and noun == "multiplication":
                print("you are about to calculate 3x3 multiplied by 3x3")
                return Matrix.objects[noun].m3x3_m3x3_matrix()
            elif mtrA == "2x3" and mtrB == "3x1" and noun == "multiplication":
                print("you are about to calculate 2x3 multiplied by 3x1")
                return Matrix.objects[noun].m2x3_m3x1_matrix()
            elif mtrA == "3x2" and mtrB == "2x3" and noun == "multiplication":
                print("you are about to calculate 3x2 multiplied by 2x3")
                return Matrix.objects[noun].m3x2_m2x3_matrix()
            elif mtrA == "3x2" and mtrB == "2x2" and noun == "multiplication":
                print("you are about to calculate 3x2 multiplied by 2x2")
                return Matrix.objects[noun].m3x2_m2x2_matrix()
            elif mtrA == "3x2" and mtrB == "2x1" and noun == "multiplication":
                print("you are about to calculate 3x2 multiplied by 2x1")
                return Matrix.objects[noun].m3x2_m2x1_matrix()
            elif mtrA == "1x3" and mtrB == "3x3" and noun == "multiplication":
                print("you are about to calculate 1x3 multiplied by 3x3")
                return Matrix.objects[noun].m1x3_m3x3_matrix()
            elif mtrA == "1x3" and mtrB == "3x2" and noun == "multiplication":
                print("you are about to calculate 1x3 multiplied by 3x2")
                return Matrix.objects[noun].m1x3_m3x2_matrix()
            elif mtrA == "1x3" and mtrB == "3x1" and noun == "multiplication":
                print("you are about to calculate 1x3 multiplied by 3x1")
                return Matrix.objects[noun].m1x3_m3x1_matrix()
            elif mtrA == "2x1" and mtrB == "1x2" and noun == "multiplication":
                print("you are about to calculate 2x1 multiplied by 1x2")
                return Matrix.objects[noun].m2x1_m1x2_matrix()
            elif mtrA == "2x1" and mtrB == "1x3" and noun == "multiplication":
                print("you are about to calculate 2x1 multiplied by 1x3")
                return Matrix.objects[noun].m2x1_m1x3_matrix()
            elif mtrA == "1x2" and mtrB == "2x2" and noun == "multiplication":
                print("you are about to calculate 1x2 multiplied by 2x2")
                return Matrix.objects[noun].m1x2_m2x2_matrix()
            elif mtrA == "1x2" and mtrB == "2x3" and noun == "multiplication":
                print("you are about to calculate 1x2 multiplied by 2x3")
                return Matrix.objects[noun].m1x2_m2x3_matrix()
            elif mtrA == "3x1" and mtrB == "1x2" and noun == "multiplication":
                print("you are about to calculate 3x1 multiplied by 1x2")
                return Matrix.objects[noun].m3x1_m1x2_matrix()
            elif mtrA == "3x1" and mtrB == "1x3" and noun == "multiplication":
                print("you are about to calculate 3x1 multiplied by 1x3")
                return Matrix.objects[noun].m3x1_m1x3_matrix()
            elif mtrA == "1x2" and mtrB == "2x1" and noun == "multiplication":
                print("you are about to calculate 1x2 multiplied by 2x1")
                return Matrix.objects[noun].m1x2_m2x1_matrix()
            elif mtrA == "2x2" and mtrB == "2x2" and noun == "multiplication":
                print("you are about to calculate 2x2 multiplied by 2x2")
                return Matrix.objects[noun].m2x2_m2x2_matrix()
            elif mtrA == "2x2" and mtrB == "2x2" and noun == "addition":
                print("you are about to calculate 2x2 added to 2x2")
                return Matrix.objects[noun].am2x2_m2x2_matrix()
            elif mtrA == "3x3" and mtrB == "3x3" and noun == "addition":
                print("you are about to calculate 3x3 added to 3x3")
                return Matrix.objects[noun].am3x3_m3x3_matrix()
            elif mtrA == "3x3" and mtrB == "3x3" and noun == "subtraction":
                print("you are about to calculate 3x3 minus 3x3")
                return Matrix.objects[noun].sm3x3_m3x3_matrix()
            elif mtrA == "2x2" and mtrB == "2x2" and noun == "subtraction":
                print("you are about to calculate 2x2 minus 2x2")
                return Matrix.objects[noun].sm2x2_m2x2_matrix()

        else:
            return "There is no {} here.".format(noun)

    else:
        return "There is no {} here.".format(noun)


def get_input():
    print("Enter The Maths problem you would like to solve!")
    wlist = ["solve", "do", "close"]
    wlist2 = ["equation", "app", "multiplication", "subtraction", "determinant", "scalar", "addition"]
    command = input(": ").split()
    if not command:
        print("enter something valid")
        get_input()
    elif len(command) == 1:
        print("enter something valid")
        get_input()
    elif len(command) == 1 and command[0] not in wlist:
        print("enter something valid")
        get_input()
    elif len(command) >= 3:
        print("enter something valid")
        get_input()
    elif len(command) == 2 and command[0] not in wlist or command[1] not in wlist2:
        print("enter something valid")
        get_input()
    else:
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]

        else:
            print("Unknown Arithmetic{} ".format(verb_word))
            return

        if len(command) >= 2:
            noun_word = command[1]
            print(verb(noun_word))


verb_dict = {
    "solve": solve,
    "close": close,
    "do": do,


}
while True:
    get_input()

