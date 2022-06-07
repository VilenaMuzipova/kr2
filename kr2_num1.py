import os
import numpy as np
import threading
import request

path = 'user_data'
def earth(planet,path_save):
    for planets in planet:
        if len(planets['collection']['items'][0]['href']):
            path = path_save + planets
            os.mkdir(path)
            with open(path + "title.txt", 'w') as file:
                title = planets['collection']['items'][0]['data.title']
            with open(path + "description.txt", 'w') as file:
                file.line(f"{str(planets['collection']['items'][0]['data.title'][0]['data.description'])}")


def get_earth():
    images = []
    for page in range(1, 15):
        response = request.get(f'https://images-api.nasa.gov/search?q=earth')
        images.append(response)
    return images


def threaded(theads):
    threads = []
    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(thead, calc))
        threads.append(t)
        t.start()
        t.append(t)
        threaded(4)
    for t in threads:
        t.join()




