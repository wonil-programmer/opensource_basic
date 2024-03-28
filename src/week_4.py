STUDENT_NUM = 5

# 입력 함수
def get_input():
    # 딕셔너리에 학생의 정보 저장
    student = {}
    student["학번"] = input("학번: ")
    student["이름"] = input("이름: ")
    student["영어"] = int(input("영어: "))
    student["C-언어"] = int(input("C-언어: "))
    student["파이썬"] = int(input("파이썬: "))
    return student

# 총점 및 평균 계산 함수
def calculate_total_average(student):
    total = student["영어"] + student["C-언어"] + student["파이썬"]
    average = total / 3
    
    return total, average


# 학점 계산 함수
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C+"
    elif average >= 40:
        return "C"
    else:
        return "F"


# 등수 계산 함수
def calculate_rank(students):
    sorted_students = sorted(students, key=lambda x: x["총점"], reverse=True)
    for i, student in enumerate(sorted_students):
        # 학생 정보 딕셔너리에 등수 추가
        student["등수"] = i + 1


# 출력 함수
def print_table(students):
    print("\n\t\t\t\t\t\t\t\t\t\t성적관리 프로그램")
    print(
        "==================================================================================="
    )
    print(" 학번\t\t\t이름\t\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print(
        "==================================================================================="
    )
    for student in students:
        print(
            f" {student['학번']}\t{student['이름']}\t\t{student['영어']}\t{student['C-언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}"
        )
    print(
        "==================================================================================="
    )


def main():
    students = []
    for _ in range(STUDENT_NUM):
        student = get_input()
        # 학생 정보 딕셔너리에 총점, 평균, 학점 추가
        student["총점"], student["평균"] = calculate_total_average(student)
        student["학점"] = calculate_grade(student["평균"])
        students.append(student)

    calculate_rank(students)
    print_table(students)


if __name__ == "__main__":
    main()
