# #course: Object-oriented programming, year 2, semester 1
# #academic year: 2020-21
# #author: B. Schoen-Phelan
# #date: 02-10-2020
# #purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: ", message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        print(1,"First character is " + message[0])
        print("Last character is " + message [-1])


        # use slice notation:
        print(2, "Slice notation position " + message[2:])
        print("Slice notation position " + message[:3])
        print("Slice notation position " + message[:])


        # escaping a character:
        print(3, "Mary\'s \"always right\"!")
        print("He said \"that\'s fantastic\"!")


        # find all a's in the input word and count how many there are:
        print(4, "This is a string. How many a\'s in tha string".count('a'))
        print("How many a\'s in the message? " + str(message.count('a')))

        #from lab solution
        lower_message = message.lower()
        print(5, "all lower characters: " + lower_message)
        print("The first occurence of a is at position: " + str(lower_message.find('a')))
        print("There are " + str(lower_message.count('a')) + " a's in the word.")
        print("Total character count is: " + str(len(lower_message)))



        # replace all occurences of the character a with the - sign
        print(6, message.replace('a', '_'))
        print(message.replace('y', '*'))
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        
        
        
        def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 1: hand the input string to a list and print it out:
        # Every word had an index location from the list when it is split
        #With "Hello World" Hello is index 0 in the list and World is index 1
        my_list = (list(message.split(" ")))
        print(1, my_list)


        # 2: append a new element to the list and print:
        # append allows you to add a new word to the list
        #the new word is added to the end of the list
        my_list.append("People")
        print(2, my_list)


        # 3: remove from the list in 3 ways:
        #.pop() will remove hello world from the list and leaves the word people in place
        print(3, my_list.pop())
        #doesn't seem to work
        # print(my_list.remove("People"))
        # 4: removes people from the list
        del my_list[-1:-2]
        print(4, my_list)


        # 5: check if the word cake is in your input list:
        #boolean operation
        print(5, 'cake' in my_list)


        # 6: reverse the items in the list and print:
        my_list.reverse()
        print(6, my_list)


        # reverse the list with the slicing trick:
        my_list.reverse()
        print(7, my_list[::-1])


        # print the list 3 times by using multiplication:
        print(8, my_list*3)



tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()
