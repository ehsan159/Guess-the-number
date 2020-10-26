#we gonna know what is best first chiose for win in this game

import random
import xlwt
import xlrd
from xlwt import  Workbook

work_ex = Workbook()
sheet1=work_ex.add_sheet('sheet me')
list1=['game 1', 'game 2', 'game 3', 'game 4', 'game 5']
list2=['try 1', 'try 2', 'try 3', 'try 4', 'try 5']
sheet1.write(0, 6, 'Solution')
sheet1.write(0, 7, 'Result')

j=0
for i in range(1, 6):
    sheet1.write(i, 0, list1[j] )
    sheet1.write(0, i, list2[j])
    j=j+1

for t in range(5):
    solution= random.randint(1, 100)
    items = list(range(10)) # I mean this to represent any kind of iterable.
    limit = 5 #nubmer of try you can do
    sheet1.write(t+1, 6, solution)

    num = []
    index = 1
    for item in items:
        a = int(input('input an integer number between 1 to 100 : '))
        num.append(a)
        if a<solution:
            print('guess greater number')
        if a>solution:
            print('guess smaller number')

        print("you can try just {} time(s)".format(limit-(item+1)))
        sheet1.write(t+1, item+1, num[item])
        if num[item]==solution:
            sheet1.write(t+1, 7, "Win")
        if len(num)==4 and num[-1] != solution:
            sheet1.write(t+1, 7, "Lose")
        if a==solution:
            print("Yeah you're right, the number is {}".format(solution))
            break
        if index == limit:
            print("Sorry, Game over, the number is {}".format(solution))
            break

        index += 1

work_ex.save('data2w.xls')


