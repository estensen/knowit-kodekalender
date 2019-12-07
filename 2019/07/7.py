for y in range(2, 27644437):
    b = y * 7
    if b % 27644437 == 1:
        print((5897 * y) % 27644437)
        break

