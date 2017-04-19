from cdiagrams.table import Table

table = Table(800, 100)
cols = 2
texts = ['take random x from X', 'calculate y = F(pk, x)', 'calculate k = H(x)',
         'encrypt m using symmetric encryption and key k', 'output (y, c)']
table.draw_table(cols, texts)
table.save("trapdoor_encrypt.png")


table = Table(800, 100)
cols = 2
texts = ['', 'calculate x from y: x = F^(-1)(sk, y)', 'calculate k = H(x)',
         'decrypt m using symmetric encryption and key k', 'output m']
table.draw_table(cols, texts)
table.save("../img/trapdoor_decrypt.png")