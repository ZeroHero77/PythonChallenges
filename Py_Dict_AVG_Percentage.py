jk = float()
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks[query_name]:
        jk += i
        kl = jk/len(scores)
    print(format(kl,"#0.2f"))
