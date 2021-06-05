n = int(input())
L = []
for i in range(n):
    name = input()
    score = float(input())
    L.append([name, score])
sorted_scores = sorted(list(set([x[1] for x in L])))
second_lowest = sorted_scores[1]
final_list = []
for student in L:
    if second_lowest == student[1]:
        final_list.append(student[0])
for student in sorted(final_list):
    print(student)









