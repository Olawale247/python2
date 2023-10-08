names=['john','mike','peter','lucky']
student=['sandra', 19, True, 2.50]
cohort=[['backend', 6, 'henry'], '6b5', 'class c',['frontend', 12, 'francis']]
print(names[0])
print(names[-1])
print(names[0:2])
print(cohort[0][0])
print(cohort[0][2])
student[0]="james"
# print(student)
# print(len(names))
# small=['james', 'glory']
# print(names + small)
# print(small * 2)
# print('john' in names)

names.append('andrew')
names.insert(1, 'sandra')
# print(names.pop())
# print(names)
new_names=names.copy()
new_names.append('henry')
print(new_names)
print(names)
names.remove('peter')
names.sort()
print(names.index('mike'))
names.reverse()
print(names)


b4=[60, 45, 70, 50]
b5=[25, 65, 40, 71]
print(b4 + b5)

#join these list together to form a single list

student=[['john',19, 'john@gmail.com', ['backend', 'frontend']], 'henry', ['6b5', '6b4' '6b3']]
print(student[0][3][1])
print(student[2][1])
print(student[0][2])

#from the above list retrieve the following
#frontend
#6b4
#john email

#write a program that prompt a user to provide their name and add the name to a list of name 
# 
 
# number_tuple=(2,3,4,5,6,7)
# print(type(number_tuple))
# print(number_tuple[0]) # retrieve an item from tuple with their index
# print(number_tuple[0:3]) # slicing a subset of the tuple 
# if 3 in number_tuple:
#     print(True)
# else:
#     print(False)
# second=(3,4,5)
# print(number_tuple + second)
# number_tuple.count()

# number_set={3,4,5,6,7,8,9}
# new_num={2,8}
# seond_number={3,4,5,6,7,8}
# number_set.add(10)
# number_set.update(new_num)
# set3=number_set.intersection(seond_number)
# set4=number_set.union(second)
# number_set.remove(5)
# val=number_set 
# print(set3)
# print(set4)
# print(number_set.pop())
# print(number_set.pop())
# print(number_set.pop())
# # print(number_set)
# print(number_set)
# print(val)

# dictionary example
student={
    'name' :'john',
    'age' : '20',
    'email' : 'john@gmail.com',
    "has_paid" : 'True',
    "address" :{
         'no':42,
        'street':'montgomary',
         'city':'Lagos',
         'country': 'nigeria'
   },
   "courses":['frontend', 'backend']
}
print(student['name'])
print(student['address']['street'])
student['name']='james'
print(student)
del student['address']
print(student.get('phone'))

dict_value=student.values()
dict_keys=student.keys()
student.update({'email': "james@gmail.com"})
student.update({"phone": "08102899699"})
student.pop('courses')
print(student)
print(dict_value)
print(dict_keys)

names=['john','mike','peter','lucky']
# is_authenticated=False
name=input("enter your name: ")
if name in names:
   print(f"welcome to dashboard{name}")
else:
    print("you are not a registerd user")


high_scores=[70,71,72,73]
average_score=[50,51,52,53,]
number=int(input("enter your score : "))

if number >= 70:
    new_highscore=high_scores.append(number)
    print(f"congratulations you passed")

elif number > 50 and number < 70 :
    average_scoreboard=average_score.append(number)
    print("congratulation  you got an average mark")
else:
    print("poor score try again later ")
    print(average_score)

