import math
A, B, H, M = map(int,input().split())

x1 = B*math.cos(math.radians(450 - 6*M))     # 分針(0π基準)
y1 = B*math.sin(math.radians(450 - 6*M))

x2 = A*math.cos(math.radians(450 - 30*H - (M / 2)))
y2 = A*math.sin(math.radians(450 - 30*H - (M / 2)))

print(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))