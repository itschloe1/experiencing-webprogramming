

#    과제 2 - 회사 조직도 만들기

class Person():

    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class AccompanyPerson(Person):
    position = "대리"

accompany_person = AccompanyPerson("chloe", "30", "female")
print(accompany_person.name)
print(accompany_person.age)
print(accompany_person.position)

#고급
class PersonNew(Person):
    def __init__(self, name, age, sex, position):
        Person.__init__(self, name, age, sex)
        self.position = position

person_new = PersonNew("chloe","30","female","assistant")
print(person_new.name)
print(person_new.age)
print(person_new.sex)
print(person_new.position)
