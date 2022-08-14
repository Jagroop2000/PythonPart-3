def highest_even(list):
    highest =0
    for item  in  list:
        if item%2==0:
            if highest < item:
                highest = item
    
    return highest


print(highest_even([10,2,3,4,8,11,12]))
  