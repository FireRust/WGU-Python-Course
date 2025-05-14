student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 199, 65, 86]
high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)