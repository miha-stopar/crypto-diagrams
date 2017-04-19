from cdiagrams.table import Table

table = Table(1100, 160)
cols = 3
texts = ['gcd(new_a, new_b)', 'new_a and new_b expressed with a and b', 'x, y coefficients for new_a and new_b',
         '76, 32', '76 * 1 + 32 * 0,    76 * 0 + 32 * 1', '(1, 0), (0, 1)',
         '32, 12', '76 * 0 + 32 * 1,    76 * 1 + 32 * (-2)', '(0, 1), (1, -2)',
         '12, 8', '76 * 1 + 32 * (-2),    32 * 1 - 12 * 2 = \n32 * 1 - (76 * 1 + 32 * (-2)) * 2', '(1,-2), (,)']

texts = ['gcd(new_a, new_b)', 'new_a and new_b expressed with a and b', 'x, y coefficients for new_a and new_b',
         '32, 12', '32 * 1 + 12 * 0,    32 * 0 + 12 * 1', '(1, 0), (0, 1)',
         '12, 8', '32 * 0 + 12 * 1,    32 * 1 + 12 * (-2)', '(0, 1), (1, -2)',
         '8, 4', '32 * 1 + 12 * (-2),    12 - 8 * 1 = 12 * 1 - (32 * 1 + 12 * (-2)) * 1 = 32 * (-1) + 12 * 3', '(1, -2), (-1, 3)',
         '4, 0', '32 * (-1) + 12 * 3, -', '(-1,3), -'
         ]
table.draw_table(cols, texts)
table.save("../img/extended_euclid.png")
