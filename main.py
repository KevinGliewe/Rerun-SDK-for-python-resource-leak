import rerun as rr

import time

# Import psutil to get the process id
import psutil
process = psutil.Process()

start_memory = process.memory_info().rss / 1024 / 1024


for i in range(10000):
    start = time.time()

    # Initialize Rerun
    rr.init(application_id="MyPythonApplication", recording_id=f"Run{i}")
    rr.connect_tcp(addr="127.0.0.1:9876")

    # Log some data
    rr.log("logs", rr.TextLog(f"This a log entry for Run {i}", level=rr.TextLogLevel.TRACE))

    # Close the connection
    rr.disconnect()

    # Print the time taken and memory usage
    end = time.time()

    time_taken_ms = (end - start) / 1000
    memory_used_mb = process.memory_info().rss / 1024 / 1024

    print(f"Run {i}, time={time_taken_ms} ms, memory={memory_used_mb} MiB, connections={len(psutil.net_connections())}, threads={len(process.threads())}")

    time.sleep(0.01)

end_memory = process.memory_info().rss / 1024 / 1024

# Print the memory usage increase
print(f"Memory usage increased by {end_memory - start_memory} MB")