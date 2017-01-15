import json
import os

characters = [ \
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "!", "?", "#", "@", ".", "-" \
            ]

def forward(x, key):
    j = 0
    for i in range(len(x)):

        if j == 4:
            j = 0

        x[i] += in3[j]
        j += 1

        if x[i] >= len(characters):
            x[i] -= len(characters)

    str = ""

    for char in x:
        str += characters[char]

    return str

def backward(x, key):
    out = []
    j = 0
    for i in range(len(x)):

        if j == 4:
            j = 0

        out.append( int(characters.index(x[i])) - in3[j] )
        j += 1

        if out[i] < 0:
            out[i] += len(characters)
    return out

update = False
data = {}

if os.path.exists("p.txt"):
    with open("p.txt" , encoding="utf-8") as file:
        data = json.load(file)
else:
    update = True

in1 = input().strip()
if in1 == "view":
    print("\nnames:")
    for key in data.keys():
        name = ""
        x = key.split()
        for i in x:
            name += characters[int(i)]
        print(name)
    print()
    exit()

in2 = input().strip()
if in2 == "update":
    update = True
    in2 = input().strip()
in3 = []

if len(in2) != 4:
    exit()

for i in range(4):
    if int(in2[i]) < len(in1):
        in3.append( int(in2[i]) + characters.index(in1[int(in2[i])]) )

    else:
        in3.append( int(in2[i]) + characters.index(in1[ int(in2[i]) % len(in1) ]) )

key = str(characters.index(in1[0]))
for i in range(1, len(in1)):
    key += " "
    key += str(characters.index(in1[i]))

if not update and key in data:

    print("\n" + forward(data[key][0], in3))
    print(forward(data[key][1], in3), "\n")

else:

    in6 = input().strip()
    in4 = input().strip()
    in5 = input().strip()

    if in4 != in5:
        exit()

    data[key] = [backward(in6, in3), backward(in4, in3)]

    with open("p.txt", 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
