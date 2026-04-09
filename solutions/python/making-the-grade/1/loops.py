def round_scores(student_scores):
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    step = (highest - 40) // 4
    return [41, 41 + step, 41 + 2 * step, 41 + 3 * step]


def student_ranking(student_scores, student_names):
    return [
        f"{i}. {name}: {score}"
        for i, (name, score) in enumerate(zip(student_names, student_scores), start=1)
    ]


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []