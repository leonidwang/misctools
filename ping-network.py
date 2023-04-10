import subprocess
import ipaddress
import multiprocessing
from prettytable import PrettyTable

"""
Python script to ping all IPs in a range and report result(up/down) in a table.

- Ping each IP 3 times.
- 0 packet loss means it's up, otherwise it's down.
- multiprocess is used to do it in parallel.
"""

# IPs you want to ping
iprange="10.1.1.0/24"

def ping(ip_address):
    command = f"ping -c 3 {ip_address}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if "0% packet loss" in stdout.decode():
        return [ip_address, "Up"]
    else:
        return [ip_address, "Down"]

if __name__ == "__main__":
    # Create a list of all IP addresses in the network
    network = ipaddress.ip_network(iprange)
    ips = [str(ip) for ip in network.hosts()]

    # Use multiprocessing to ping all IP addresses in parallel
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = []
        for i, result in enumerate(pool.imap_unordered(ping, ips), 1):
            if result is not None:
                results.append(result)
            if i % 10 == 0 or i == len(ips):
                print(f"Pinged {i}/{len(ips)} IP addresses")

    # Summarize the results in a table
    table = PrettyTable(["IP Address", "Status"])
    table.align = "l"
    for result in results:
        table.add_row(result)
    print(table)
