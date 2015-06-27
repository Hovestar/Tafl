#6 colors
import random

def check(guess,end):
	dlt = []
	end2 = end[:]
	black = 0
	for i in range(4):
		if guess[i]==end2[i]:
			black+=1
			dlt.append(i)
	for i in dlt[::-1]:
		del end2[i]
		del guess[i]
	white = 0
	for i in guess:
		if i in end2:
			white+=1
			del end2[end2.index(i)]
	return white,black



def play():
	colors = 6
	goal = [random.randrange(colors) for i in range(4)]
	guess = input('What is your guess? ')
	rounds = 1
	while guess!=goal:
		white,black = check(guess,goal)
		print('White: '+str(white)+'\nBlack: '+str(black))
		guess = input('What is your guess? ')
		rounds += 1
		
	print("It took "+str(rounds)+" rounds.")

def compareAll(end):
	for guess in [i,j,k,l for i in range(6) for j in range(6) for k in range(6) for l in range(6)]:
		

""""
----
b---
w---
bb--
bw--
ww--
bbb-
bbw-
bww-
www-
bbbb
~~~~
bbww
bwww
wwww
"""
