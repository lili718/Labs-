from fraction import Fraction
def harmonic(n):
    out = Fraction(0,1)
    while n > 0:
        out += Fraction(1,n)
        n -= 1
    return out
def two(n):
    out = Fraction(0,1)
    while n > -1:
        out += Fraction(1,2) ** n
        n -= 1
    return out
def zero(n):
    return Fraction(2,1) - two(n)
def partialRiemannZeta(n, b):
    out = Fraction(0,1)
    while n > 0:
        out += Fraction(1,n) ** b
        n -= 1
    return out
if __name__ == '__main__':
    print('Welcome to Fun with Fractions!')
    while True:
        try:
            inp = int(input('Enter Number of iterations (integer>0):'))
            if inp <= 0:
                raise ValueError('Please input an integer > 0.')
            break
        except:
            pass
    print('H(',inp,')=',harmonic(inp),sep = '')
    print('H(',inp,')~=',harmonic(inp).approximate(),sep = '')
    print('T(',inp,')=',two(inp),sep = '')
    print('T(',inp,')~=',two(inp).approximate(),sep = '')
    print('Z(',inp,')=',zero(inp),sep = '')
    print('Z(',inp,')~=',zero(inp).approximate(),sep = '')
    b = 2
    while b < 9:
        print('R(',inp,',',b,')=',partialRiemannZeta(inp,b),sep = '')
        print('R(',inp,',',b,')~=%.8f' % (partialRiemannZeta(inp,b).approximate()),sep = '')
        b += 1
    
            
            