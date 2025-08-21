# try :
#     10 + score
# except:
#     raise ValueError('Invalid scores')


# hours = []

# try:
#     average = sum(hours) / len(hours)
# except:
#     average = 0 

# print(average)

# try:
#     login(user)
# except:
#     print('user not known. Please try again')


# age = 1000
# try:
#     adult_years = age -18
# except:
#     raise TypeError('Input is not a number')
# else:
#     if adult_years > 150:
#         raise ValueError('Age is too large')


# if not age >=0 : 
#     raise ValueError('age cannot be negative')


# print "hello"

# if cost > 10:
# print('Expensiveeeee!!!!!!!!!')
# import statistics as sts

# score = [4,4,3,6,7,3,1,2,5,6]

# mean = sts.mean(score)
# print(f'Mean score is {mean}')


# import math

# value = round(math.pi,2)

# print(f'the value of pi is {value}')
# print(f'the square root of 16 is {math.sqrt(16)}')

# age = 17
# has_premit = True 
# is_insured =True

# and operator will only allow us to execute when both the codition is true
# if age > 16 and has_premit:
#     print('Can drive')

# print('Not eligible')    

# and operator will skip the code is 1 or more code block is false
# if age > 18 and has_premit == True:
#     print('Can drive')

# print('Not eligible')    

# if age > 16 and has_premit and is_insured:
#     print('can drive')
# else:
#     print('not eligible')


# class Car:
#     wheels = 4
#     doors = 4

#     def start_engine(self):
#         print('Vrooomm!!')

# my_car = Car()
# print(my_car.wheels)
# my_car.start_engine()