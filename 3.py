n = int(input("Задайте ограничение: "))
num = 0
proc = " процент"

while num <= n:
	skl = num % 10
	if skl == 0 or (skl >= 5 and skl <= 9):
		print(str(num) + proc + "ов")
	elif skl == 1:
		print(str(num) + proc)
	elif skl >= 2 and skl <= 4:
		print(str(num) + proc + "а")
	num += 1
input()
