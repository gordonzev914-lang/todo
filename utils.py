
tasks=[]
def get_user_choice(options):
    print(f"{options} what is yoer choice")
    choice=input()
    return choice

def callis_a_function_by_choice(choice,task_adder,task_shower,exit,tasks,condition):
    
    if choice=="1" or choice=="Add a task":
        
        return task_adder()
    elif choice=='2' or choice=="show_all_tasks":
        return task_shower(tasks)
    elif choice=='3' or choice=="leave":
        return exit(condition)
    

def show_all_tasks(tasks: list):
    for i in tasks:
        if not i:
            print("empty_list")
    print(tasks)


# new_task=input("enter yoer task")    

def add_task(tasks:list,new_task:str):
    return tasks.append(new_task)

def exit(condition):
    return condition is False
    

