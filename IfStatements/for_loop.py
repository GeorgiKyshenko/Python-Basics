def solve(number):
    var = 0
    for x in range(1, number):
        if number % x == 0:
            var += x
    if var == number:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    n = int(input())
    out = solve(n)
    print(out)
    