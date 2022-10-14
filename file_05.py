tomeg:int = int(input('Hány Kg vagy? '))
magassag:float = int(input('Háyn cm magas vagy? ')) / 100

tti = tomeg / (magassag ** 2)
print(f'testtömegindexed: {round(tti, 2)}')
print('Testsúlyosztály:', end=' ')
if   tti < 16:   print('súlyos soványság')
elif tti < 17:   print('mérsékelt soványság')
elif tti < 18.5: print('enyhe soványság')
elif tti < 25:   print('normális testsúly')
elif tti < 30:   print('túlsúlyos')
elif tti < 35:   print('I. fokú elhízás')
elif tti < 40:   print('II. fokú elhízás')
else:            print('III. fokú (súlyos) elhízás')
