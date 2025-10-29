import utils
todo=[]
options=["1.add a task",
         "2.show all tasks",
         "3.exit"]
def main(tasks,options):
    condition=True
    while  condition is True:

        menu=utils.get_user_choice(options)

        The_selected_option=utils.callis_a_function_by_choice(menu,task_adder,task_shower,exit,tasks)

        task_shower=utils.show_all_tasks()

        new_task = input('enter task')
        task_adder=utils.add_task(tasks,new_task)

        get_out=utils.exit(condition)




