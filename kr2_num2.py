import numpy
import time
from multiprocessing import Pool

startTime = time.time()  # время начала замера

items = numpy.random.randint(1000000, size=1000000)
print(len(items), items[:10 ** 6])

items.sort()
print("Наибольшее число:", items[-1])


endTime = time.time()  # время конца замера
totalTime = endTime - startTime  # вычисляем затраченное время
print("Время, затраченное на выполнение данного кода = ", totalTime)



if __name__ == '__main__':
    print("При последовательном:")
    startTime = time.time()
    for _ in range(4):
        print("--- %s seconds ---" % totalTime)

    pool = Pool(processes=4)
    print("При параллельном:")
    startTime = time.time()
    # result = pool.map(range(1000000))
    for _ in range(4):
        print("--- %s seconds ---" % totalTime)

