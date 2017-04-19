from cdiagrams.bitstrap import Bitstrap

forged = True

strap = Bitstrap(920, 70)
bits = []
if not forged:
    bits.extend(["00", "01"])
    bits.extend(["FF"] * 360)
    bits.extend(["00", "14"])
else:
    bits.extend(["00", "01"])
    bits.extend(["FF"] * 3)
    bits.extend(["00", "14"])

h = "925a89b43f3caff507db0a86d20a2428007f10b6" # sha1 hash of 'hi mom'
for i in range(0, 40, 2):
    bits.append(h[i:i+2])

if forged:
    #bits.extend(["00"] * 357)
    bits.extend(["FF"] * 357)

strap.draw_strap(bits)
strap.save("../img/bleichenbacher_signature.png")


