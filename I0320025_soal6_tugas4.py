x = 4       # 4 = 0000 0100
y = 11      # 11= 0000 1011

z = x | y   # 15= 0000 1111
print("nilai z:",z,", binary :",format(z,'08b'))

z = x >> 2  # 1 = 0000 0001
print("nilai z:",z,", binary :", format(z,'08b'))

z = x ^ y   # 15= 0000 1111
print("nilai z:",z,', binary :',format(z,'08b'))

z = ~x      # -5=-0000 0101
print("nilai z:",z,", binary :",format(z,'08b'))

z = 11 & 4  # 0 = 0000 0000
print("nilai z:",z,", binary :",format(z,'08b'))