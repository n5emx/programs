@echo Off
:start
color 1F
cls
echo. 
echo. 
echo                 DNS 1: 10.104.76.23   Windstream Private
echo                 DNS 2: 166.102.165.11 Windstream Public
echo                 DNS 3: 8.8.8.8        Google Public
echo.
echo.
echo.
echo               ___________________________________________________________
echo              ^|                                                          ^|
echo              ^| 1.   Change IP Address                                   ^|
echo              ^|                                                          ^|
echo              ^| 2.   Reset IP to DHCP                                    ^|
echo              ^|                                                          ^|
echo              ^| 3.   Release / Renew IP                                  ^|
echo              ^|                                                          ^|
echo              ^| 4.   Disable Wired LAN / Program random IP               ^|
echo              ^|                                                          ^|
echo              ^| 5.   Config for MetroNID                                          ^|
echo              ^|                                                          ^|
echo              ^| 6.   Help!                                               ^|
echo              ^|                                                          ^|
echo              ^| 7.   Quit                                                ^|
echo              ^|                                                          ^|
echo              ^|_________________________________________________________ ^|


set /p MenuCmd=Enter Option:
if /i {%MenuCmd%}=={1} (goto :command1)
if /i {%MenuCmd%}=={2} (goto :command2)
if /i {%MenuCmd%}=={3} (goto :command3)
if /i {%MenuCmd%}=={4} (goto :command4)
if /i {%MenuCmd%}=={5} (goto :command5)
if /i {%MenuCmd%}=={6} (goto :commandH)
if /i {%MenuCmd%}=={7} (goto :command7)



:jump
set /p IP4=Enter IPv4 Address:

CLS
goto printMaskMenu

:jumpbak



set /p GW=Enter Gateway(0 for none):
if /i {%GW%}=={0} (goto :nogw)

echo ______________
echo %IP4%
echo %Mask%
echo %GW%
netsh interface ipv4 set address "Local Area Connection" static %IP4% %Mask% %GW%
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto command5

:nogw

echo ______________
echo %IP4%
echo %Mask%
netsh interface ipv4 set address "Local Area Connection" static %IP4% %Mask%
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto command5


:command1
goto jump

:command2
netsh interface ipv4 set address "Local Area Connection" source=dhcp
REM ipconfig /release > null
ipconfig /flushdns
ipconfig /renew > null
goto command6

:command3
ipconfig /release
ipconfig /renew
goto start

:command4


set /a str="rand=%random% %% 200"
echo IP is 10.10.10.%str%
echo x = msgbox("10.10.10.%str%" ,0, "IP Address") > c:\ip.vbs
echo.%str%


call c:\windows\system32\wscript.exe c:\ip.vbs


netsh interface ipv4 set address "Local Area Connection" static 10.10.10.%str% 255.255.255.0
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto start

:command5
netsh interface ipv4 set address "Local Area Connection" static 192.168.1.250 255.255.255.0
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto start


:command6
netsh interface ip set dnsservers name="Local Area Connection" source=dhcp
goto start

:commandH
cls
color F1
type ChangeIP_help.txt
pause
goto start

:command7
goto end







:slash21
set Mask=255.255.248.0
goto jumpbak

:slash22
set Mask=255.255.252.0
goto jumpbak

:slash23
set Mask=255.255.254.0
goto jumpbak

:slash24
set Mask=255.255.255.0
goto jumpbak

:slash25
set Mask=255.255.255.128
goto jumpbak

:slash26
set Mask=255.255.255.192
goto jumpbak

:slash27
set Mask=255.255.255.224
goto jumpbak

:slash28
set Mask=255.255.255.240
goto jumpbak

:slash29
set Mask=255.255.255.248
goto jumpbak

:slash30
set Mask=255.255.255.252
goto jumpbak

:slash31
set Mask=255.255.255.254
goto jumpbak

:slash32
set /p Mask=Enter NetMask:
goto jumpbak





:printMaskMenu
echo.
echo                     Preconfigured Network Mask Menu 
echo               ____________________________________________
echo              ^|                                            ^|
echo              ^| 1.   /21  255.255.248.0       2046 Usable  ^|
echo              ^| 2.   /22  255.255.252.0       1022 Usable  ^|
echo              ^| 3.   /23  255.255.254.0       510  Usable  ^|
echo              ^| 4.   /24  255.255.255.0       254  Usable  ^|
echo              ^| 5.   /25  255.255.255.128     126  Usable  ^|
echo              ^| 6.   /26  255.255.255.192     62   Usable  ^|
echo              ^| 7.   /27  255.255.255.224     30   Usable  ^|
echo              ^| 8.   /28  255.255.255.240     14   Usable  ^|
echo              ^| 9.   /29  255.255.255.248     6    Usable  ^|
echo              ^| A.   /30  255.255.255.252     4*   Usable  ^|
echo              ^| B.   /31  255.255.255.224     2*   Usable  ^|
echo              ^| C.   User Defined                          ^|
echo              ^|___________________________________________ ^|


set /p MenuMask=Enter NetMask:
if /i {%MenuMask%}=={1} (goto :slash21)
if /i {%MenuMask%}=={2} (goto :slash22)
if /i {%MenuMask%}=={3} (goto :slash23)
if /i {%MenuMask%}=={4} (goto :slash24)
if /i {%MenuMask%}=={5} (goto :slash25)
if /i {%MenuMask%}=={6} (goto :slash26)
if /i {%MenuMask%}=={7} (goto :slash27)
if /i {%MenuMask%}=={8} (goto :slash28)
if /i {%MenuMask%}=={9} (goto :slash29)
if /i {%MenuMask%}=={a} (goto :slash30)
if /i {%MenuMask%}=={b} (goto :slash31)
if /i {%MenuMask%}=={c} (goto :slash32)


:end
color 0F