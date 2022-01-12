import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


def load_report_cards(directory, num_students):
    report_cards = []

    for student_number in range(num_students):
        report_card = load_report_card(directory, student_number)
        report_cards.append(report_card)

    return report_cards


def add_student_averages(report_cards, subjects):
    for report_card in report_cards:
        sum_of_marks = 0

        for key, value in report_card.items():
            if key not in subjects:
                continue

            sum_of_marks += value

        average = sum_of_marks / len(subjects)
        # add a new key to the report card with the average
        report_card["average"] = average


def get_average_student_grade(report_cards):
    sum_of_averages = 0

    for report_card in report_cards:
        sum_of_averages += report_card["average"]

    return sum_of_averages / len(report_cards)


def get_subject_averages(report_cards, subjects):
    subject_averages = {subject: 0 for subject in subjects}

    for report_card in report_cards:
        for subject in subjects:
            mark = report_card[subject]
            subject_averages[subject] += mark

    for subject in subjects:
        subject_averages[subject] /= len(report_cards)

    return subject_averages


def get_grade_level_averages(report_cards):
    grade_level_averages = {grade: [] for grade in range(1, 9)}

    for report_card in report_cards:
        grade = report_card["grade"]
        average = report_card["average"]

        grade_level_averages[grade].append(average)

    for grade in grade_level_averages:
        grade_level_averages[grade] = sum(
            grade_level_averages[grade]) / len(grade_level_averages[grade])

    return grade_level_averages


report_cards = load_report_cards("students", NUM_STUDENTS)
add_student_averages(report_cards, SUBJECTS)

average_student_grade = round(get_average_student_grade(report_cards), 2)

subject_averages = get_subject_averages(report_cards, SUBJECTS)
sorted_subject_averages = sorted(subject_averages.items(), key=lambda x: x[1])
hardest_subject = sorted_subject_averages[0][0]
easiest_subject = sorted_subject_averages[-1][0]

grade_level_averages = get_grade_level_averages(report_cards)
sorted_grade_level_averages = sorted(
    grade_level_averages.items(), key=lambda x: x[1])
best_grade_level = sorted_grade_level_averages[-1][0]
worst_grade_level = sorted_grade_level_averages[0][0]

students_sorted_by_grade = sorted(report_cards, key=lambda x: x['average'])
best_student = students_sorted_by_grade[-1]["id"]
worst_student = students_sorted_by_grade[0]["id"]

print("Average Student Grade:", average_student_grade)
print("Hardest Subject:", hardest_subject)
print("Easiest Subject:", easiest_subject)
print("Best Performing Grade:", best_grade_level)
print("Worst Performing Grade:", worst_grade_level)
print("Best Student ID:", best_student)
print("Worst Student ID:", worst_student)
