# l = ["a", "b", "c", "d", 89, 90, 91]
# l[3] = "t"
# print(l)
#
# tup = ("t", "m", "j", "d", 89, 90, 91)
# print(tup)
#
# st = set[("a", "Jan", "c", "March", 89, 90, 91)]
# st.add("t")
# print(st)
#
# dic = {
#     1: "Jan",
#     2: "Feb",
#     3: "March",
# }
# print(dic)
# n = int(input())
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 < n < 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 < n < 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")str(a) + " - " + str(b) + " ==> " + a - b + "\n"

# a = int(input())
# b = int(input())
#
# print(
#     str(a) + " + " + str(b) + " ==> " + str(a + b) + "\n" +
#     str(a) + " - " + str(b) + " ==> " + str(a - b) + "\n" +
#     str(a) + " * " + str(b) + " ==> " + str(a * b) + "\n"
# )

# def is_leap(year):
#     return
#
#
n = int(input())

for i in range(1, n+1):
    if i <= n:
        print(i, end="")
    else:
        print("")
