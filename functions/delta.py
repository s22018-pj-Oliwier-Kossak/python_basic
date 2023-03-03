a = int(input("enter the factor a: "))
b = int(input("enter the factor b: "))
c = int(input("enter the factor c: "))

def QuadraticEquation(a,b,c):
    delta = b**2 -4*a*c


    if a == 0:
            print('no solutions')
    elif delta < 0:
        print('no solutions')
    elif delta == 0:
        x1 = -b/2*a
        return x1
    elif delta > 0:
        x1 = (-b - delta**(1/2))/(2*a)
        x2 = (-b + delta ** (1 / 2)) / (2 * a)
        print(x1,x2)

print(QuadraticEquation(a,b,c))
