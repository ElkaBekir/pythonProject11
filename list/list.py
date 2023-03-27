bool('')

bool('asd')

bool(123)
bool(0)



with_vowels = "This is so much fun!"

''.join(char for char in with_vowels if char not in "aeiou")

''.join(["cool", "dude"])

nested_list = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
for i in nested_list:
    for val in i:
         print(val)



coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for loc in coords:
    for coord in loc:
        print(loc)


board = [[num for num in range(1,4)] for val in range(1,4)]

print(board)

board = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(board)