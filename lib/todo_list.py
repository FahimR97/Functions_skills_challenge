class TodoList:

    def __init__(self):
        self.emptylist = []
        self.completedlist = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.emptylist.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return self.emptylist
    

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return self.completedlist

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

