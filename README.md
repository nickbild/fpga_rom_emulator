# RapidROM

This FPGA ROM emulator dramatically speeds software development time on computers with ROM-based storage.  It will simulate any 28c256-compatible ROM chips.

Typically, the process to load new code involves powering down the computer, physically removing the ROM, placing the ROM in a programmer, flashing the code, then returning the ROM to the computer and powering it back up.  This process is very time consuming and cumbersome when testing frequent, minor changes to the code, or when debugging a problem.

This FPGA-based emulator can remain attached to the computer and be reprogrammed in a few seconds without even powering the computer down.  Just reprogram the emulator, then hit the CPU reset button to run the new code.

## How It Works

RapidROM has a 15 bit address bus, 8 bit data bus, and a chip enable signal.  Connect the address input lines to your computer's address bus.  Similarly, connect the data output lines to your computer's data bus (data lines are set to high impedance when chip enable is high).  Connect the chip enable pin to the ROM chip enable line (active low).

When an address is put on the address bus, and the chip enable is low, RapidROM will put the corresponding data value on the data bus within 40 nanoseconds.

## Loading Simulated ROM Contents

A convenience script ([build.sh](https://github.com/nickbild/fpga_rom_emulator/blob/main/build.sh)) is included that will compile a 6502 assembly file with DASM, then output (via [bytes_list.py](https://github.com/nickbild/fpga_rom_emulator/blob/main/bytes_list.py)) a comma-delimited list of byte values representing the program.  The list of bytes is inserted at the top of [bram_generator.py](https://github.com/nickbild/fpga_rom_emulator/blob/main/bram_generator.py) which outputs BRAM initialization code to store your program in FPGA memory.  Copy and paste this output into [top.v](https://github.com/nickbild/fpga_rom_emulator/blob/main/top.v) after the `// Insert BRAM definitions after this point.` comment line.  Flash the TinyFPGA with top.v and the new program is ready to run.

## Media

Coming soon!

## Bill of Materials

- 1 x TinyFPGA BX
- Depending on voltage levels of computer, you may need logic level shifters (TinyFPGA operates at 3.3V)
- Miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
