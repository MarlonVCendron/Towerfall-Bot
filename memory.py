import pymem
mem = pymem.Pymem("TowerFall.exe")
#mem = pymem.Pymem("kernel32.dll")
#base = pymem.process.module_from_name(mem.process_handle, "kernel32.dll").lpBaseOfDll
#base = pymem.process.module_from_name(mem.process_handle, "TowerFall.exe").lpBaseOfDll
#print(hex(base))

threadstack0 = 0x14ff918

baseOffsetX = 0x994
offsetsX = [0x8, 0x1b0,0xc,0x20,0x8,0x54]
baseOffsetY = 0x89c
offsetsY = [0x1c, 0x28,0x54,0x104,0xc,0x58]


def getAddr(baseOffset, offsets):
    addr = mem.read_int(threadstack0 - baseOffset)
    for offset in offsets[:-1]:
        addr = mem.read_int(addr + offset)
    return addr + offsets[-1]

while True:
    valX = mem.read_int(getAddr(baseOffsetX, offsetsX))
    valY = mem.read_int(getAddr(baseOffsetY, offsetsY))
    print(f'X: {valX} Y: {valY}')
