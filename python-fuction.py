# def print_hello(name):
#     print(f"hello {name}")



# def  get_sqt(num:int):
#     return num*num


# print_hello("henry")
# print_hello("john")
# print_hello("mike")
# print(get_sqt(5))
# print(get_sqt(7))
# print(get_sqt(11))

def add_num(a:int, b:int)-> int:
    return a + b

add=lambda a, b: a + b

print(add(12, 6))



def multi_num(a:int, b:int):
    return a*b

# print(add_num(5,8))
# print(add_num(10,9))

# def even_checker(num):
#     if  num  % 2 == 0:  
#        return True
#     return False
# print(even_checker(6))

# def get_nums(*args):
#     total=0
#     for a in args:
#         total += a
#     return total 

# def set_student(**kwargs):
#     print(kwargs)


# set_student(first_name="henry", last_name="john", age=19)
# set_student(first_name="henry", last_name="peter")
# set_student(first_name="henry")


# print(get_nums(3,5,6,7,8,8,9))

# def funct (x,y):
#     return x/y 

# print(funct(y=2, x=4))


# def smallest_in_list(nums:list):
#     smallest = nums[0]
#     for i in nums:
#         if i  < smallest:
#             smallest=i
#     return smallest
#     pass 


# number=[6,4,7,8,9,12]
# min=smallest_in_list(number)
# print(min)


# def outter_function():
#     print("i am an outter fuction")
#     def secret_fun():
#         print("i am a secret function")
#     secret_fun()



# outter_function()

# def registred_student():
#     list=[]
#     # input('what is your name :') This is how to use a prompt 
#     name= input('Enter name :')
#     list.append(name)
#     print(list)

# registred_student()


# def remove_name(name_list , name):
#     for a in name_list:
#         if a ==name:
#             new_result=name_list.remove(name)
#             return name
#         else:
#             return "name not found"
#     return new_result    

# list_of_names=['alice', 'john', 'mike', 'james']

# list_of_name2=['sandra', 'lucky', 'joy', 'peter']
# #calling the remove_name function 
# print(remove_name(list_of_names, 'alice'))


# def name_rep(list_name):
#     name=input('what is your name?:')
#     for a in list_name:
#         if a ==name:
#             return "name is already taken"
#             break 
#         else:
#             list_name.append(name)
#             break
#     name=input("enter your name :")

    
    
# list_of_names=['alice', 'john', 'mike', 'james']

# list_of_name2=['sandra', 'lucky', 'joy', 'peter']
# #calling the remove_name function 
# print(remove_name(list_of_name2, 'joy'))
# name_rep (list_of_names)


# def outter_function():
#     print("i am an outer function")
#     def secret_fun():
#         price=20.05
#         return price
#     val=secret_fun()
#     print(val)

# outter_function()

# def maxprocessed_payment(n):
#     def processed_payment():
#         newprocessed_payment=[]
#         new_list=newprocessed_payment.append(n)
#         return new_list
#     processed_payment()

# print(maxprocessed_payment(20))


# def calc_num(n):
#     def add_num(y):
#         return n + y
#     return add_num

# sum=calc_num(10)
# print(sum(20))

# def c_number(m):
#     def d_num(n):
#         return m - n
#     return d_num

# div=c_number(10)
# print(div(20))

# def c_percentage(num , percentage):
#     value= int(num / 100 * percentage)
#     return value 

# print(c_percentage(10000 , 5))



# def payment(amount:int):
#     if amount <= 0:
#         print("the amount you provided is not acceptable")
    

# def caculate(fun,n, m):
#     re = fun(n,m)
#     return re 


# val= caculate(add_num,5,8)
# val2= caculate(multi_num,7,9)
# print(val)
# print(val2)


# def add_message(func):
#     def wrapper():
#         print("this is my extra message")
#         func()
#         print("okay im done")
#     return wrapper

# @add_message
# def hell_world():
#     welcome="welcome to univelcity"
#     return print(welcome)

# print(hell_world())


# def divide(a,b):
#     return a/b 

# res=divide(-2, 10)




# def improved_division(func):
#     def wrapper(a,b):
#         if a == 0:
#              print('sorry you cant not divide zero numbers')
#         else:
#             val=func(a,b)  
#         return wrapper

# @improved_division
# def divide(a,b):
#     return a/b

# res=divide(0/10)

# print(res)

# def prevent_faliure(func):
#     def inner_func(m, n):
#         if not isinstance (m, int) and  isinstance(n, int):
#            print("sorry only integer are allowed")
#            return
#         else:
#             val=func(m, n)
#             return val
#     return inner_func 


def enter_names(name):
    name_list=[]
    name_list.append(name)
    return name_list

print (enter_names("charles"))

res = lambda x: x * 2
print(res(5))

def mult_num(a, b):
    return a * b

mult=lambda a, b: a * b

print(mult(12, 3))

#recursion examples
def reduceby2(num):
    if num <= 0:
        print('i am finished operation')#base point
        return
    else:
        count: []
        for i in range (0, num):
             count +=''
        print(num,' ' .join(count))
        reduceby2(num - 2)

reduceby2(8)

def factorial(x):
    if x == 1:
       return 1
    else:
        return x * factorial(x - 1)
    

def multiplication(num1, num2):
    if num1 == 0 or num2 ==0:
        return 0
    else:
        return num1 + multiplication(num1, num2 -1)
    
print(multiplication(3, 3))
val=factorial(6)
print(val)
#def even_checker (num:int):



       