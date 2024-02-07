# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.


#User wants a program that can add tasks and see a list of it 
#user wants to mark tasks as complete, and remove it from the list

class Tasktracker:

    def __init__(self):
        self.list = []

    def see_tasks(self):
        return self.list

    def add_task(self,Task):
        adder = self.list.append(Task)
        return adder

    def mark_complete(self,Task):
        minuser = self.list.remove(Task)
        return minuser


#Task examples
    
    #Whenever an object is created from the class, a blank list should be generated
    #Whenever see tasks is called, a list of the current things in the list can be added,
    #whenever add_task is added to the list, the user is able to append to the list
    #Whenever mark_complete is called, the user is able to input the task they wish to remove from the list 
