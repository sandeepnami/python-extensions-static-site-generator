from urllib.parse import _NetlocResultMixinStr
from ssg import hooks
import time

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time 
    start_time = time.time()  # Get the current systems time
    
@hooks.register("written")
def written():
    global total_written
    total_written = total_written + 1
    
@hooks.register("stats")
def stats():
    final_time = time.time() - start_time