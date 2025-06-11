import random #py module
import my_module

#module: each module is responsible for a diff task

# print(random.randint(4, 6))

# print(my_module.my_fav_number)

random_no = random.random() #module, function
# 0 <= number < 1 (semi open range)
print(random_no)

#extending the range
random_no_10 = random.random() * 10
print(random_no_10)

#random float
ran_uniform = random.uniform(1,10) #a <= number <=b


