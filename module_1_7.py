grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}

students = sorted(students)
average_mark = [sum(sublist)/len(sublist) for sublist in grades]
stud_mark = dict(zip(students, average_mark))
print(stud_mark)