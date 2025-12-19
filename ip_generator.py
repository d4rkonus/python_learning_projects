#!/usr/bin/python3
from random import randint

octeto = lambda: randint(0, 255)

new_ip = lambda: f"{octeto()}.{octeto()}.{octeto()}.{octeto()}"

ips_created = []

def created_ips(number):
    for _ in range(number):
        ip = new_ip()
        ips_created.append(ip)

created_ips(5)

for index, ip in enumerate(ips_created):
    print(f"\n{index+1} ===> {ip}\n")
