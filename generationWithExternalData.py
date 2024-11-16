from ast import main
import os
import pandas as pd
import openpyxl
import numpy as np

XlsxPath = "./test.xlsx"
findThis = 326
avpList = [str]
userList = [str]
licenseList = [str]
dmapList = [int]
gateIpList = [str]
clientIpList = [str]

def main():
    print("main")
    openXlsx()
    for findThis in range(537, 540):
        shporaGeneration(findThis)        
        batGeneration(findThis)
        configGeneration(findThis)
    print("EndPoint")    

def openXlsx():
    wookbook = openpyxl.load_workbook(XlsxPath)
    worksheet = wookbook.active
    for i in range(1, worksheet.max_row):
        avpList.append(str(worksheet[i][1].value))
        userList.append(str(worksheet[i][2].value))
        licenseList.append(str(worksheet[i][4].value))
        dmapList.append((worksheet[i][13].value))
        gateIpList.append(str(worksheet[i][16].value))
        clientIpList.append(str(worksheet[i][17].value))
        
    print (avpList[dmapList.index(findThis)]+' '+userList[dmapList.index(findThis)]+' '+
           licenseList[dmapList.index(findThis)]+' '+str(dmapList[dmapList.index(findThis)])+' '+
           gateIpList[dmapList.index(findThis)]+' '+clientIpList[dmapList.index(findThis)])
    #print(dmapList[0])

def shporaGeneration(i):        
    #create dir
    make_dir_arg = userList[dmapList.index(i)] + '_' + avpList[dmapList.index(i)]
    old_file = 'ШпаргалкаТест.txt'
    try:
        os.mkdir(make_dir_arg)
    except:
        print("Есть такая дирректория " + make_dir_arg)
    #open file
    file = open( old_file , 'rt' )
    #print(file.read())
    #create tmp file
    temp_file_str = file.read()
    file.close()
    #change user number
    f = temp_file_str.replace('uUUUU', userList[dmapList.index(i)])
    temp_file_str = f
    #change serial number
    f = temp_file_str.replace('AAAAAAAAA', avpList[dmapList.index(i)][3:13])
    temp_file_str = f
    #change license number
    f = temp_file_str.replace('LNLLLLL', 'LN' + licenseList[dmapList.index(i)])
    new_file = open(userList[dmapList.index(i)] + '_' + avpList[dmapList.index(i)] + '\\Шпаргалка.txt','w')
    new_file.write(f)
    new_file.close()
    #print(f)

def batGeneration(i):
    #generate bat
    old_bat = 'usbTest.bat'
    #open file
    bat = open( old_bat , 'rt' )
    temp_bat_str = bat.read()
    bat.close()
    #change user
    b = temp_bat_str.replace('uUUUU', userList[dmapList.index(i)])
    temp_bat_str = b
    #change serial number
    b = temp_bat_str.replace('AAAAAAAAA', avpList[dmapList.index(i)][3:13])
    temp_bat_str = b
    #change license number
    b = temp_bat_str.replace('LNLLLLL', 'LN' + licenseList[dmapList.index(i)])
    new_bat = open(userList[dmapList.index(i)] + '_' + avpList[dmapList.index(i)] + '\\usb.bat','w')
    new_bat.write(b)
    new_bat.close()
    #print(b)

def configGeneration(i):    
    old_file = 'ConfigTest.txt'
    file = open( old_file , 'rt' )
    #print(file.read())
    temp_file_str = file.read()
    file.close()
    #user change
    f = temp_file_str.replace('uUUUU', userList[dmapList.index(i)])
    temp_file_str = f
    #DMAP change
    f = temp_file_str.replace("DMAP DDD", "DMAP " + str(dmapList[dmapList.index(i)]))
    temp_file_str = f
    #IP change
    if clientIpList[dmapList.index(i)][2] == '.' or clientIpList[dmapList.index(i)][2] == ' ':
        
        f = temp_file_str.replace("XX.XXX.XXX.XXX", clientIpList[dmapList.index(i)][0:2] + '.'
                                                    + clientIpList[dmapList.index(i)][3:6] + '.'
                                                    + clientIpList[dmapList.index(i)][7:10] + '.'
                                                    + clientIpList[dmapList.index(i)][11:])
        temp_file_str = f
        #POOL change
        f = temp_file_str.replace("III-III-III", clientIpList[dmapList.index(i)][3:6] + '-'
                                                    + clientIpList[dmapList.index(i)][7:10] + '-'
                                                    + clientIpList[dmapList.index(i)][11:])
    else:
        f = temp_file_str.replace("XX.XXX.XXX.XXX", clientIpList[dmapList.index(i)][0:2] + '.'
                                                    + clientIpList[dmapList.index(i)][2:5] + '.'
                                                    + clientIpList[dmapList.index(i)][5:8] + '.'
                                                    + clientIpList[dmapList.index(i)][8:])
        temp_file_str = f
        #POOL change
        f = temp_file_str.replace("III-III-III", clientIpList[dmapList.index(i)][2:5] + '-'
                                                    + clientIpList[dmapList.index(i)][5:8] + '-'
                                                    + clientIpList[dmapList.index(i)][8:])            
    new_file = open(userList[dmapList.index(i)] + '_' + avpList[dmapList.index(i)]
                             + '\\Config' + userList[dmapList.index(i)] + '.txt','w')
    new_file.write(f)
    new_file.close()



if __name__ == "__main__":main()