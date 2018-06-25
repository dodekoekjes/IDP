#!/usr/bin/python3

import struct

bytes = bytearray()
arr = [1, 2, 3, 4, True, 0.871]

INT = 0x00
UINT = 0x01
STR = 0x02
BOOL = 0x03
FLOAT = 0x04

QUIT = 0xf0
MOVE = 0xf1
ARM = 0xf2

for v in arr:
    # print(type(v) is bool)
    
    if type(v) is int:
        vtype = "<i"
        bytes.append(INT)
    elif type(v) is bool:
        vtype = "?"
        bytes.append(BOOL)
    elif type(v) is float:
        vtype = "<f"
        bytes.append(FLOAT)

    val = struct.pack(vtype, v)
    for b in val:
        bytes.append(b)
    
print(bytes)

offset = 0

for _ in range(6):
    arr2 = bytearray()
    vtype = bytes[offset]
    offset+=1

    if vtype == INT:
        len=4
        vtype2 = "<i"
    elif vtype == BOOL:
        len=1
        vtype2 = "?"
    elif vtype == FLOAT:
        len=4
        vtype2 = "<f"
    
    for _ in range(len):
        arr2.append(bytes[offset])
        offset += 1
    print(struct.unpack(vtype2, arr2)[0])

print(hex(2147483647), hex(-2147483648))
print(bytearray(2147483647))