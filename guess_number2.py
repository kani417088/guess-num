import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	number = input('請輸入一個數字:')
	number = int(number)
	if number == r:
		print('猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif number > r:
		print('比答案大喔')
	else:
		print('比答案小喔')
	print('這是你猜的第', count, '次')