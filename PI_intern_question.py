# finds prime numbers
def prime_finder(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    if num == 1:
        return False
    return True


# to see the pyramid
def print_list(array2d):
    for i in range(0, len(array2d)):
        for j in range(0, i + 1):
            print(array2d[i][j], end=" ")
        print()


# changes the value of the prime numbers -100000 to make the calculation not pick any path with prime numbers
def prime_number_destroyer(array2d):
    for i in range(0, len(tri_num)):
        for j in range(0, i + 1):
            if prime_finder(int(array2d[i][j])):
                array2d[i][j] = -100000
    return array2d


# takes the input as it is
tri2 = """215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233"""

tri = """1
8 4
2 6 9
8 5 9 3"""

# divide input into chunks
rows = tri.split("\n")
tri_num = list()
for row in rows:
    nums = row.split(" ")
    tri_num.append(nums)

# turn the chunks into integers
for i in range(0, len(tri_num)):
    for j in range(0, i + 1):
        tri_num[i][j] = int(tri_num[i][j])

# make all the prime numbers -100000
prime_number_destroyer(tri_num)

#print_list(tri_num)

# start from bottom, pick maximum of the 2 values and sum them with upper number
for i in range(len(tri_num) - 1, -1, -1):
    for j in range(0, i):
        tri_num[i - 1][j] += max(tri_num[i][j], tri_num[i][j + 1])

print("Total sum is: " + str(tri_num[0][0]))

#print_list(tri_num)
