names=['Ana','John','Denise','Katy']
grade=['B','A+','A','A']
course=[2.00,6.0001,20.002,9.01]

def get_grade(student,name_list,grade_list,course_list):
    i=name_list.index(student)
    grade=grade_list[i]
    course=course_list[i]
    return (grade,course)

studentGrade,studentCourse=get_grade('Denise',names,grade,course)
print(studentGrade,studentCourse)

