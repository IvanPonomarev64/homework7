class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = []
        
        

    def evaluation_of_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_for_student(self, student):
        if isinstance(student, Student):   
            for i in student.grades.values():
                student.average_rating += i

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum(self.average_rating) / len(self.average_rating)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'                    
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = []

    def average_grade_for_lectures(self, lecturer):
        if isinstance(lecturer, Lecturer):   
            for i in lecturer.grades.values():
                lecturer.average_rating += i    
                    
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(self.average_rating) / len(self.average_rating)}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Студенты
some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
some_student_1 = Student('Ivan', 'Ponomarev', 'male')
some_student_1.courses_in_progress += ['Python']

# Ревьюеры
some_reviewer = Reviewer('Some', 'Buddy')

# Выставление оценок студентам
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.8)
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Git', 9.9)
some_reviewer.rate_hw(some_student_1, 'Python', 10)
some_reviewer.rate_hw(some_student_1, 'Python', 10)

# Лекторы
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_lecturer_1 = Lecturer('Vendi', 'Darling')
some_lecturer_1.courses_attached += ['Python']

# Выставление оценок лекторам
some_student.evaluation_of_lecturers(some_lecturer, 'Python', 10)
some_student.evaluation_of_lecturers(some_lecturer, 'Python', 9.8)
some_student.evaluation_of_lecturers(some_lecturer, 'Python', 9.9)
some_student.evaluation_of_lecturers(some_lecturer, 'Git', 10)
some_student.evaluation_of_lecturers(some_lecturer, 'Git', 9.9)
some_student.evaluation_of_lecturers(some_lecturer_1, 'Python', 10)
some_student.evaluation_of_lecturers(some_lecturer_1, 'Python', 10)

# Подсчет средней оценки лекторам
some_lecturer.average_grade_for_lectures(some_lecturer)
some_lecturer_1.average_grade_for_lectures(some_lecturer_1)

# Подсчет средней оценки студентам
some_student.average_grade_for_student(some_student)

print(some_reviewer)
print(f'\n{some_lecturer}')
print(f'\n{some_student}')
print(f'\n{some_lecturer_1.average_rating > some_lecturer.average_rating}')
print(f'\n{some_student.average_rating < some_student_1.average_rating}')