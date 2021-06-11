import time

class Task:
    def __init__(self,index:int,start,stop):
        self.index=index
        self.start=start
        self.stop=stop

    def __repr__(self):
        return f'Task Number {self.index} , Start : {self.start} , End : {self.stop}'

    def getTime(self):
        time_string = time.strftime("%H:%M:%S", time.localtime())
        return time_string


    def check(self):
        while(1):
            if self.start==self.getTime():
                temp=self.start
                self.start=None
                yield f'Task number {self.index} has started at {temp}'

            if self.stop==self.getTime():
                temp = self.stop
                self.stop = None
                yield f'Task number {self.index} has ended at {temp}'

            yield

tasks=[Task(1,'03:58:00','03:58:15').check() , Task(2,'03:58:15','03:58:45').check(),Task(3,'03:58:25','03:58:50').check()]


while (tasks):
    task=tasks[0]
    x=next(task)
    if x!=None:
        print(x)
    tasks.remove(task)
    tasks.append(task)