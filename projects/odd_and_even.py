def average_grades(gradebook: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    for student in gradebook:
        total: int = 0
        for grade in gradebook[student]:
            total += grade
        averages[student] = total / len(gradebook[student])
    return averages            