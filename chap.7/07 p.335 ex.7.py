def student_list():
    infile = open('students.txt', 'r')
    s_list=[]
    for line in infile:
        s_list.append(line)
    infile.close()

student_list()