# Alphabet pattern
# Eg. no of lines = 4
# Output
#   A
#   A   B
#   A   B   C
#   A   B   C   D

n = input("Enter no of lines : ")
for i in range(1, int(n)+1):
    for j in range(65, 65+int(i)):
        print("  ", chr(j), end="")
        # chr() takes an integer and return character wrt it's ascii
    print()
