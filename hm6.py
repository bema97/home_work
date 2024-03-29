
#Make sure to un-comment the function line below when you are done.
#Remember to name your function correctly.
def bigger_guy(x, y):
    return max(x,y)

#DO NOT remove lines below here,
#this is designed to test your code.
def test_bigger_guy():
  assert bigger_guy(1, 2) == 2
  assert bigger_guy(10, 20) == 20
  assert bigger_guy(20, 10) == 20
  assert bigger_guy(10, 10) == 10
  assert bigger_guy(2, 1) == 2
  assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
  print("YOUR CODE IS CORRECT!")
test_bigger_guy()