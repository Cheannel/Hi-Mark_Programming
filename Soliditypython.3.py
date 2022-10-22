+# A program that show the scheme of admission of students
# student should input the scores of their four main jamb subjects

# ASSIGNMENT BY LUGHAS IMMACULATA .C
English = eval(input('Enter your score: '))
Maths = eval(input('Enter your score: '))
Subject3 = eval(input('Enter your score: '))
Subject4 = eval(input('Enter your score: '))
aggregate = (English+Maths+Subject3+Subject4)/4
print('The aggregate of the scores you entered is', aggregate)
if aggregate >= 80:
    print('Your department of eligibility: Department of Medicine, and Law')
elif aggregate == 79 and aggregate >= 75:
    print('Your department of eligibility: Department of Banking and Finance, Insurance, and Accountancy')
elif aggregate == 74 and aggregate >= 71:
    print('Your department of eligibility: Department of Pharmacy, Physiology, Pharmacology, and Nursing')
elif aggregate == 70 and aggregate >= 61:
    print('Your department of eligibility: Department of Computer Science, Psychology, and Statistics')
elif aggregate == 60 and aggregate >= 55:
    print('Your department of eligibility: Department of Botany, and Zoology')
elif aggregate == 54 and aggregate >= 50:
    print('Your department of eligibility: Department of Agric Science')
else:
    print('No admission')

