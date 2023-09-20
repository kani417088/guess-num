import random
r = random.randint(1, 100)

while True:
	number = input('請輸入一個數字:')
	number = int(number)
	if number == r:
		print('猜對了!')
		break
	elif number > r:
		print('比答案大喔')
	else:
		print('比答案小喔')