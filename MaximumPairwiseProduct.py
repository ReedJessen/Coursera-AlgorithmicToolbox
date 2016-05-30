# Uses python3


n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


result = 0


first_biggest = sorted(a)[-1]
second_biggest = sorted(a)[-2]


result = first_biggest * second_biggest

print(result)
