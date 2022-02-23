from bs4 import BeautifulSoup 
import pickle

threadstack0 = 0x14ff918

def main():
    file = open('Cheat Table/Towerfall.CT', 'r')
    cheat_table  = BeautifulSoup(file.read(), 'xml') 
    file.close()

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
        data[variable_name]['offsets'] = offsets_array
        data[variable_name]['address'] = address

    with open('Cheat Table/CheatTable_dict', 'wb') as dict_file:
        pickle.dump(data, dict_file)


if __name__ == '__main__':
    main()