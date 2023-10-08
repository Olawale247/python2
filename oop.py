from abc import  ABC, abstractmethod


class Book(ABC):
    title="things fall apart"
    def __init__(self, page_number, color):
         self.page_number=page_number
         self.color=color

    def move(self):
         print("i am moving")

    @abstractmethod
    def set_title(self, new_title):
         

         pass 

class Calculatorblueprint(ABC):
    def __init__(self, num1,num2) -> None:
         self.num1=num1
         self.num2=num2
     
    @abstractmethod
    def addition(self):
         pass
    
    @abstractmethod
    def sum(self):
         pass 
    @abstractmethod
    def __str__(self):
         return f"book object with the color: {self.color}"
    

class Caculator(Calculatorblueprint):

     def sum(self):
          print("yes i know i must create  my implementation")

     def addition(self):
          return super().num1 + super().num2
     
     def __str__(self):
          return f"testing"
     
cul=Caculator(5,9)
cul.sum()
     

class Product:
     quantity=50
     def __init__(self, name, description) -> None:
          self.name=name
          self.description=description
          self._price=400

     def discount_price(self, reduce_price):
          discount_price=self._price - reduce_price
          return discount_price
     

     def get_price(self):
          return self._price
     
     @classmethod
     def buy_product(cls , qty):
         new_quantity = cls.quantity - qty 
         return new_quantity
     

p1=Product("item one " , "food item")
print(p1.get_price())
p2=Product("item two","some item")
            



# obj=Book(200, "black")
# # print(obj)
# obj2=Book(300, "green")
# obj3=Book(400, "red")
# obj.move()
# # print(obj2.page_number)
# # print(obj.color)


# # class Exercise:
# #       book = 'things fall apart'
# #       def __init__(self, identity, level) -> None:
# #            self.identity =identity
# #            self.level = level 
# #       def __str__(self) -> str:
# #             return f'the greater they fall, {self.name}'
      
# # exe= Exercise ('things fall apart', 'black man', 500)


# class Car:
#     def __init__(self ,model, color,year) -> None:
#          self.model= model
#          self.color=color
#          self.year=year

#     def summary(self):
#          return f"this is meant for the rich, the {self.model}, built in the year "
    


# class Book:
#      def __init__(self, serial_number, color ) -> None:
#           self.serial_number= serial_number
#           self.color=color

class Human:
     def __init__(self, name, age) -> None:
          self.name=name
          self.age=age


     def Walk(self):
           print("i can walk as human")


     def run(self):
           print("i can run fast like a man")


class Student(Human):
     
      def __init__(self, name, age, school_name, course) -> None:
           self.school_name=school_name
           self.course= course
           super().__init__(name,age) 


      def go_to_school(self):
           print("i go to school everyday except weekends")
     
      #overriding that in the parent class 
      def run(self):
           print("yeah i can run very fast")
     
      #super function
      def run(self):
           super().run()
           print("an extra task to run")

      @staticmethod
      def exam():
           print("i am writing exam today")

      def __str__(self) -> str:
           return self.name 
     
     

std=(Student("john", 24,"univelcity", "backend development"))
std2=(Student("mike", 19, "univelcity", "frontend development"))


class Shape:
     def __init__(self, no_of_sides) -> None:
           self.n= no_of_sides
           self.sides=[0 for i in range (no_of_sides)]

     def inputsides(self):
           self.sides = [float(input("enter sides "+str(i+1)+":")) for i in range (self.n)]

      # method to display the length of each side of the polygon
     def dispsides(self):
           for i in range (self.n):
                print("side", i+1, "is",self.sides[i])


class Triangle(Shape):
      def __init__(self) -> None:
          Shape.__init__(self,3)

      def findarea(self):
           a, b, c= self.sides

           # cacaulate the semi_perimeter
           s= (a + b + c) / 2
           return s  
     

# Triangle=Triangle() 
# Triangle.dispsides()
# Triangle.inputsides()

class Animal:
     def __init__(self ,wild, domestic ) -> None:
          self.wild= wild
          self.domestic= domestic 

     def bite(self):
          print("animal can bite and it is poisonious")

     def scary(self):
          print("animal looks are scary")

class Mammal:
     def __init__(self, birth_type) -> None:
          self.birth_type= birth_type
          
class Aquatic:
     def __init__(self, mode_of_living) -> None:
          self.mode_of_living= mode_of_living

     def swim(self):
          print("aquatic animal can swim")

     def dive(self):
          print("aquatic animal can dive")

class Fish(Animal,Aquatic):
     def __init__(self, wild, domestic,  mode_of_living) -> None:
          super().__init__(wild,domestic)
          Aquatic.__init__(self,mode_of_living)

     def Swim(self):
          print("fishes have tails to swim")
          
          
class Birds(Animal):
     def __init__(self,wild,domestic, flying) -> None:
          self.flying=flying
          super().__init__(wild,domestic)

     def wings(self):
          print("birds have wings to fly")
 
diff_ani=Birds("owl","hdhd", "parrot")
diff_ani2=Fish("catfish","dryfish" ,"hg")

# diff_ani.wings()
# diff_ani2.Swim()

class Course:
     def __init__(self, name) -> None:
          self.name=name
          
class Student(Human, Course): #multiple
     def __init__(self, name, leg, age,school_name) -> None:
          self.school_name=school_name 
          super().__init__(leg, age)
          Course.__init__(self, name)

class Rabbit(Animal, Mammal):
     def __init__(self, wild, domestic, birth_type) -> None:
          super().__init__(wild, domestic)
          Mammal.__init__(self, birth_type)

     def dig_hole(self):
          print("rabbit dig holes for living")

rat1= Rabbit("black", "big_head", "alive")
# rat1.bite()
# print(rat1.birth_type)

fis1=Fish("food","eat", "whale")
# fis1.swim()
# print(fis1.domestic)




class Dog:
     def __init__(self,name,age) -> None:
          self.name=name
          self.age=age

     def make_sounds(self):
          ("dogs barks")

class cat:
     def __init__(self,name) -> None:
          self.name=name

     def make_sounds(self):
          print("cat meow")

class Lion:
     def __init__(self, age) -> None:
          self.ade=age
     
     def make_sounds(self):
          print("lion roars")

liol1=Lion(1)
cat1=cat("jessica")
dog1=Dog("jack", 1)
# liol1.make_sounds()
# cat1.make_sounds()

class A:
     def __init__(self, n) -> None:
          self.n=n

     def __add__(self,obj):
          return True
     
     def __sub__(self):
          pass
     
     def __gt__(self, obj):
          return self.n > obj.n

     def __lt__(self,obj):
          return self.n < obj.n 


# example 2 for operator overloading

class Complex:
     def __init__(self, num1, num2) -> None:
          self.num1=num1
          self.num2=num2

     def  __add__(self, others):
          return self.num1 + others.num1, self.num2 + others.num2

     def __sub__(self, others):
          print("i am performing sub")           
     
     def __gt__(self, others):
          if(self.num1 > others.num1):
               return True 
          else:
               return False
          



numb1=Complex(10, 8)
numb2=Complex(14, 9)
print(numb1 + numb2)
print(numb1 - numb2)



     
obj1=A(4)
obj2=A(5)
print(obj1 + obj2)
print(obj1 > obj1)


