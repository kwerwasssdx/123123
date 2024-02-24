x0 = int(input())
y0 = int(input())
if  (abs(x0-4)<=2 and abs(y0-2)<=3):
    st1 = 'yes'
else:st1='no'
if 1 <= (x0 - 1) ** 2 + y0 ** 2 <= 4:
    st2='yes'
else:st2='no'
print(st1, st2)