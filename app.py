def calculate_average(maths, science, english):
    return (maths + science + english) / 3


def get_result(average):
    if average >= 40:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    maths = 85
    science = 72
    english = 78

    average = calculate_average(maths, science, english)
    result = get_result(average)

    print("Average Marks:", average)
    print("Student Result:", result)