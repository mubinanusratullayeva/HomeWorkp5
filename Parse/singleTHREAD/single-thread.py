import time
import requests
from bs4 import BeautifulSoup

start_time = time.time_ns() // 1_000_000

for i in range(1, 16):
    url = f'https://multimediya.uz/e-kitob/index.php?mavzu={i}'
    respond = requests.get(url)

    try:
        if respond.status_code == 200:
            soup = BeautifulSoup(respond.content, 'html.parser')

            # for h in range(1, 16):
            file = open(str(i)+'.html', 'w', encoding='UTF-8')
            file.write(soup.prettify())
            file.close()
    except Exception as e:
        print(e)


end_time = time.time_ns() // 1_000_000
print(f"{end_time - start_time: .3f}") # 4583