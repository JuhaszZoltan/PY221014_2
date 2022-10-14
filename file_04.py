fogy = float(input('mennyit fogyaszt az autó 100 Km-en? '))
ar = int(input('mennyibe kerül egy liter benzin? '))
ut = int(input('hány Km az út? '))
utas = int(input('hányan vagytok? '))

print(f'az útiköltség: {fogy / 100 * ar * ut / utas} HUF/fő')