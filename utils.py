
tasks=[]
def get_user_choice(options):
    print(f"{options} what is yoer choice")
    choice=input()
    return choice


    

def show_all_tasks(tasks: list):
    for i in tasks:
        if not i:
            print("empty_list")
    print(tasks)


    

def add_task(tasks:list,new_task:str):
    return tasks.append(new_task)

def exit():
    return  False
    

