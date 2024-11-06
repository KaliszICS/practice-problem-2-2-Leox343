'''
lesson 2.2
created by leo xu
last edited on oct 15
'''
def q1(): 
  #Write Assignment code here
  ans1 = input("Input an integer: ")
  if int(ans1) == 5: 
    print("The number is Five")
  else:
    print("The number is not Five")
def q2(): 
  #Write Assignment code here
  ans2 = input("Input a number: ")
  if float(ans2) < 1: 
    print("Negative")
  else:
    print("Positive")
def q3():
  #Write Assignment code here
  ans3 = input("Input an integer: ")
  num = int(ans3) % 2
  if num == 0:
    print("Even")
  else:
    print("Odd")
def q4():
  #Write Assignment code here
  ans4 = input('Type "Hello": ')
  if ans4 == "Hello":
    print("The word is Hello")
  else:
    print("The word is not Hello")
  
#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
# q4()