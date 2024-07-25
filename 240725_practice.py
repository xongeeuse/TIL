# class Animal:
#     count = 0

#     def __init__(self, species):
#         self.species = species
#         Animal.count += 1

#     @classmethod
#     def number_of_Animal(cls):
#         print(f'동물은 총 {cls.count}마리입니다.')

# cat1 = Animal('cat')
# dog1 = Animal('dog')
# cow1 = Animal('cow')

# Animal.number_of_Animal()
# dog1.number_of_Animal()

# # class Cat(Animal):




# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __str__(self):
        return '나는 동물이야.'
    


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

    def __str__(self):
        return '나는 강아지야.'



class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    
    # 클래스매서드
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

    # 인스턴스매서드
    # def access_num_of_animal(self):
    #     return f'동물의 수는 {self.num_of_animal}마리입니다.'

# 클래스매서드로 호출
dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

# 인스턴스매서드로 호출
# dogcat = Pet()
# print(dogcat.access_num_of_animal())

print(dog)
print(cat)