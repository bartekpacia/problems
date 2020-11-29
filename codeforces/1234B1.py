from collections import deque

line = input().split(" ")
n = int(line[0])
k = int(line[1])

all_id_list = input().split(" ")
displayed = deque(maxlen=k)
for index, _id in enumerate(all_id_list):
    if _id not in displayed and len(displayed) <= k:
        displayed.appendleft(_id)
    if _id in displayed and len(displayed) <= k:
        pass
    else:
        displayed.pop()
        displayed.appendleft(_id)

print(len(displayed))
for _id in displayed:
    print(_id, end=" ")
