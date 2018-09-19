
import random

def ask_group():
	n = input("What is your question?")
	return n

x = ask_group()
#print(x)

answers = [
           'Reply hazy, try again',
           'Ask again later.',
           'Better not tell you now.',
           'Cannot predict now.',
           'Concentrate and ask again.',
           'Do not count on it.',
           'My reply is no.',
           'My sources say no.',
           'Outlook not so good.',
           'Very doubtful.']
print(random.choice(answers))