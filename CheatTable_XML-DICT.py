from bs4 import BeautifulSoup 
import pickle

def main():
    with open('threadstack0-address.txt', 'r') as file:
        threadstack0 = int(file.read(), 16)
    with open('Cheat Table/Towerfall.CT', 'r') as file:
        cheat_table  = BeautifulSoup(file.read(), 'xml') 

    data = {}
    cheat_entries = cheat_table.find_all('CheatEntry')
    for cheat_entry in cheat_entries:
        description = cheat_entry.find('Description').get_text()[1:-1]
        address_text = cheat_entry.find('Address').get_text()
        offsets = cheat_entry.find_all('Offset')

        offset_thread = int(address_text.split('-')[1], 16)
        address = threadstack0 - offset_thread

        offsets_array = []
        for offset in offsets:
            offsets_array.append(int(offset.get_text(), 16))

        variable_name = description.replace(" ", "").lower()
        data[variable_name] = {}
        data[variable_name]['offsets'] = list(reversed(offsets_array))
        data[variable_name]['base_address'] = address

    with open('Cheat Table/CheatTable_dict', 'wb') as dict_file:
        pickle.dump(data, dict_file)


if __name__ == '__main__':
    main()