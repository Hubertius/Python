"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""
choice = input("Write a string containing multiple words: ")
result = choice.split()
#print(choice)
#print(result)
result = result[::-1]
result_string = ' '.join(result)
print(result_string)


