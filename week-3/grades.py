def printGrades( grades ):
    students = len( grades ) # number of students
    exams = len( grades[ 0 ] ) # number of exams
    # print table headers
    print ("The list is:")
    print (" ", end='')

    for i in range( exams ):
        print ("[%d]" % i, end='')

    print()
    # print scores, by row
    for i in range( students ):
        print ("grades[%d]" % i, end='')

        for j in range( exams ):
            print (grades[ i ][ j ], "",end='')
        print()

# main program
grades = [ [ 77, 68, 86, 73 ], [ 96, 87, 89, 81 ], [ 70, 90, 86, 81 ] ]

printGrades( grades )

print ("\n")
