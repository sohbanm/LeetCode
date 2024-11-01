def twinStrings(a, b):
    res = []

    for i in range(len(a)):
        odd_a = set()
        even_a = set()
        odd_b = set()
        even_b = set()

        if len(a[i]) == len(b[i]):
            odd_a = set(a[i][1::2])
            even_a = set(a[i][::2])
            odd_b = set(b[i][1::2])
            even_b = set(b[i][::2])
        else:
            res.append("No")
        
        if odd_a == odd_b and even_a == even_b:
            res.append("Yes")
        else:
            res.append("No")
            
    return res

a = ['abcd','abcd']
b = ['cbad','adbc']

print(twinStrings(a, b))