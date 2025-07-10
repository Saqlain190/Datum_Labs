import csv,os
class grades():
    def __init__(self, name,id, grade,):
        self.name=name
        self.id = id
        self.grade = grade
    def add_student(self):
        self.name =str(input("Enter the Name of the student:"))
        self.id = int(input("Enter ID of Student: "))
        self.grade = str(input("Enter the Grade of Student: "))

        file_exists=os.path.isfile("students_grades.csv")

        file_empty=not file_exists  or os.stat("students_grades.csv").st_size == 0

        with open("students_grades.csv","a",newline='') as file:

            writer = csv.writer(file)
            if file_empty:
                writer.writerow(['Name','ID','Grade'])
            writer.writerow([self.name,self.id,self.grade])

        print("Record Add Sucessfully")
        

    def update_student_record(self):
        print("Enter the ID of student which record you want to update:")
        self.id = int(input())
        new_rows = []

        with open("students_grades.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
              if row[1]== str(self.id):
                print("Enter New Details")
                self.name = str(input("Enter the Name of the student:"))
                self.id = int(input("Enter ID of Student: "))
                self.grade = str(input("Enter the Grade of Student:"))
                new_rows.append([self.name, self.id, self.grade])
              else:
                new_rows.append(row)

        with open("students_grades.csv",'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("Record Updated Successfully")


    def delete_student_record(self):
        self.id = input("Enter ID of student to delete: ")
        new_rows = []
   
        with open("students_grades.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == self.id:
                        print("Deleting record:", row)
                        deleted = True  
                        continue  
                    new_rows.append(row)  

        with open("students_grades.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        if deleted:
            print("Record deleted successfully!")
        else:
            print("Student ID not found.")

    def display(self):

        with open("students_grades.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

            
    def options(self):
        while True:
         print("Enter your option:")
         n = int(input("1 for Add student \n 2 for Update Students Data \n 3 for Delete student Record \n 4 for Display Record \n 5 Exit \n" ))
         if n==1:
            student.add_student()
         elif n==2:
            student.update_student_record()
         elif n==3:
            student.delete_student_record()
         elif n==4:
            student.display()
         elif n==5:
            print("Exit")
            break


if __name__ == "__main__":
    student = grades("","","")
    student.options()
   
    
