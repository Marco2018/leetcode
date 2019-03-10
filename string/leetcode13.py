def romanToInt(s):
    sym=['I','V','X','L','C','D','M']
    num=[1,5,10,50,100,500,1000]
    n=len(s)
    i=number=0
    while i<n:
        if i<n-1 and sym.index(s[i])<sym.index(s[i+1]):
            number=number+num[sym.index(s[i+1])]-num[sym.index(s[i])]
            i = i + 2
        else:
            number = number + num[sym.index(s[i])]
            i = i + 1
    return number

s="MCMXCIV"
print(romanToInt(s))