# {key:  value    for vars in  iterable }
# {num:  num*num  for num  in  range(1,11) }

# item price in dollers
old_price = {'Milk':1.02,'Coffie':2.5,'Bread':2.5}

doller_to_pound = 0.76
new_price = {item: value*doller_to_pound for (item, value) in old_price.items()}
print(new_price)

# Here, we can the retrieved the item price in doller and converted them to pounds. Using dictionary comprehension
# makes this task much simpler and shorter.
