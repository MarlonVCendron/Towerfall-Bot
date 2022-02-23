from ReadWriteMemory import ReadWriteMemory

base_address = 0x10ffbe8
static_address_offset = 0x994
pointer_static_address = base_address - static_address_offset
offsets = [0x8, 0x1b0,0xc,0x20,0x8,0x54]

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('TowerFall.exe')
process.open()
my_pointer = process.get_pointer(pointer_static_address, offsets=offsets)
pointer_value = process.read(my_pointer)
print(f'Value: {pointer_value}')
