import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print("=" * 40, "System Information", "=" * 40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Name: {uname.node}")
print(f"Release {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")

print("=" * 40, "Processor Information", "=" * 40)
print(f"Processor: {uname.processor}")
print("Physical cores: ", psutil.cpu_count(logical=False))
print("Cores total: ", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Maximum frequency: {cpufreq.max:.2f} MGhz")
print(f"Maximum frequency: {cpufreq.min:.2f} MGhz")
print(f"Maximum frequency: {cpufreq.current:.2f} MGhz")

print("CPU load per core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total load: {psutil.cpu_percent()}%")

print("=" * 40, "System Memory Information", "=" * 40)
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percent: {svmem.percent}%")

print("=" * 40, "Swap Memory Information", "=" * 40)
swap = psutil.swap_memory()
print(f"Value: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percent: {swap.percent}%")

print("=" * 40, "Dick System Information", "=" * 40)
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Disk: {partition.device} ===")
    print(f"   Filesystem Type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:

        continue
    print(f"   Total Capacity: {get_size(partition_usage.total)}")
    print(f"   Used Capacity: {get_size(partition_usage.used)}")
    print(f"   Free Capacity: {get_size(partition_usage.free)}")
    print(f"   Percent Capacity: {partition_usage.percent}%")

print("=" * 40, "Network Information", "=" * 40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"   IP: {address.address}")
            print(f"   Mask: {address.netmask}")
            print(f"   Broadcast: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"   MAC-address: {address.address}")
            print(f"   Mask: {address.netmask}")
            print(f"   Broadkast: {address.broadcast}")

net_io = psutil.net_io_counters()
print(f"Total sent bytes: {get_size(net_io.bytes_sent)}")
print(f"Total receive bytes: {get_size(net_io.bytes_recv)}")
