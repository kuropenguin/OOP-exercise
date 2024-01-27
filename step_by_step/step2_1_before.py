def get_grade(score: int) -> str:
    if score > 80:
        return "A"
    else:
      if score > 60:
        return "B"
      else:
        return "C"

grade = get_grade(85)
print(grade)  # "A"
