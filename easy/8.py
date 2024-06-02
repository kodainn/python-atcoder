a, b = input().split()

concat = a + b
concat_num = int(a + b)

if((concat_num**0.5).is_integer()):
    print("Yes")
else:
    print("No")