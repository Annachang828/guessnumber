import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字的結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('1-100請猜一個數字:')
	num = int(num)
	if num == r:
		print('Congrats!!!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大拉')
	elif num < r:
		print('比答案小拉')
	print('這是你猜的第', count, '次')