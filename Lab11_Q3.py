class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        r = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            if i < len(self.coefficients):
                t1= self.coefficients[i]
            else:
                t1=0
            if i < len(other.coefficients):
                t2= other.coefficients[i]
            else:
                t2 = 0
            r.append(t1+t2)
        return Polynomial(r)
    
    def __mul__(self,other):
        r = [0]*(len(self.coefficients)+len(other.coefficients))
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                r[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(r)
    
    def __str__(self):
        terms = []
        for i , coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0 :
                    terms.append(str(coeff))
                elif i ==1:
                    terms.append(f'{coeff}x')
                else:
                    terms.append(f'{coeff}x^{i}')
        if not terms:
            return '0'
        
        return ' + '.join(terms[::-1])
    
    # Get coefficients from the user for a polynomial
def get_coeff():
    coeff = []
    degree = int(input("Enter the degree of the polynomial: "))
    for i in range(0,degree+1,1):
        coef = int(input(f"Enter the coefficient for x^{i}: "))
        coeff.append(coef)
    return coeff
    
print('What should we do?')
print('1. Add two Polynomials')
print('2. Multiply Two Polynomials')
print('3. Display a Polynomial')

a = int(input('Choose from (1-3): '))
if a==1:
    l=[]
    for i in range(2):
        c= get_coeff()
        l.append(c)
    p1= Polynomial(l[0])
    p2 = Polynomial(l[1])
    r= p1 + p2

    print('After addition, we get polynomial: ',r)

elif a==2:
    l=[]
    for i in range(2):
        c= get_coeff()
        l.append(c)
    p1= Polynomial(l[0])
    p2 = Polynomial(l[1])

    print('The product is : ', p1*p2)

elif a==3:
    c = get_coeff()
    print(Polynomial(c))

else:
    print('INVALID INPUT !!!')










