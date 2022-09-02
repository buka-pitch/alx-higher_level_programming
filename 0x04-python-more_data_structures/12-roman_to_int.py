#!/usr/bin/python3
def roman_to_int(rom_string):
    if rom_string is None or type(rom_string) is not str:
        return (0)
    ro_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(rom_string)):
        if i > 0 and ro_num[rom_string[i]] > rom_num[rom_string[i - 1]]:
            integer += rom_num[rom_string[i]] - \
                2 * rom_num[rom_string[i - 1]]
        else:
            integer += rom_num[rom_string[i]]
    return integer
