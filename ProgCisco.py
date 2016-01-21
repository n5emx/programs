import os.path
#   SFP-A_RJ45-B
#   RJ45-A_SFP-B
#InputFileName = input("Enter filename of tech support dump file:  ")
InputRtrName = input("Router Hostname: ")
InputSN = input("Router Serial Number: ")
InputMgmntIP = input("Enter IP of Management:  ")
InputSM = input("Enter Subnet Mask bits 28,29 or 30:  ")
InputVL = input("Enter Management VLAN:  ")
print ("Description Example:  Joes Pizza | IP/LVXX/001122/WCI" + '\n')
InputDesc = input("Enter Customer Name | Circuit ID:  ")

OutputFile = "c:\\configs\\CiscoMgmt.cfg"

MgmntSM = ""
string = ""
MgmntIP = ""
ConnType = ""
DescGE01 = ""
RtrName = InputRtrName
SerialNum = InputSN

#if(InputConnType == "a"):
#    ConnType = "SFP-A_RJ45-B"
#elif(InputConnType == "b"):
#    ConnType = "RJ45-A_SFP-B"
#else: ConnType = "RJ45-A_RJ45-B"

#print (ConnType)     

if(InputSM == "30"):
    MgmntSM = "255.255.255.252"

if(InputSM == "29"):
    MgmntSM = "255.255.255.248"

if(InputSM == "28"):
    MgmntSM = "255.255.255.240" 

print ("Subnet Mask is: " + MgmntSM)  

# Parse octets in mgmnt string
FirstOctet = int(InputMgmntIP.split(".")[0])
SecondOctet = int(InputMgmntIP.split(".")[1])
ThirdOctet = int(InputMgmntIP.split(".")[2])
LastOctet = int(InputMgmntIP.split(".")[3])

#build GW and IP Octets
MgmtGW = LastOctet + 1
MgmtIP = LastOctet + 2
MgmntIP = str(FirstOctet) +"." + str(SecondOctet) + "." + str(ThirdOctet) + "." + str(MgmtIP)
MgmntGW = str(FirstOctet) +"." + str(SecondOctet) + "." + str(ThirdOctet) + "." + str(MgmtGW)
print (MgmntIP)
print (MgmntGW)
print (OutputFile)


StringLength = len(RtrName) + len(SerialNum) + 8 
if(StringLength > 44):
    PadLength = 0
else: PadLength = 45 - StringLength
print (StringLength)
Pad = " " * PadLength
print(PadLength)
print(Pad)

text_file = open(OutputFile, "w")


#------------------------------------------
text_file.write("hostname " + InputRtrName + '\n')
text_file.write("enable secret W3d3L1v3R247" + '\n')
text_file.write("aaa new-model" + '\n')
text_file.write("aaa authentication login default group tacacs+ local" + '\n')
text_file.write("aaa authentication login ADMIN group tacacs+ local" + '\n')
text_file.write("aaa authentication login PPPCHECK group radius" + '\n')
text_file.write("aaa authentication enable default group tacacs+ enable" + '\n')
text_file.write("aaa authentication ppp PPPCHECK group radius" + '\n')
text_file.write("aaa authorization config-commands" + '\n')
text_file.write("aaa authorization exec default group tacacs+ local" + '\n')
text_file.write("aaa accounting exec action-type start-stop group tacacs+" + '\n')
text_file.write("aaa accounting network action-type start-stop group tacacs+" + '\n')
text_file.write("aaa session-id common" + '\n')
text_file.write("username FrU66L3 secret Th3M0fLi542" + '\n')
text_file.write("int Embedded-Service-Engine 0/0" + '\n')
text_file.write("shutdown" + '\n')
text_file.write("interface GigabitEthernet0/1" + '\n')
text_file.write("description " + DescGE01 + '\n')
text_file.write("no media-type" + '\n')
text_file.write("no ip address" + '\n')
text_file.write("no shutdown" + '\n')
text_file.write("interface GigabitEthernet0/1." + str(InputVL) + '\n')
text_file.write("description MGMT" + '\n')
text_file.write("encapsulation dot1Q " + str(InputVL) + '\n')
text_file.write("ip address " + MgmntIP + " " + MgmntSM + '\n')
text_file.write("no cdp enable" + '\n')
text_file.write("no shutdown" + '\n')
text_file.write("ip forward-protocol nd" + '\n')
text_file.write("ip http server" + '\n')
text_file.write("ip http access-class 23" + '\n')
text_file.write("ip http authentication local" + '\n')
text_file.write("ip http secure-server" + '\n')
text_file.write("ip http timeout-policy idle 60 life 86400 requests 10000" + '\n')
text_file.write("ip route 0.0.0.0 0.0.0.0 " + MgmntGW + '\n')    
text_file.write("ip route 71.30.156.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 71.30.157.0 255.255.255.0 " + MgmntGW + '\n') 
text_file.write("ip route 98.16.254.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 98.16.255.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 162.40.21.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 166.102.0.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 166.102.1.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 166.102.188.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 173.188.111.0 255.255.255.0 " + MgmntGW + '\n') 
text_file.write("ip route 173.221.64.0 255.255.255.0 " + MgmntGW + '\n') 
text_file.write("ip route 173.221.65.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 173.221.66.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("ip route 173.221.67.0 255.255.255.0 " + MgmntGW + '\n')
text_file.write("logging trap debugging" + '\n')
text_file.write("logging source-interface GigabitEthernet0/1." + str(InputVL) + '\n')
text_file.write("snmp-server source-interface traps GigabitEthernet0/1." + str(InputVL) + '\n')
text_file.write("snmp-server trap-source GigabitEthernet0/1." + str(InputVL) + '\n')
text_file.write("logging 173.188.11.156" + '\n')
text_file.write("access-list 10 remark Allows VTY access from certain WINDSTREAM networks" + '\n')
text_file.write("access-list 10 permit 166.102.0.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 166.102.1.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 166.102.188.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 173.188.11.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 162.40.21.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 71.30.156.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 71.30.157.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 98.16.254.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 98.16.255.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 173.221.66.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 173.221.67.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 173.221.64.0 0.0.0.255" + '\n')
text_file.write("access-list 10 permit 173.221.65.0 0.0.0.255" + '\n')
text_file.write("access-list 10 deny   any" + '\n')
text_file.write("access-list 15 remark Allows VTY access to only one address for VTY 5 - 8" + '\n')
text_file.write("access-list 15 permit 166.102.188.37 log" + '\n')
text_file.write("access-list 23 permit 10.10.10.0 0.0.0.7" + '\n')
text_file.write("access-list 97 remark Allows RO SNMP access from certain Netsolve networks" + '\n')
text_file.write("access-list 97 permit 216.141.32.0 0.0.3.255" + '\n')
text_file.write("access-list 97 permit 216.141.39.0 0.0.0.255" + '\n')
text_file.write("access-list 97 deny   any log" + '\n')
text_file.write("access-list 98 remark Allows RO SNMP access from certain WINDSTREAM networks" + '\n')
text_file.write("access-list 98 permit 166.102.0.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 166.102.1.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 166.102.188.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 173.188.11.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 162.40.21.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 71.30.156.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 71.30.157.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 173.221.66.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 173.221.67.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 173.221.64.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 173.221.65.0 0.0.0.255" + '\n')
text_file.write("access-list 98 permit 98.16.249.128 0.0.0.127" + '\n')
text_file.write("access-list 98 deny   any" + '\n')
text_file.write("access-list 99 remark Allows RW SNMP access from certain WINDSTREAM networks" + '\n')
text_file.write("access-list 99 permit 166.102.188.0 0.0.0.255" + '\n')
text_file.write("access-list 99 permit 162.40.21.0 0.0.0.255" + '\n')
text_file.write("access-list 99 permit 173.188.11.0 0.0.0.255" + '\n')
text_file.write("access-list 99 deny   any" + '\n')
text_file.write("no cdp run" + '\n')
text_file.write("snmp-server community a326a7ca RO 98" + '\n')
text_file.write("snmp-server community e8tk3fyb RO 98" + '\n')
text_file.write("snmp-server community j621v7kc RO 98" + '\n')
text_file.write("snmp-server enable traps tty" + '\n')
text_file.write("snmp-server enable traps envmon" + '\n')
text_file.write("snmp-server enable traps config" + '\n')
text_file.write("snmp-server enable traps entity" + '\n')
text_file.write("snmp-server enable traps snmp" + '\n')
text_file.write("snmp-server enable traps snmp linkdown linkup" + '\n')
text_file.write("snmp-server enable traps envmon fan shutdown supply temperature" + '\n')
text_file.write("snmp-server enable traps ipsla" + '\n')
text_file.write("snmp-server enable traps rtr" + '\n')
text_file.write("snmp-server host 162.40.21.25 version 2c a326a7ca" + '\n')
text_file.write("snmp-server host 162.40.21.25 version 2c e8tk3fyb" + '\n')
text_file.write("snmp-server host 98.16.249.140 version 2c j621v7kc" + '\n')
text_file.write("snmp-server host 98.16.249.141 version 2c j621v7kc" + '\n')
text_file.write("snmp-server host 98.16.249.142 version 2c j621v7kc" + '\n')
text_file.write("snmp-server host 98.16.249.143 version 2c j621v7kc" + '\n')
text_file.write("snmp-server host 98.16.249.144 version 2c j621v7kc" + '\n')
text_file.write("tacacs-server host 173.188.111.245" + '\n')
text_file.write("tacacs-server host 166.102.188.246" + '\n')
text_file.write("tacacs-server host 173.188.111.254" + '\n')
text_file.write("tacacs-server directed-request" + '\n')
text_file.write("tacacs-server key 53q49Q4dL7559" + '\n')
text_file.write("radius-server host 166.102.165.73 auth-port 1812 acct-port 1813" + '\n')
text_file.write("radius-server host 166.102.165.74 auth-port 1812 acct-port 1813" + '\n')
text_file.write("radius-server key 7 087349185C1C514245" + '\n')
text_file.write("control-plane" + '\n')
text_file.write("banner login ^" + '\n')
text_file.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + '\n')
text_file.write("$$ Windstream                                 $$" + '\n')
text_file.write("$$ Internet Services                          $$" + '\n')

text_file.write("$$ " + RtrName + "  S/N " + SerialNum  + Pad +"$$" + '\n')
#SRRRRRRRRRRRRRRRRSSSSS/NSNNNNNNNNNNNNNNSPPPPPPPP

text_file.write("$$ UNAUTHORIZED ACCESS IS PROHIBITED          $$" + '\n')
text_file.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + '\n')
text_file.write("^" + '\n')
text_file.write("line 2" + '\n')
text_file.write("access-class 10 in" + '\n')
text_file.write("transport input none" + '\n')
text_file.write("transport output none" + '\n')
text_file.write("line con 0" + '\n')
text_file.write("exec-timeout 15 0" + '\n')
text_file.write("logging synchronous" + '\n')
text_file.write("no modem enable" + '\n')
text_file.write("stopbits 1" + '\n')
text_file.write("line aux 0" + '\n')
text_file.write("line vty 0 4" + '\n')
text_file.write("access-class 10 in" + '\n')
text_file.write("exec-timeout 15 0" + '\n')
text_file.write("privilege level 15" + '\n')
text_file.write("transport input telnet ssh" + '\n')
text_file.write("scheduler max-task-time 5000" + '\n')
text_file.write("end" + '\n')

#close text file
text_file.close()                     
