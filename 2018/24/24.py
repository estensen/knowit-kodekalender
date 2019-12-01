msg = 'GODJULOGGODTNYTTÅR'

col_vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

col_num = 0
for i, c in enumerate(msg):
    col_num = col_num * 29 + (col_vals.index(c) + 1) 
    
print(col_num)

