import pymem
import pickle
import numpy as np

mem = pymem.Pymem("TowerFall.exe")

def get_addr(base_address, offsets):
    addr = mem.read_int(base_address)
    for offset in offsets[:-1]:
        addr = mem.read_int(addr + offset)
    return addr + offsets[-1]


def get_players_positions(dict=False):
    with open('Cheat Table/CheatTable_dict', 'rb') as file:
        cheat_table = pickle.load(file)

    if dict:
        positions = {}
        for variable, address_info in cheat_table.items():
            value = mem.read_int(get_addr(address_info['base_address'], address_info['offsets']))
            positions[variable] = value
        return positions
    else:
        positions = np.array([])
        for variable, address_info in cheat_table.items():
            try:
                value = mem.read_int(get_addr(address_info['base_address'], address_info['offsets']))
            except:
                value = -1
            positions = np.append(positions, value)
        return positions


if __name__ == '__main__':
    print(get_players_positions())