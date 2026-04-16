

class Task:
    def __init__(self, tid, title, priority="low"):
        self.tid = tid
        self.title = title
        self.priority = priority
        self.status = "todo"


class Board:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.tid] = task

    def move_task(self, tid, status):
        if tid in self.tasks:
            self.tasks[tid].status = status

    def delete_task(self, tid):
        if tid in self.tasks:
            del self.tasks[tid]

    def get_by_status(self, status):
        return [t for t in self.tasks.values() if t.status == status]

    def get_priority_tasks(self, priority):
        return [t for t in self.tasks.values() if t.priority == priority]
