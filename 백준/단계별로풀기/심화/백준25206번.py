rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
rating_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
total = 0
subjectsum = 0

for i in range(20) :
    sub, score, grade = input().split()
    if grade == 'P' :
        pass
    else :
        total += score
        subjectsum += score * rating_score[rating.index(grade)]

print('%.6f' % (subjectsum/total))