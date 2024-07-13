
qsnLst = [
    '''1. Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom''', '''2. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned
''', '''3. Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p''', '''4. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted
'''
]
AnsList = ['c', 'b', 'c', 'a']
priceLst = [1000, 2000, 3000, 4000]
gainPrice = 0
print("Welcome to KBC")
print("Let's start the game")
a = input("press 'S' for Start  and Q for Quit: ")
if(a == 'S' or a == 's'):
  print("you have to answer 4 questions\n")
  print("if you answer all the questions correctly you will win the game\n\n")
  # print("Your first question is for ₹1000 ")
  # print(qsnLst[0])
  # ans1=input("Enter your answer(a/b/c/d) : ")
  # if(ans1 == AnsList[0]):
  #   print("Right Answer You win ₹1000 rupees " )
  # else:
  #   print("Wrong Answer ! Better luck next time" )
  for i in range(0, len(qsnLst)):
    print("Your question is for ₹",priceLst[i])
    print(qsnLst[i])
    ans1 = input("Enter your answer(a/b/c/d) : ")
    if (ans1 == AnsList[i]):
      print("\nRight Answer You win ₹", priceLst[i], "rupees \n\n")
      gainPrice= gainPrice+priceLst[i]
    else:
      print("\nWrong Answer ! Better luck next time\n\n")
      gainPrice = gainPrice+0
      # print(qsnLst[i])
      # ans1 = input("Enter your answer(a/b/c/d) : ")
      # if (ans1 == AnsList[i]):
      #   print("\nRight Answer You win ₹", priceLst[i], "rupees ")
      # else:
      #   print("\nWrong Answer ! Better luck next time")
  print("Your total winning price is ₹", gainPrice)
  print("Thanks for playing")

elif(a == 'Q' or a == 'q'):
 print("You sucessfully Quit")

else:
  print("Wrong Input")