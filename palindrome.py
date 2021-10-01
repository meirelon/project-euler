import math

def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))


# with while loop
i=999
j=999
count=0
palindrome_max = 0
while True:
    if i*999 < palindrome_max:
        break
    count+=1
    res = i*j
    palindrome = res == rev(res)
    j-=1
    if j<100:
        i-=1
        j=i
    if i<100:
        break

    if palindrome and res>palindrome_max:
        palindrome_max = res
    else:
        continue

print(count, palindrome_max)
