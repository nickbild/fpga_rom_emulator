# Populate byte array.
bytes = []
v = 0
for i in range(12288):
    bytes.append(0) # TODO: v
    v += 1
    if v == 256:
        v = 0

# Generate BRAM Verilog code.
byte_counter = 0

for i in range(24):
    print("""    SB_RAM40_4K #(
      .READ_MODE(1),     // 512x8
      .WRITE_MODE(1),    // 512x8""")

    for k in range(16):
      label = k
      if label == 10:
          label = "A"
      elif label == 11:
          label = "B"
      elif label == 12:
          label = "C"
      elif label == 13:
          label = "D"
      elif label == 14:
          label = "E"
      elif label == 15:
          label = "F"

      # Output wacky, poorly-documented init format.
      print("      .INIT_{0}(256'b".format(label), end='')
      newline = ""
      for j in range(16):
        b1 = '{:08b}'.format(bytes[byte_counter])
        b2 = '{:08b}'.format(bytes[byte_counter+256])
        mixed_byte = ""
        for x in range(8):
            mixed_byte += b1[x] + b2[x]
        byte_counter += 1
        newline = mixed_byte + newline
      print(newline, end='')

      if label == "F":
          print(")")
      else:
          print("),")

    print("""    ) ram{0} (
      .RDATA(memory_data_out_{0}),
      .RADDR(rom_address),
      .WADDR(0),
      .WDATA(0),
      .RCLKE(1'b1),
      .RCLK(CLK),
      .RE(1'b1),
      .WCLKE(1'b1),
      .WCLK(CLK),
      .WE(1'b0)
    );
""".format(i))
