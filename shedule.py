import time
from watchdog.observers import Observer
from shedule_class import FileShedule

event_handler = FileShedule()
observer = Observer()
path: str = r"F:\PyP"
observer.schedule(event_handler, path=path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except:
    print("Exception")
finally:
    observer.stop()
    observer.join()
