import random
com =  random.choice(['棒子','老虎','雞','蟲'])
while True:
	player = input ('棒打老虎雞吃蟲，請出拳：')
	if player != '棒子' and player != '老虎' and player != '雞' and player != '蟲':
		print ('請輸入 棒子/老虎/雞/蟲 唷')
		continue
	else:
		break
print ('我出的是', com)
if player == com or (player == '棒子' and com == '雞') or (player == '老虎' and com == '蟲') or ( player == '雞' and com == '棒子') or ( player == '蟲' and com == '老虎'):
	print ('平手!')
elif (player == '棒子' and com == '老虎') or (player == '老虎' and com == '雞') or ( player == '雞' and com == '蟲') or ( player == '蟲' and com == '棒子'):
	print ('恭喜你贏啦!')
else:
	print ('真可惜~再接再厲吧!')