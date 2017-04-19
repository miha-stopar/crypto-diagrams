from cdiagrams.table import Table

table = Table(800, 132)
cols = 3
texts = ['2*7 = 14 = 1*11+3  ', 'odd => upper half', 'min = max - (max-min)/2 = 11 - (11-0)/2 = 6, max = 11',
         '4*7 = 28 = 2*11+6', 'even => lower half', 'min = 6, max = min + (max-min)/2 = 6 + (11-6)/2 = 8',
         '8*7 = 56 = 5*11+1', 'odd => upper half', 'min = max - (max-min)/2 = 8 - (8-6)/2 = 7, max = 8',
         '16*7 = 112 = 10*11+2', 'even => lower half', 'min = 7, max = min + (max-min)/2 = 7 + (8-7)/2 = 7' ]

table.draw_table(cols, texts)
table.save("../img/rsa_parity.png")
