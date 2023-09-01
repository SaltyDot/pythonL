print("hello world")
# умови
# v1
# n1 = 10 + 20 * 2  # оператор привласнення, отрабатывает последним
# n2 = 20
# v2
# n1, n2 = 10, 20 + 10  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
#
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
#
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки

# print("hello" in "hello world"
hours= int(input("Enter hours: "))
if hours >= 12:
    print("PM")
else:
    print("AM")