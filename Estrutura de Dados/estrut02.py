print ('uso do if')
peso = float (input ('Digite seu peso: '))
altura = float (input ('Digite seu peso: '))
IMC = peso/ (altura**2)

if IMC < 19:
    print('abaixo do peso')
elif IMC >= 19 and IMC <26:
    print('peso ideal')
else:
    print('acima do peso')

