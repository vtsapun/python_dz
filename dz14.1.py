class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} лет, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f', Зачетная книжка: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupFullException()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Номер группы: {self.number}\n{all_students}'

class GroupFullException(Exception):
    def __init__(self, message="Група вже має максимальну кількість студентів (10)."):
        self.message = message
        super().__init__(self.message)

# Приклад використання:

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'Bill', 'Gates', 'AN146')
st4 = Student('Female', 22, 'Emma', 'Watson', 'AN147')
st5 = Student('Male', 26, 'Mark', 'Zuckerberg', 'AN148')
st6 = Student('Female', 24, 'Adele', 'Adkins', 'AN149')
st7 = Student('Male', 29, 'Jeff', 'Bezos', 'AN150')
st8 = Student('Female', 27, 'Taylor', 'Swift', 'AN151')
st9 = Student('Male', 25, 'Elon', 'Musk', 'AN152')
st10 = Student('Female', 23, 'Shakira', 'Mebarak', 'AN153')
st11 = Student('Male', 31, 'Leonardo', 'DiCaprio', 'AN154')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except GroupFullException as e:
    print(e)

print(gr)
