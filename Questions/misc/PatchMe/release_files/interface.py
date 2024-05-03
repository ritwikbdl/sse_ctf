#!/usr/local/bin/python

import random
import subprocess
import re


def test_valid_hex(data):
    return re.match(r"0x[0-9a-fA-F]+", data) is not None


with open("bin", "rb") as f:
    bin_ = list(f.read())
    print('''
░██████╗░██████╗███████╗  ██████╗░░█████╗░██████╗░░░██╗██╗
██╔════╝██╔════╝██╔════╝  ╚════██╗██╔══██╗╚════██╗░██╔╝██║
╚█████╗░╚█████╗░█████╗░░  ░░███╔═╝██║░░██║░░███╔═╝██╔╝░██║
░╚═══██╗░╚═══██╗██╔══╝░░  ██╔══╝░░██║░░██║██╔══╝░░███████║
██████╔╝██████╔╝███████╗  ███████╗╚█████╔╝███████╗╚════██║
╚═════╝░╚═════╝░╚══════╝  ╚══════╝░╚════╝░╚══════╝░░░░░╚═╝
''')
    for i in range(3):
        address = input("Enter address in hex(eg., 0x1234): ").strip()

        if not test_valid_hex(address):
            print("[ERROR]\tInvalid address.")
            exit(1)
        address = int(address, 16)
        if address < 0 or address > len(bin_):
            print("[ERROR]\tAddress is out of range.")
            exit(1)

        val = input("Enter one byte in hex(eg., 0x56): ").strip()

        if not test_valid_hex(val):
            print("[ERROR]\tInvalid value")
            exit(1)

        val = int(val, 16)
        if val < 0 or val > 256:
            print("[ERROR]\tvalue is out of range.")
            exit(1)

        bin_[address] = val

        if i < 2:
            choice = input("Do you want to continue? (y/n): ").strip()
            if choice != "y":
                break

    name = random.randint(0, 1000000)
    path = f"bin_out_{name}"
    with open(path, "wb") as fo:
        fo.write(bytes(bin_))
    # change file permission add +x
    subprocess.run(["chmod", "+x", path])
    s = subprocess.Popen(
        ["./" + path],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output = s.communicate()
    print(output)
    subprocess.run(["rm", path])
