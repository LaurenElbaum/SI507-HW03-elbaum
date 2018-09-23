import random

 answers = ['It is certain.',
           'It is decidedly so.',
           'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
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
           'Very doubtful.',
           'Signs point to yes.']

def ask_group():
  n = input("What is your question?")
  while n != "quit":
    
    if n.endswith('?'):
      print(random.choice(answers))
    else:    
      print("I’m sorry, I can only answer questions.")
    
    n = input("What is your question?") 
  
 x = ask_group()
