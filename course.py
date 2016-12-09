def main():
    courses = course()
    instructors = instructor()
    class_time = time()

    course_id = input("Enter course name")
    course_name = (courses[course_id], instructors[course_id], class_time[course_id])

    print(course_name)


def course():
    course_name = ""
    courses = {"CS101":3004, "CS102":4501,"CS103":6755,"NT110":1244,"CM241":1411}
    return courses


def instructor():
    instructors = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
    return instructors
def time():
    class_time = {"CS101":"8:00 a.m.","CS102":"9:00 a.m.", "CS103":"10:00 a.m.", "NT110":"11:00 a.m.", "CM241":"1:00 p.m."}
    return class_time

main()