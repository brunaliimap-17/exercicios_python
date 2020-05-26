import math

CatOp = float(input('Comprimento do Cateto Oposto:'))
CatAdj = float(input('Comprimento do Cateto adjacente:'))

hi =math.hypot(CatOp, CatAdj)


#hi = (CatOp ** 2 + CatAdj ** 2 ) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))
