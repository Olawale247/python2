from functools import reduce
# i=0
# while i < 6:
#     print(f"i am the {i} iteration")
#     i+=1

# total=0
# num=int(input("enter a number"))
# while num !=0:
#         total +=num
#         num=int(input("enter your number: "))

# for a in range(10):
#     print(a+2)

fruits=["apple", "orange", "watermelon", "cashew","pineapple"]
new_list=[]
for fruit in fruits:
      conv=(fruit.upper())
      new_list.append(conv)

print(new_list)

number=[3,5,6,7,9,4,2]
# even_list=[ a*2 for a in number if a % 2==0]
# mul_list=[ i*2 for i in number]
# print(even_list)
# print(mul_list)
iterator_init=iter(number)
print(next(iterator_init))
print(next(iterator_init))
print(next(iterator_init))
print(next(iterator_init))
print(next(iterator_init))
print(next(iterator_init))
# name="charles"
# char_list= [letter for letter in name]
# print(char_list)

def PowTwo(max=0):
      n = 0
      while n < max:
            yield 2 ** n
            n +=1

def get_sqt_uptp(n):
      for a in range(n):
            yield a

sqt=PowTwo(5)
sq_num=get_sqt_uptp(4)
print(next(sq_num))
print(next(sq_num))
print(list(sq_num))
# print(next(sqt))
# print(next(sqt))
# print(next(sqt))
# print(list(sqt))
# for i in list (sqt):
#       print(i)


my_pets=['alfred','tabith', 'willaim','arla']
uppered_pets=list(map(str.upper,  my_pets))
print(uppered_pets)

def mult(n:int) -> int:
      return 2**n

student_score=[45,60,72,58,81,68,75]
def A_student(score):
      return score > 70

numb = [3,5,6,7,8,9]




def sum(a,b):
      return a + b

total_sum=reduce (sum, numb)
print(total_sum)