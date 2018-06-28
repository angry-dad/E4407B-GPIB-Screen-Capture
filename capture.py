import visa

def read_capture(resource_string="GPIB0::18::INSTR"):
    rm = visa.ResourceManager()
    instr = rm.open_resource(resource_string)
    instr.timeout = 10000
    #Store the current screen image on instrument as C:PICTURE.GIF
    instr.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
        #Grab the screen image file from the instrument
    capture = instr.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')
    with open('capture.gif', 'wb') as fp:
        for byte in capture:
            fp.write(byte)
    #Delete the tempory file on the flash named C:PICTURE.GIF
    instr.write(":MMEM:DEL 'R:PICTURE.GIF'")
    instr.close()
    rm.close()
