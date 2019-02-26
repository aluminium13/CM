from data import relevance, statistics
from task import Task


class sys_FIFO():
     
    # ініціалізування СМО
    def __init__(self, it):
        self.iterations = it        # кількість задач, що подаються на СМО
        self.count = 0
        self.queue = []
        self.solved = []
        #self.allTasks = []

    # симуляція роботи системи
    def start(self):

        # встановлення часу в 0
        self.t_current = 0

        # генерація першої задачі
        self.generateTask()
        self.t_endOfComputing = self.queue[0].t_solve

        # обробка/створення задач
        while self.count < self.iterations:
            if self.t_endOfComputing == -1 or self.t_nextTaskGen < self.t_endOfComputing:
                self.t_current = self.t_nextTaskGen
                self.generateTask()
                if self.t_endOfComputing == -1:
                    self.t_endOfComputing = self.queue[0].t_solve + self.t_current
            else:
                self.computeTask()
        while len(self.queue) != 0:
            self.computeTask()
        
        # отримання статистики
        statistics(self.solved, self.iterations)
       
    # функція генерації нового завдання
    def generateTask(self):
        task = Task(self.t_current)
        self.count += 1
        self.queue.append(task)
        self.t_nextTaskGen =  task.t_new
        #self.allTasks.append(task)
        

    # функція обробки задачі на процесорі
    def computeTask(self):
        
        self.t_current = self.t_endOfComputing
        currentTask = self.queue.pop(0)
        timeInQueque = self.t_current - currentTask.t_in - currentTask.t_solve
        if relevance(timeInQueque) != 0:
            currentTask.t_inQueque = timeInQueque
            currentTask.t_firstComp = timeInQueque
            currentTask.t_out = self.t_current
            self.solved.append(currentTask)
        
        if len(self.queue) != 0:
            self.t_endOfComputing = self.t_current + self.queue[0].t_solve
        else:
            self.t_endOfComputing = -1
