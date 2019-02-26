lmbda = 0.8                                           # інтенсивність на вході
mu = 1                                               # інтенсивність на виході
n = 10001                                            # к-ть задач

k1, k2, k3, k4, k5 = -4, -1, -1, 3, 6               # вагові коефіцієнти критеріїв ефективності
t1, t2 = 2000, 4                                       # часові параметри для актуальності 

# функція для обчислення актуальності задачі
def relevance(t):
    if t <= t1:
        return 1
    elif t1 < t < t1 + t2:
        return (t2-t)/(t2-t1) 
        # 2 - 0.5*t
    else:
        return 0


# функція для обрахунку цільової функції
def statistics(solved, n):
    """ 
    х1 - середній час знаходження задачі в системі;
    х2 - дисперсія часу знаходження в системі; 
    х3 - час реакції системи на появу задачі 
    х4 - відношення кількості оброблених задач до загальної кількості 
    х5 - сумарна оцінка актуальності (важливості) оброблених задач.
    """
    x1 = sum((i.t_out - i.t_in) for i in solved)/len(solved)
    x2 = dispersion(solved)
    x3 = sum(i.t_firstComp for i in solved)/len(solved)
    x4 = len(solved)/n
    x5 = sum(relevance(i.t_out-i.t_in) for i in solved)                             # актуальність на вході чи на виході на процесорі?
    #x5 = sum(relevance(i.t_inQueque) for i in solved)                           
    
    print("X1: %f, X2: %f, X3: %f, X4: %f, X5: %f" % (x1, x2, x3, x4, x5))
    y = k1*x1+k2*x2+k3*x3+k4*x4+k5*x5 
    print("y = k1*x1+k2*x2+k3*x3+k4*x4+k5*x5 = " + str(y))


# функція обрахунку дисперсії
def dispersion(solved):
    arr = [(i.t_out - i.t_in) for i in solved]
    m = sum(arr)/len(arr)
    return sum(map(lambda x: (m - x) ** 2, arr))/len(arr)
