
def takeJumpAway(string):
    newString=string.replace("\n","")
    return newString

def takeJumpAwayArray(list):
    l1=[]
    count=0
    tam=len(list)
    for word in list:
        count+=1
        if (count == tam):
            l1.append(takeJumpAway(word))
        else:
            l1.append(word)
    return l1

#this is the ugliest code I've made. But it works
def find_the_type(list_of_Type_dictionaries,word):
    type=""
    for d in list_of_Type_dictionaries:
        for new_k,new_val in d.items():
            for i in new_val:
                if word==i:
                    type=new_k
                    break
    return type

def decode_identifier(string):
    if string=='ra':
        return 1
    elif string=='sp':
        return 2
    else:
        return int(string.replace("x",""))

def instruction_R(func7,rs2,rs1,func3,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if (not rd):
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
    while cont < 32:
        instruction.append(func7[-1])
        func7=func7[:-1]
        cont+=1
    return instruction

def instruction_I(isNeg,imm,rs1,func3,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #if it's empty
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 32:
        if (not imm):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(imm[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    return instruction

def instruction_S(rs2,rs1,func3,imm,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not imm): #if it's empty
            instruction.append('0')
        elif(imm[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
    while cont < 32:
        if(not imm): #if it's empty
            instruction.append('0')
        elif(imm[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(imm[-1])
        imm=imm[:-1]
        cont+=1
    return instruction

def instruction_B(isNeg,rs2,rs1,func3,label,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    if len(label)>=11 and label[-10]!='b':
        instruction.append(label[-10])
    else:
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    cont+=1
    label=label[:-1]
    while cont < 12:
        if(not label): #if it's empty
            instruction.append('0')
        elif(label[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    while cont < 15:
        instruction.append(func3[-1])
        func3=func3[:-1]
        cont+=1
    while cont < 20:
        if (not rs1):
            instruction.append('0')
        elif(rs1[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs1[-1])
        rs1=rs1[:-1]
        cont+=1
    while cont < 25:
        if (not rs2):
            instruction.append('0')
        elif(rs2[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rs2[-1])
        rs2=rs2[:-1]
        cont+=1
    while cont < 31:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    label=label[:-1]
    if (not label):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label[-1])
    return instruction

def instruction_U(isNeg,label,rd,opcode):#it probably works
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #if it's empty
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    for i in range(12):
        label=label[:-1]

    while cont < 31:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1
    return instruction

def instruction_J(isNeg,label,rd,opcode):
    instruction=[]
    cont=0
    while cont < 7:
        instruction.append(opcode[-1])
        opcode=opcode[:-1]
        cont+=1
    while cont < 12:
        if(not rd): #if it's empty
            instruction.append('0')
        elif(rd[-1]=='b'):
            instruction.append('0')
        else:
            instruction.append(rd[-1])
        rd=rd[:-1]
        cont+=1
    label=label[:-1]

    label_copy1=label
    label_copy2=label
    label_copy3=label

    for i in range(12):
        label=label[:-1]

    while cont < 20:
        if (not label):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label[-1])
        label=label[:-1]
        cont+=1

    for i in range(11):
        label_copy1=label_copy1[:-1]
    if (not label_copy1):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    elif(label_copy1[-1]=='b'):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label_copy1[-1])

    label_copy2=label_copy2[:-1]
    while cont < 31:
        if (not label_copy2):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        elif(label_copy2[-1]=='b'):
            if isNeg:
                instruction.append('1')
            else:
                instruction.append('0')
        else:
            instruction.append(label_copy2[-1])
        label_copy2=label_copy2[:-1]
        cont+=1

    for i in range(20):
        label_copy3=label_copy3[:-1]

    if (not label_copy3):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    elif(label_copy3[-1]=='b'):
        if isNeg:
            instruction.append('1')
        else:
            instruction.append('0')
    else:
        instruction.append(label_copy3[-1])
    return instruction


def converter_A2Complement(imm):
    new_imm=""
    firstOneBurned=False
    if(imm[-1]=='1'):
        new_imm=imm[-1]+new_imm
        imm=imm[:-1]
        firstOneBurned=True

    while imm[-1]!='b':
        if (firstOneBurned):
            if(imm[-1]=='1'):
                new_imm='0'+new_imm
            else:
                new_imm='1'+new_imm
        else:
            new_imm=imm[-1]+new_imm
        if(imm[-1]=='1'):
            firstOneBurned=True
        imm=imm[:-1]
    return new_imm

def flip_array(array):
    l1=[]
    count=1
    for e in array:
        l1.append(array[-count])
        count+=1
    return l1

if __name__ =="__main__":

    Dictionary_R = {
    'R':["add","sub","sll","slt","sltu","xor","srl","sra","or","and"]
    }

    Dictionary_I = {
    'I':["addi","slli","slti","sltiu","xori","srli","srai","ori","andi"]
    }

    Dictionary_IJ = {
    "IJ":"jalr"
    }

    Dictionary_L = {
    'L':["lb","lh","lw","lbu","lhu"]
    }

    Dictionary_J = {
    'J':["jal"]
    }

    Dictionary_Ului = {
    'Ului':["lui"]
    }

    Dictionary_Uauipc = {
    'Uauipc':["auipc"]
    }

    Dictionary_S = {
    'S':["sb","sh","sw"]
    }

    Dictionary_B = {
    'B':["beq","bne","blt","bge","bltu","bgeu"]
    }

    Dictionary_OpCode = {
    'R':"0110011",
    'I':"0010011",
    'L':"0000011",
    'LR':"1100111",
    'S':"0100011",
    'B':"1100011",
    'J':"1101111",
    'Ului':"0110111",
    'Uauipc':"0010111"
    }

    Dictionary_Func3 = {
    "add":"000",
    "sub":"000",
    "sll":"001",
    "slt":"010",
    "sltu":"011",
    "xor":"100",
    "srl":"101",
    "sra":"101",
    "or":"110",
    "and":"111",

    "addi":"000",
    "slli":"001",
    "slti":"010",
    "sltiu":"011",
    "xori":"100",
    "srli":"101",
    "srai":"101",
    "ori":"110",
    "andi":"111",

    "lb":"000",
    "lh":"001",
    "lw":"010",
    "lbu":"100",
    "lhu":"101",

    "jalr":"000",

    "beq":"000",
    "bne":"001",
    "blt":"100",
    "bge":"101",
    "bltu":"110",
    "bgeu":"111",

    "sb":"000",
    "sh":"001",
    "sw":"010",

    "jal":"000",
    "lui":"000",
    "auipc":"000"
    }

    Dictionary_Func7 = {
    "add":"0000000",
    "sub":"0100000",
    "sll":"0000000",
    "slt":"0000000",
    "sltu":"0000000",
    "xor":"0000000",
    "srl":"0000000",
    "sra":"0100000",
    "or":"0000000",
    "and":"0000000",

    "addi":"0000000",
    "slli":"0000000",
    "slti":"0000000",
    "sltiu":"0000000",
    "xori":"0000000",
    "srli":"0000000",
    "srai":"0000000",
    "ori":"0000000",
    "andi":"0000000",

    "lb":"0000000",
    "lh":"0000000",
    "lw":"0000000",
    "lbu":"0000000",
    "lhu":"0000000",

    "jalr":"0000000",

    "beq":"0000000",
    "bne":"0000000",
    "blt":"0000000",
    "bge":"0000000",
    "bltu":"0000000",
    "bgeu":"0000000",

    "sb":"0000000",
    "sh":"0000000",
    "sw":"0000000",

    "jal":"0000000",
    "lui":"0000000",
    "auipc":"0000000"
    }

    Dictionary_Hexadecimal = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F",
    }

    TypeList = [Dictionary_R,Dictionary_I,Dictionary_IJ,Dictionary_L,Dictionary_J,Dictionary_Ului,Dictionary_Uauipc,Dictionary_S,Dictionary_B]
    instruction_32bits=[];
    linesList=[]
    with open("InputSampleLLL.txt",'r') as Input:
        linesList=Input.readlines()
        for line in linesList:
            elements=line.split(",")
            elements=takeJumpAwayArray(elements)
            type=find_the_type(TypeList,elements[0])#elements[0]:mnemonic: addi, Type: I
            opcode=(Dictionary_OpCode[type])
            func3=(Dictionary_Func3[elements[0]])
            func7=(Dictionary_Func7[elements[0]])

            rd=""
            rs1=""
            rs2=""
            imm=""
            isNeg=False
            if(type=='R'):
                rd=bin(decode_identifier(elements[1])) #beware, 'bin' is in actually just string, and strings are NOT lists
                rs1=bin(decode_identifier(elements[2]))
                rs2=bin(decode_identifier(elements[3]))
                instruction_32bits=instruction_R(func7,rs2,rs1,func3,rd,opcode) #I got my binary code
                #Now I must flip it (hardware notation you know)
                inst32bf = flip_array(instruction_32bits) #instruction_32bits_flipped
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                #print(Hexa)
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
            if (type=='I' or type=='L' or type=='IJ'):
                rd=bin(decode_identifier(elements[1]))
                if (type=='I'):
                    rs1=bin(decode_identifier(elements[2]))
                    imm=bin(decode_identifier(elements[3]))
                else:
                    imm=bin(decode_identifier(elements[2]))
                    rs1=bin(decode_identifier(elements[3]))

                if(imm[0]=='-'):
                    isNeg=True
                    imm=converter_A2Complement(imm)

                instruction_32bits=instruction_I(isNeg,imm,rs1,func3,rd,opcode)
                inst32bf = flip_array(instruction_32bits)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
            if (type=='S'):
                rs2=bin(decode_identifier(elements[1]))
                imm=bin(decode_identifier(elements[2]))
                rs1=bin(decode_identifier(elements[3]))
                #for type 'S' the imm is never negative ('til where I know')
                instruction_32bits=instruction_S(rs2,rs1,func3,imm,opcode)
                inst32bf = flip_array(instruction_32bits)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
            if(type=='B'):
                rs1=bin(decode_identifier(elements[1]))
                rs2=bin(decode_identifier(elements[2]))
                label=bin(decode_identifier(elements[3])*4)
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_B(isNeg,rs2,rs1,func3,label,opcode)
                inst32bf = flip_array(instruction_32bits)
                #print(inst32bf)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
            if (type=='Ului' or type=='Uauipc'):
                rd=bin(decode_identifier(elements[1]))
                label=bin(decode_identifier(elements[2])*4)
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_U(isNeg,label,rd,opcode)
                inst32bf = flip_array(instruction_32bits)
                #print(inst32bf)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")
            if(type=='J'):
                rd=bin(decode_identifier(elements[1]))
                label=bin(decode_identifier(elements[2])*4)
                if(label[0]=='-'):
                    isNeg=True
                    label=converter_A2Complement(label)

                instruction_32bits=instruction_J(isNeg,label,rd,opcode)
                inst32bf = flip_array(instruction_32bits)
                #print(inst32bf)
                cont=0
                Hexa=""
                for i in range(8):
                    temp=inst32bf[cont]+inst32bf[cont+1]+inst32bf[cont+2]+inst32bf[cont+3]
                    Hplus=Dictionary_Hexadecimal[temp]
                    print(temp)
                    Hexa = Hexa + Hplus
                    cont+=4
                with open("OutputSampleHex.txt",'a') as Output:
                    Output.write(Hexa)
                    Output.write("\n")

    print("\n\n END OF LINE \n")

    #with open("OutputSampleHex.txt",'a') as Output:
        #Output.write("\ncachorro")
