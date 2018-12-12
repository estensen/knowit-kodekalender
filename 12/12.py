emojis = '😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎'

ascii_emojis = [] 
lowest = ord(emojis[0])

for emoji in emojis:
    ascii_int = ord(emoji) 
    ascii_emojis.append(ascii_int)
    if ascii_int < lowest:
        lowest = ascii_int

# Assume that there is a space char in the sentance and that we have to shift each emoji to ASCII 
ascii_space = 32
diff = lowest - ascii_space

for i in range(len(ascii_emojis)):
    ascii_int = ascii_emojis[i] - diff
    ascii_emojis[i] = chr(ascii_int)


print(''.join(ascii_emojis))

