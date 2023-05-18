#Desenvolva um programa que receba como entrada do usuário as medidas de três lados de
#um triângulo. O programa deverá retornar como saída qual o tipo do triângulo, de acordo com
#as regras:
#• Triângulo Equilátero possui os três lados com as mesmas medidas.
#• Triângulo Escaleno possui os três lados diferentes
#• Triângulo Isósceles possui dois lados iguais
#Deve-se ainda verificar se as medidas formam um triângulo. Três medidas formam um triângulo
#quando a soma de dois lados for maior do que um terceiro lado.



lado_1 = int(input('informe o lado do triangulo1:'))
lado_2 = int(input('informe o lado do triangulo2:'))
lado_3 = int(input('informe o lado do triangulo3:'))

if (lado_1 + lado_2 > lado_3) and \
    (lado_1 + lado_3 > lado_2) and \
    (lado_2 + lado_3 > lado_1):
    print('Os lados formam um triangulo')
    if (lado_1 == lado_2) and (lado_2 == lado_3):
        print('Triangulo equilatero!')
    elif(lado_1 != lado_2) and (lado_1 != lado_3) and (lado_2 != lado_3):
        print('Triangulo escaleno!:')
    else:
        print('Triangulo isósceles!:')




else:
    print('Os lados não formam um triangulo')




