from math import pi

r:int = int(input('kör sugarának hossza (cm): '))

print(f'a kör kerülete: {round(2 * r * pi, 4)} cm')
print(f'a kör területe: {round(r ** 2 * pi, 4)} cm^2')