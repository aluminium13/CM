from data import relevance, statistics
from task import Task

class sys_FB():
     
     # ініціалізування СМО
    def __init__(self, it, tau):
        self.iterations = it               # кількість задач, що подаються на СМО
        self.t_critical = tau              # критичне значення часу для процесору
        self.count = 0
        self.queque = [[]]
        self.solved = []
        self.currentTask = None
        #self.allTasks = []
        
    # симуляція роботи системи
    def start(self):

        # встановлення часу в 0        
        self.t_current = 0

        # генерація першої задачі
        self.generateTask()
        self.getFromQueques()

        # обробка/створення задач
        while self.count < self.iterations:
            if self.t_endOfComputing == -1 or self.t_nextTaskGen < self.t_endOfComputing:
                self.t_current = self.t_nextTaskGen
                self.generateTask()
                if self.t_endOfComputing == -1:
                    self.getFromQueques()
            else:
                self.computeTask()
        while sum(len(i) for i in self.queque) != 0:
            self.computeTask()
        
        # отримання статистики
        statistics(self.solved, self.iterations)

    # функція генерації нового завдання
    def generateTask(self):
        task = Task(self.t_current)
        self.count += 1
        self.queque[0].append(task)
        self.t_nextTaskGen = task.t_new
        #self.allTasks.append(task)

    # функція обробки задачі на процесорі
    def computeTask(self):
        
        self.t_current = self.t_endOfComputing
        timeInQueque = self.t_current - self.currentTask.t_in - self.currentTask.t_solve
        if relevance(timeInQueque) != 0:    
            if  self.currentTask.t_firstComp == 0:
                self.currentTask.t_firstComp = self.t_current - self.currentTask.t_in
            
            if self.readyToGoOut:
                    self.currentTask.t_inQueque = timeInQueque
                    self.currentTask.t_out = self.t_current
                    self.solved.append(self.currentTask)
            else:
                try:
                    self.queque[self.currentTask.marker].append(self.currentTask)
                except:
                    self.queque.append([])
                    self.queque[self.currentTask.marker].append(self.currentTask)
        self.getFromQueques()

    # функція перевірки чи час виконання задачі не перевищує критичний час обробки процесором
    def compareWithCritical(self):
        if self.currentTask.t_solve < self.t_critical:
            self.t_endOfComputing = self.t_current + self.currentTask.t_solve
            self.readyToGoOut = True
        else:
            self.t_endOfComputing = self.t_current + self.t_critical
            self.currentTask.t_solve -= self.t_critical
            self.readyToGoOut = False
            self.currentTask.marker += 1

    # функція отримання задачі з черг враховуючи їх пріорітетність
    def getFromQueques(self):
        for i in range(len(self.queque)):
            if self.queque[i] != []:
                self.currentTask = self.queque[i].pop(0)
                self.compareWithCritical()
                return
        self.t_endOfComputing = -1