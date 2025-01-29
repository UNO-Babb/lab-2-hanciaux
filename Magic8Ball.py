#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers=["Certainly", "No.", "Couldn't tell you", "I don't know", "Perchance", "Perhaps", "Tossup", "I have zero clue", "Don't count on it", 
         "Why would you ask such a question?", "Without a shadow of a doubt", "My independent sources say no", "I don't know, so quit asking",
         "Could happen", "Ask again later", "Ask someone else"]
  #Answer question randomly with one of the options from your earlier list.
num=random.random() #decimal 0-1
num=num*1000 #number 0-1000
num=int(num) #no decimals
num=num%16 #0-16

question=input("Ask a yes or no question: ")
print(answers[num]) #




if __name__ == '__main__':
  main()
