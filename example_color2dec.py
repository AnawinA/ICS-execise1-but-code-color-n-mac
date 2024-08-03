from color_n_dec import dec2color, color2dec
from mac_n_bin import mac2bin, bin2mac

## Exercise 01 
# 4. pixel [R, G, B]
a = "#A132EC"
print("a:", color2dec(a))

b = "59c1ad"
print("b:", color2dec(b))

c = [1, 240, 132]
print("c:", dec2color(c))

# 5. MAC Address
print()

d0 = "15:a4:c7:ff:39:82"
print("d0:", mac2bin(d0))
print("d0:", bin2mac(mac2bin(d0)))

print()

d = "B2:CC:16:00:88:41"
print("d:", mac2bin(d))
e = "100101110010110010000011110110011111001111010010"
print("e:", bin2mac(e))