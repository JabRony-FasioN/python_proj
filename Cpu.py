import psutil

# Function to get current memory usage
def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent


# Set the memory threshold for the alarm
memory_threshold = 50

# Check memory usage and send alert if threshold is exceeded
if get_memory_usage() > memory_threshold:
    subject = 'Memory Usage Alert'
    print("test")
    body = 'Memory usage is above {}%'.format(memory_threshold)
    print(subject, body)