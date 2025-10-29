import utils
import by_indix
todo=[]
options=["1.add a task",
         "2.show all tasks",
         "3.exit",
         "4.delete"]
def main(tasks,options):
    get_out = True
    while  get_out == True:
        

        choice=utils.get_user_choice(options)
        
        if choice=="1" or choice=="Add a task":
            new_task=input("enter a task")
            task_adder=utils.add_task(tasks,new_task)
        elif choice=='2' or choice=="show_all_tasks":
            task_shower=utils.show_all_tasks(tasks)
        elif choice=='3' or choice=="leave":
            get_out=utils.exit()
        elif choice=='4' or choice=="delete":
            delete=by_indix.delete_task(tasks,index)
        

        
print(main(todo,options))
        




