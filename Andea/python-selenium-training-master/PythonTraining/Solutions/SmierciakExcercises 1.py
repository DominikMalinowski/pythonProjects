import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
import Chapter6

Chapter1.Chapter1()
Chapter1.Chapter1Extra()
Chapter2.Chapter2()
print(Chapter3.Chapter3(15,5,5,"123456789qwertyuiopasdfghjklzxcvbn"))
try:
    print(Chapter4.Chapter4(['Green', 'White', 'Black', 'Pink', 'Yellow']))
except Exception as error:
    print(error)
try:
    print(Chapter4.Chapter4(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
except Exception as error:
    print(error)
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
newdict = Chapter5.Chapter5(dic1, dic2)
newdict = Chapter5.Chapter5(newdict, dic3)
print(newdict)
try:
    print(Chapter6.Chapter6("Red;Green;White;Black;Pink;Yellow"))
except Exception as error:
    print(error)
try:
    print(Chapter6.Chapter6("Black;Pink;Yellow"))
except Exception as error:
    print(error)


