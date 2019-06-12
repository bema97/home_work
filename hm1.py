
#Make sure to un-comment the function line below when you are done.
#Remember to name your function is_even()
def is_even(x):
    return x % 2 == 0

#DO NOT remove lines below here,
#this is designed to test your code.

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(8) == True
  assert is_even(100) == True
  assert is_even(101) == False
  print("YOUR CODE IS CORRECT!")

test_is_even()