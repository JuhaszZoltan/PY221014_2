a:int = int(input('derékszögű 3szög egyik befogójának hossza (cm): '))
b:int = int(input('derékszögű 3szög másik befogójának hossza (cm): '))

if a > 0 and b > 0:
    c:float = (a ** 2 + b ** 2) ** .5
    print(f'átfogó hossza: {round(c, 2)} cm')
else:
    print('ez nem lehet egy derékszögű 3szög két befogója...')