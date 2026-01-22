def get_average_grade(scores):
    thresholds = [59, 62, 66, 69, 72, 76, 79, 82, 86, 89, 92, 96, 100]
    grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
    average_score = int(sum(scores) / len(scores))

    for i in range(len(thresholds)):
        if average_score <= thresholds[i]:
            return grades[i]

# print(get_average_grade([92, 91, 90, 94, 89, 93]))
# print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))
# print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))
# print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))
# print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]))
# print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))