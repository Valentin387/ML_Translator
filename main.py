"""
class Instruction():
    def __init__(self,string):
        self.mnemonic=
        self.rd=
        self.rs1=
        self.rs2=
"""

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
def find_the_mnemonic(list_of_Type_dictionaries,word):
    mnemonic=""
    for d in list_of_Type_dictionaries:
        for new_k,new_val in d.items():
            for i in new_val:
                if word==i:
                    mnemonic=new_k
                    break
    return mnemonic


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

    TypeList = [Dictionary_R,Dictionary_I,Dictionary_IJ,Dictionary_L,Dictionary_J,Dictionary_Ului,Dictionary_Uauipc,Dictionary_S,Dictionary_B]
    register=[];
    linesList=[]
    with open("InputSampleLLL.txt",'r') as Input:
        linesList=Input.readlines()
        for line in linesList:
            elements=line.split(",")
            elements=takeJumpAwayArray(elements)
            mnemonic=find_the_mnemonic(TypeList,elements[0])
            opcode=Dictionary_OpCode[mnemonic]
            func3=Dictionary_Func3[elements[0]]
            func7=Dictionary_Func7[elements[0]]




    #with open("OutputSampleHex.txt",'a') as Output:
        #Output.write("\ncachorro")
