# ルール1．1つのメソッドにつきインデントは1段落までにすること
from typing import List

def method1():
    block = build_block()
    print(block)

def build_block() -> str:
    s = []
    for y in range(10):
        line = build_line(y)
        s.append(line)
        s.append("\n")
    return ''.join(s)
    
    
def build_line(y: int) -> str:
  line = []
  for x in range(10):
      mark = choice_mark(y, x)
      line.append(mark)
  return ''.join(line)


def choice_mark(y: int, x: int) -> str:
    if y == x:
        return "■"
    return "●"

method1()
