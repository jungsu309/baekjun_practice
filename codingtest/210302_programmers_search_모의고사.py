def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second =[2, 1, 2, 3, 2, 4, 2, 5]
    third=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct_first = 0
    correct_second = 0
    correct_third=0

    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            correct_first = correct_first + 1
        if second[i%8] == answers[i]:
            correct_second = correct_second + 1
        if third[i%10] == answers[i]:
            correct_third = correct_third + 1

    max_score = max(correct_first,correct_second,correct_third)

    if max_score == correct_first:
        answer.append(1)
    if max_score == correct_second:
        answer.append(2)
    if max_score == correct_third:
        answer.append(3)

    return answer
#solution([1,2,3,4,5])
print(solution([1,3,2,4,2]))
