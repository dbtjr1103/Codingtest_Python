import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return "".join(list(answer.keys()))