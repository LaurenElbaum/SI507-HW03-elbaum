import random

def ask_group():
	n = input("What is your question?")
	return n

x = ask_group()
#print(x)

answers = ['It is certain.',
           'It is decidedly so.',
           'Without a doubt.',
           'Yes - definitely.',
           'You may rely on it.',
           'As I see it, yes.',
           'Most likely.',
           'Outlook good.',
           'Yes.',
           'Signs point to yes.']
print(random.choice(answers))
