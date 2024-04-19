class Student:
    def __init__(self, 학번, 이름, 영어, C언어, 파이썬):
        self.학번 = 학번
        self.이름 = 이름
        self.영어 = 영어
        self.C언어 = C언어
        self.파이썬 = 파이썬
        self.총점 = self.영어 + self.C언어 + self.파이썬
        self.평균 = self.총점 / 3
        self.학점 = self.calculate_grade()

    def calculate_grade(self):
        if self.평균 >= 90:
            return "A+"
        elif self.평균 >= 80:
            return "A"
        elif self.평균 >= 70:
            return "B+"
        elif self.평균 >= 60:
            return "B"
        elif self.평균 >= 50:
            return "C+"
        elif self.평균 >= 40:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.학번}\t{self.이름}\t{self.영어}\t{self.C언어}\t{self.파이썬}\t{self.총점}\t{self.평균:.2f}\t{self.학점}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.학번 == student_id:
                self.students.remove(student)
                print(f"학번 {student_id} 학생이 삭제되었습니다.")
                return
        print(f"학번 {student_id} 학생을 찾을 수 없습니다.")

    def search_student(self, search_key):
        for student in self.students:
            if search_key in [student.학번, student.이름]:
                print("검색 결과:")
                print(student)
                return
        print("일치하는 학생을 찾을 수 없습니다.")

    def sort_students_by_total(self):
        sorted_students = sorted(self.students, key=lambda x: x.총점, reverse=True)
        return sorted_students

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.평균 >= 80)
        return count

    def print_table(self):
        print("\n\t\t\t\t\t\t성적관리 프로그램")
        print("===================================================================================")
        print(" 학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점")
        print("===================================================================================")
        for student in self.students:
            print(student)
        print("===================================================================================")


def main():
    student_management_system = StudentManagementSystem()
    STUDENT_NUM = 2
    for _ in range(STUDENT_NUM):
        학번 = input("학번: ")
        이름 = input("이름: ")
        영어 = int(input("영어: "))
        C언어 = int(input("C-언어: "))
        파이썬 = int(input("파이썬: "))
        student = Student(학번, 이름, 영어, C언어, 파이썬)
        student_management_system.add_student(student)

    student_management_system.print_table()

    # 특정 학생 삭제
    remove_student_id = input("삭제할 학생의 학번을 입력하세요: ")
    student_management_system.remove_student(remove_student_id)

    # 특정 학생 검색
    search_key = input("검색할 학생의 학번 또는 이름을 입력하세요: ")
    student_management_system.search_student(search_key)

    # 총점을 기준으로 학생 정렬
    sorted_students = student_management_system.sort_students_by_total()
    print("\n총점을 기준으로 정렬된 학생 목록:")
    for student in sorted_students:
        print(student)

    # 평균 80점 이상인 학생 수 카운트
    count = student_management_system.count_students_above_80()
    print(f"\n평균 80점 이상인 학생 수: {count}")


if __name__ == "__main__":
    main()
