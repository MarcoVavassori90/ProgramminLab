my_list = [1,3,5,2,4]

print ("The sum of my_list is", sum(my_list))

def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

print ("The sum of my_list is", sum_of_list(my_list))