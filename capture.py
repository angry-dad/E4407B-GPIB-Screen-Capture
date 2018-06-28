import visa

def read_capture(resource_string="GPIB0::18::INSTR"):
    rm = visa.ResourceManager()
    instr = rm.open_resource(resource_string)
    # Override the default timeout as the transfer can exceed this
    instr.timeout = 10000
    # Store the current screen image to instrument memory, which is the R 'drive'
    instr.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
    # Grab the screen image file from the instrument. 
    # Set datatype to char that will be written out to a binary file
    capture = instr.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')
    with open('capture.gif', 'wb') as fp:
        for byte in capture:
            fp.write(byte)
    # Delete the file from memory
    instr.write(":MMEM:DEL 'R:PICTURE.GIF'")
    instr.close()
    rm.close()
