x = 0
y = 0
z = 0

for i in range(int(input())):
    xi, yi, zi = map(int, input().split())
    x += xi
    y += yi
    z += zi

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")