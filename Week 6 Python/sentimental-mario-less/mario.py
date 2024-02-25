# TODO
# Loop to request a number for the height of the half-pyramid
while True:
    heigth = input("Enter the heigth (from 1 to 8):")
    if heigth.isdigit():
        heigth = int(heigth)
        if heigth >= 1 and heigth <= 8:
            break
    print("Enter an integer between 1 and 8")

# Loop to request the numbers for the half-pyramid lines
for i in range(heigth):
    spaces = heigth - i - 1
    hashes = i + 1
    line = " " * spaces + "#" * hashes
    print(line)