import math
n0 = float(input('\033[1;30;41mDigite o angulo:\033[m '))
rad = math.radians(n0)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O angulo de {} tem o seno {:.2f}\nO angulo {} tem o cosseno {:.2f}\n O angulo de {} tem a tangente {:.2f}'.format(n0, sen, n0, cos, n0, tan))