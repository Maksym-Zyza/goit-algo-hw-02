import queue

queue = queue.Queue()

request_id = 0

def generate_request():
    request = input("Enter a request: ")
    queue.put(request)

def process_request():
    if not queue.empty():
        global request_id
        request_id += 1
        request = queue.get()
        print(f"{request_id}. Request: {request}")
    else:
        print("Queue is empty")


while True:
    generate_request()
    process_request()