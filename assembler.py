def convertBinToHex(bin):
    hex =" "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex
def checkInstruction(inst):
    convertInstruction = " "
    if inst == "sub":
        convertInstruction = "0000"
    elif  inst == "add":
        convertInstruction = "0001"
    elif inst == "addi":
        convertInstruction = "0010"
    elif inst == "jmp":
        convertInstruction = "0011"
    elif inst == "and":
        convertInstruction = "0100"
    elif inst == "lw":
        convertInstruction = "0101"
    elif inst == "beq":
        convertInstruction = "0110"
    elif inst == "sll":
        convertInstruction = "0111"
    elif inst == "slt":
        convertInstruction = "1000"
    elif inst == "sw":
        convertInstruction = "1001"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction
def checkRegister(reg):
    
    convertReg = ""
    if  reg == "$r0": 
        convertReg ="0000" 
    elif reg == "$r1":
        convertReg ="0001"
    elif reg == "$r2":
        convertReg ="0010"
    elif reg == "$r3":
        convertReg ="0011"
    elif reg == "$r4":
        convertReg ="0100"
    elif reg == "$r5":
        convertReg ="0101"
    elif reg == "$r6":
        convertReg ="0110"
    elif reg == "$r7":
        convertReg ="0111"
    elif reg == "$r8":
        convertReg ="1000"
    elif reg == "$r9":
        convertReg ="1001"
    elif reg == "$r10":
        convertReg ="1010"
    elif reg == "$r11":
        convertReg ="1011"
    elif reg == "$r12":
        convertReg ="1100"
    elif reg == "$r13":
        convertReg ="1101"
    elif reg == "$r14":
        convertReg ="1110"
    elif reg == "$r15":
        convertReg ="1111"
    else:
        convertReg =="Invalid Register"
        
    return convertReg
def decimalToBinary(num):

    if(num<0):
        num =  16 + num

    ext = ""
    result = ""
    
    while(num>0):
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        #result = (num%2 == 0 ? "0" : "1") + result
        num = num//2

    for i in range(4-len(result)):
        ext = "0" + ext

    result = ext + result


    return result



readf = open("inputs","r")
writef = open("outputs","w")
writef.write("v2.0 raw\n")

#print(f.readline())
for i in readf:
    splitted = i.split()
    
    if(splitted[0] == "sub" or splitted[0] == "add" or splitted[0] == "and" or splitted[0] == "slt" or splitted[0] == "sll" ):
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_rs = convertBinToHex(checkRegister(splitted[1]))
        conv_rt = convertBinToHex(checkRegister(splitted[2]))
        conv_rd = convertBinToHex(checkRegister(splitted[3]))

        out = conv_inst + conv_rs + conv_rt + conv_rd
        print(out)
        writef.write(out+"\n")

    elif(splitted[0] == "addi" or splitted[0] == "lw" or splitted[0] == "beq" or splitted[0] == "sw"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_rs = convertBinToHex(checkRegister(splitted[1]))
        conv_rt = convertBinToHex(checkRegister(splitted[2]))
        conv_im = convertBinToHex(decimalToBinary(int(splitted[3])))

        out = conv_inst + conv_rs + conv_rt + conv_im
        print(out)
        writef.write(out+"\n")  
     
    elif(splitted[0] == "jmp"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_target = convertBinToHex(decimalToBinary(int(splitted[1])))

        out = conv_inst + "0" + "0" + conv_target
        print(out)
        writef.write(out+"\n") 
        


    
