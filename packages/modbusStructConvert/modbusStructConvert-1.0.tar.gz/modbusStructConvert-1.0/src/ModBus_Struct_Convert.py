#-*- coding:utf-8 -*-
'''
    ModBus_Struct_Convert_Ex
    Author:Ray Wong
    Version:1.0
    Description:
        ModBus各种数据转换类
'''
import chardet
import struct
import types

class ModBus_Struct_Convert:
    def __init__(self):
        self.AB_CD = 0
        self.CD_AB = 1
        self.BA_DC = 2
        self.DC_BA = 3
        self.AB_CD_EF_GH = 0
        self.GH_EF_CD_AB = 1
        self.BA_DC_FE_HG = 2
        self.HG_FE_DC_BA = 3
        self.Short = 'h'
        self.Int = 'i'
        self.Long = 'l'
        self.Float = 'f'
        self.Double = 'd'
        self.LongLong = 'q'
    
    def Check_Data_Type(self,value,data_type):
        '''
            检查数据类型是否正确
        '''
        tmp = None
        if data_type in ['h','i']:
            tmp = types.IntType
        elif data_type in ['l','q']:
            tmp = types.LongType
        elif data_type in ['f','d']:
            tmp = types.FloatType
        if isinstance(value,tmp):
            return True
        else:
            return False
    
    def Get_Struct_Param(self,data_type,display):
        '''
            获取转换参数
        '''
        A_param = ''
        if display == 0 or display == 1:
            A_param = '>'
        else:
            A_param = '<'
        B_param = 'H'
        if data_type in ['i','l','f']:
            B_param = 'HH'
        elif data_type in ['d','q']:
            B_param = 'HHHH'
        else:
            B_param = 'H'
        return A_param+B_param

    
    def Convert_String_ASCII(self,value):
        '''
            字符串转ASCII
        '''
        if isinstance(value,types.StringType):
            ascii_list = []
            for s in list(value):
                ascii_list.append(ord(s))
            return ascii_list
        else:
            return None
    
    def Convert_ASCII_String(self,value):
        '''
            ASCII转字符串
        '''
        if isinstance(value,types.ListType):
            char_list = []
            for c in value:
                char_list.append(chr(c))
            return ''.join(char_list)
        else:
            return None
    
    def Convert_Dec_Bytes(self,value,data_type,display=0):
        '''
            数值转Byte类型
            参数:值,数据类型,序列
        '''
        if display > 4:
            return None
        if self.Check_Data_Type(value,data_type) == False:
            return None
        tmp = None
        struct_param = self.Get_Struct_Param(data_type,display)
        tmp = list(struct.unpack(struct_param,struct.pack('>'+data_type,value)))
        if display == 1 or display == 3: 
            return tmp[::-1]  
        else:
            return tmp
    
    def Convert_Bytes_Dec(self,value,data_type,display=0):
        '''
            Byte类型转数值
            参数:Bytes数组,数据类型,序列
        '''
        if display > 4:
            return None
        if not isinstance(value,types.ListType):
            return None
        tmp = []
        if display == 1 or display == 3:
            value = value[::-1]
        for b in value:
            if display == 0 or display == 1:
                tmp.append(struct.pack('>H',b))
            else:
                tmp.append(struct.pack('<H',b))
        return struct.unpack('>'+data_type,''.join(tmp))[0]


if __name__ == '__main__':
    msce = ModBus_Struct_Convert()
    print u'#####String <=> ASCII#####'
    print msce.Convert_String_ASCII('ray')
    print msce.Convert_ASCII_String([114, 97, 121])
    print u'#############'
    data = msce.Convert_Dec_Bytes(-12.34,msce.Double,msce.BA_DC_FE_HG)
    print data
    print msce.Convert_Bytes_Dec(data,msce.Double,msce.BA_DC_FE_HG)
