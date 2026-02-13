import psutil
import datetime

from dns.ipv4 import inet_aton


def check_server():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Get disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent

    # Get network I/O
    net_io = psutil.net_io_counters()

    # Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the server status
    print(f"Server Status at {current_time}:")
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > 80:
        print("Warning: High CPU usage!")

    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > 80:
        print("Warning: High Memory usage!")

    print(f"Disk Usage: {disk_usage}%")
    print(f"Network I/O: Sent={net_io.bytes_sent} bytes, Received={net_io.bytes_recv} bytes")

if __name__ == "__main__":
    check_server()