import random

r = random.randint(1, 100)
while True:
	num = input('1-100請猜一個數字:')
	num = int(num)
	if num == r:
		print('Congrats!!!')
		break
	elif num > r:
		print('比答案大拉')
	elif num < r:
		print('比答案小拉')