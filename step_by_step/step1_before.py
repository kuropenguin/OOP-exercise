def method1():
    s = []
    for i in range(10):
        for j in range(10):
            if i == j:
                s.append("■")
            else:
                s.append("●")
        s.append("\n")
    print(''.join(s))

method1()
