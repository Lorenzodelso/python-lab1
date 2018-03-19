string = input("Input the string: ")

if len(string) < 2:
    print ("")
    exit(1)

res = string[:2] + string[-2:]
print(res)