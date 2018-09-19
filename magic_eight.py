def ask_group():
	n = input("What is your question?")
	while n != "quit":

		if n.endswith('?'):
			print("Great!") 
		else:    
			print("I’m sorry, I can only answer questions.")

		n = input("What is your question?")	

	

x = ask_group()
#print(x)


"""
if input("What is your question?").endswith('?'):
    print("Great!") 
else:    
    print("I’m sorry, I can only answer questions.")
"""