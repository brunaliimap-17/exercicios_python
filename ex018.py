import math

ang = float(input('Digite o ângulo:'))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('O seno do ângulo {} é {:.2f}'.format(ang, sen))
print('O cosseno do ângulo {} é {:.2f}'.format(ang, cos))
print('A tangente do ângulo {} é {:.2f}'.format(ang, tg))
