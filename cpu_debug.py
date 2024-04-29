import pdb,time, psutil, requests
memory_limit = 55
url = "http://192.168.176.3:8080/data" # тесты с использованием второго тестового задания

def memory_use():
    memory = psutil.virtual_memory()
    memory_proc = memory.percent
    pdb.set_trace()
    if memory_proc > memory_limit:
        alarm_req = f"потребление памяти превышает {memory_proc}%, отправка запроса"
        print(alarm_req)
        sender(alarm_req)
        time.sleep(1)
        
    else:
        print(f"Потребление памяти на данный момент - {memory_proc}%")

def sender(message):
    packedge = {'message': message}
    try:
        response = requests.post(url, json=packedge)
        if response.status_code == 200:
            print("запрос отправлен")
        else:
            print("запрос не отправлен")
    except requests.exceptions.RequestException as e:
        print(f"запрос не отправлен: {e}")

if __name__ == "__main__":
    while True:
        
        memory_use()