class Solver:
    def __init__(self, a, b, c): #method used to initialize attributes of class
        self.a = a
        self.b = b
        self.c = c

    def m_solver(self):
        m_result = (self.c + self.b)/(self.a) #solves monomial algebraically by adding b to c and dividing by a
        return m_result

    def p_solver(self, a, b,c):
        p_result = (self.c**2-self.b)/self.a #solves polynomial agebraically by subtracting b from c squard and dividing by a
        return p_result

num_input = input("Enter values for a, b, and c in ax-b=c: ").split() #user input for values a, b and c
num1, num2, num3 = map(float, num_input) #changes values into floats

solve = Solver(num1,num2,num3) #initialize instance of class
calcmono=solve.m_solver() #instance of class uses m_solver method
print("For ax-b=c, x=" + str(calcmono)) #displays answer for monomial

calcpoly=solve.p_solver(num1,num2,num3) #instance of class uses p_solver method
print("For (ax+b)^1/2=c, x=" +str(calcpoly)) #displays answer for polynomial