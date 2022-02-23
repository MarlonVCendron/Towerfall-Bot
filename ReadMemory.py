import pymem
import pickle

mem = pymem.Pymem("TowerFall.exe")

def getAddr(base_address, offsets):
    addr = mem.read_int(base_address)
    for offset in offsets[:-1]:
        addr = mem.read_int(addr + offset)
    return addr + offsets[-1]

def main():
    with open('Cheat Table/CheatTable_dict', 'rb') as file:
        cheat_table = pickle.load(file)

    while True:
        for variable, address_info in cheat_table.items():
            value = mem.read_int(getAddr(address_info['base_address'], address_info['offsets']))
            print(variable, value)
        break


if __name__ == '__main__':
    main()