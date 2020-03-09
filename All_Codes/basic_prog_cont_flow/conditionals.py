

if Player.health <= 0:
    print('You have lost, please restart and try again.')
else:
    action = input('Please enter your next action:')

if Student.grade >= 90:
    if Student.grade <= 94:
        Student.letterGrade = "A-"
    elif Student.grade <=97:
        Student.letterGrade = "A"
    else:
        Student.letterGrade = "A+"  


if Student.grade >= 70:
    if Student.grade <= 74:
        Student.letterGrade = "C-"
        if Student.average <=75:
            if Student.warningCount >= 2:
                print(Student.name + ' requires a 3rd strike warning')
    elif Student.grade <=77:
        Student.letterGrade = "C"
    else:
        Student.letterGrade = "C+"        


