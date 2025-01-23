def oligotm(a, c, g, t):
    if a + c + g + t <= 13:
        tm = 2*(a + t) + 4*(c + g)
    else:
        tm = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
    return tm

print(oligotm(1, 2, 4, 6))
print(oligotm(9, 1, 8, 2))
