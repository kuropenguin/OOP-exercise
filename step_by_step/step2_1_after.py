# ルール2．else句を使用しないこと
def get_grade(score: int) -> str:
    if score > 80:
        return "A"
    if score > 60:
      return "B"
    return "C"

grade = get_grade(85)
print(grade)  # "A"
