# Open files as bytes objects
with open("p1", "rb") as p1_file:
    p1 = p1_file.read()
with open("c1", "rb") as c1_file:
    c1 = c1_file.read()
with open("c2", "rb") as c2_file:
    c2 = c2_file.read()

# Here is some code to help you xor these bytes objects
# output = bytes(x ^ y for x, y in zip(text1, text2))
