import pymem
from resolver import resolve_ptr_chain

def main():
    pm = pymem.Pymem("How to Fish.exe")
    module_base = pymem.process.module_from_name(
    pm.process_handle, "mono-2.0-bdwgc.dll"
    ).lpBaseOfDll

    pointer_base = module_base + 0x007390F8
    offsets = [0x90, 0xC30, 0x18, 0x168, 0x68, 0x110, 0x6C]

    while True:
        final_address = resolve_ptr_chain(pm, pointer_base, offsets)
        value = pm.read_int(final_address)
        print("Money: ", value)
        user_input = int(input("How much money do you wish to have?"))
        pm.write_int(final_address, user_input)

if __name__ == "__main__":
    main()

