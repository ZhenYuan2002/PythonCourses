#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tommy', 12)
cat2 = Cat('Mary', 3)
cat3 = Cat('David', 16)

# 2 Create a function that finds the oldest cat

def oldest_cat(*age):
    return max(age)

x = oldest_cat(cat1.age, cat2.age, cat3.age)
print(f'The oldest cat is {x} years old')


#WITHOUT OOP
#age = 0
#if cat1.age > cat2.age and cat1.age > cat3.age:
#    age = cat1.age
#elif cat2.age > cat1.age and cat2.age > cat3.age:
#    age = cat2.age
#elif cat3.age > cat1.age and cat3.age > cat2.age:
#    age = cat3.age
#x = age
#print(f'The oldest cat is {x} years old')



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2