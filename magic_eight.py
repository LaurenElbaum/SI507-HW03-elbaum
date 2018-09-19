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
<<<<<<< HEAD
           'Signs point to yes.',
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
=======
           'Signs point to yes.']
>>>>>>> add_questionsB
print(random.choice(answers))
