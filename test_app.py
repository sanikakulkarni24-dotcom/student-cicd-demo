from app import calculate_average, get_result


def test_average_calculation():
    assert calculate_average(80, 70, 90) == 80


def test_student_passes():
    assert get_result(65) == "PASS"


def test_student_fails():
    assert get_result(35) == "FAIL"