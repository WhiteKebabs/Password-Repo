import json
import os

characters = [ \
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "!", "?", "#", "@", ".", "-" \
            ]

def forward(x, key):
    """
    This function uses the key array to decrypt password x
    """

    j = 0
    for i in range(len(x)):

        if j == 4:
            j = 0

        x[i] += in3[j]
        j += 1

        if x[i] >= len(characters):
            x[i] -= len(characters)

    str_arr = [str(characters[char]) for char in x]
    st = "".join(str_arr)

    return st

def backward(x, key):
    """
    This function uses the key array to encrypt password x
    """

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

update = False # Flag for updating existing entry
data = {}

# Check if the passwords file exists and open it
if os.path.exists("p.txt"):
    with open("p.txt" , encoding="utf-8") as file:
        data = json.load(file)
else:
    update = True

in1 = input().strip() # Read first input

# If the first input is 'view', display all account names stored
if in1 == "view":
    print("\nnames:")
    for key in data.keys():
        name = [characters[int(i)] for i in key.split()]
        print("".join(name))
    print()
    exit()

in2 = input().strip() # Read second input

# If the second input is 'update',
if in2 == "update":
    update = True
    in2 = input().strip()
in3 = []

# Slightly modify the PIN
for i in range(len(in2)):
    if int(in2[i]) < len(in1):
        in3.append( int(in2[i]) + characters.index(in1[int(in2[i])]) )
    else:
        in3.append( int(in2[i]) + characters.index(in1[ int(in2[i]) % len(in1) ]) )

# Convert account name to key for comparison
key_arr = [str(characters.index(i)) for i in in1]
key = " ".join(key_arr)

# Print details if key exists and is not for update
if not update and key in data:
    print("\n" + forward(data[key][0], in3) + "\n" + forward(data[key][1], in3) + "\n")

else:

    in6 = input().strip() # Prompt username
    in4 = input().strip() # Prompt password
    in5 = input().strip() # Prompt password confirmation

    # Check if the two passwords match
    if in4 != in5:
        exit()

    data[key] = [backward(in6, in3), backward(in4, in3)]

    with open("p.txt", 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
