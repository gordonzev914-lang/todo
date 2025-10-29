





# for i in range(len(tasks)):
#     if i==3:
#         tasks.pop(i)
# print(tasks)    





def delete_task(tasks: list, index: int):
    for i in range(len(tasks)):
        if i ==index:
            tasks.pop(i)
    return True        



