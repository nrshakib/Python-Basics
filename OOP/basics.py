class Student:
    roll = ''
    gpa = ''

    def setValue(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f'Roll: {self.roll},GPA:{self.gpa}')


Shakib = Student()
Shakib.setValue(75,3.11)
Shakib.display()

Rijvi = Student()
Rijvi.setValue(10,3.99)
Rijvi.display()