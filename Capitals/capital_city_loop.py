from Capitals import capitals_dict
import random

capital_list = list(capitals_dict.keys())
randomIndex = random.randint(0,len(capital_list))
randomState = capital_list[randomIndex]
print("Whats the capital of "+ randomState + "? " )
answer = str(input())

while answer.lower() != capitals_dict.get(randomState).lower() and answer.lower() != "exit":
	answer = str(input())

if answer.lower() != "exit":
	print ("That's correct!")
else:
	print ("Good bye")

#
# random.shuffle(capital_list)
# print(capital_list)
#
# for i in capitals_dict:
# 	print(i,capitals_dict[i])


#print("Whats the capital of " + capitals_dict.pop() + "?" )
#
# answer = input()
# if answer.lower() == capitals_dict[randomindex]
#
