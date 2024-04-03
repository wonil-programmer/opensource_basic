STUDENT_NUM = 5

def get_input():
    student = {}
    student["학번"] = input("학번: ")
    student["이름"] = input("이름: ")
    student["영어"] = int(input("영어: "))
    student["C-언어"] = int(input("C-언어: "))
    student["파이썬"] = int(input("파이썬: "))
    return student

def calculate_total_average(student):
    total = student["영어"] + student["C-언어"] + student["파이썬"]
    average = total / 3
    return total, average

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

def calculate_rank(students):
    sorted_students = sorted(students, key=lambda x: x["총점"], reverse=True)
    for i, student in enumerate(sorted_students):
        student["등수"] = i + 1

def print_table(students):
    print("\n\t\t\t\t\t\t\t\t\t\t성적관리 프로그램")
    print(
        "==================================================================================="
    )
    print(" 학번\t이름\t\영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
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

def add_student(students, student):
    students.append(student)

def remove_student(students, student_id):
    for student in students:
        if student["학번"] == student_id:
            students.remove(student)
            print(f"학번 {student_id} 학생이 삭제되었습니다.")
            return
    print(f"학번 {student_id} 학생을 찾을 수 없습니다.")

def search_student(students, search_key):
    for student in students:
        if search_key in student.values():
            print("검색 결과:")
            print_table([student])
            return
    print("일치하는 학생을 찾을 수 없습니다.")

def sort_students_by_total(students):
    return sorted(students, key=lambda x: x["총점"], reverse=True)

def count_students_above_80(students):
    count = sum(1 for student in students if student["평균"] >= 80)
    return count

def main():
    students = []
    for _ in range(STUDENT_NUM):
        student = get_input()
        student["총점"], student["평균"] = calculate_total_average(student)
        student["학점"] = calculate_grade(student["평균"])
        add_student(students, student)

    calculate_rank(students)
    print_table(students)

    # 특정 학생 삭제
    remove_student_id = int(input())
    remove_student(students, remove_student_id)

    # 특정 학생 검색
    search_key = input("검색할 학생의 학번 또는 이름을 입력하세요: ")
    search_student(students, search_key)

    # 총점을 기준으로 학생 정렬
    sorted_students = sort_students_by_total(students)
    print("\n총점을 기준으로 정렬된 학생 목록:")
    print_table(sorted_students)

    # 평균 80점 이상인 학생 수 카운트
    count = count_students_above_80(students)
    print(f"\n평균 80점 이상인 학생 수: {count}")

if __name__ == "__main__":
    main()
