import time
import requests
from bs4 import BeautifulSoup
import threading

start_time = time.perf_counter()

def parse(i):
    base_url = f'https://multimediya.uz/e-kitob/index.php?mavzu={i}'
    respond = requests.get(base_url)

    try:
        if respond.status_code == 200:
            soup = BeautifulSoup(respond.content, 'html.parser')

            file = open(str(i)+'.html', 'w', encoding='UTF-8')
            file.write(soup.prettify())
            file.close()

    except Exception as error:
        print(error)

threads = []

for i in range(1, 16):
    thread = threading.Thread(target=parse, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.perf_counter()
print(end_time-start_time)