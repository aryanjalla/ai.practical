def f(s):
    s.sort()
    if len(s)>3:
        a = s[0]+s[-1]+min(2*s[1],s[0]+s[-2])
        return a + f(s[:-2])
    else:
        return sum(s[len(s)==2:])
lst = []
n = int(input("Enter number of people crossing the bridge : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("Total timetaken would be ")
print(f(lst))