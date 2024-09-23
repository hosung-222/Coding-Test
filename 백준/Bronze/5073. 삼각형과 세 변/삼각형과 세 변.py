a, b, c = map(int, input().split())
while a != 0 and b != 0 and c != 0:
    data = [a, b, c]
    data.sort()
    if data[0] + data[1] <= data[2]:
        print("Invalid")
    elif data[0] == data[1] == data[2]:
        print("Equilateral")
    elif data[0] == data[1] or data[1] == data[2] or data[0] == data[2]:
        print("Isosceles")
    else:
        print("Scalene")

    a, b, c = map(int, input().split())    