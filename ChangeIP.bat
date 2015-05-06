@echo Off
color 1F
echo This works best if you hard code the following into your LAN
echo DNS settings. Option 2 will not reset your DNS settings  
echo                 DNS 1: 10.104.76.23   Windstream Private
echo                 DNS 2: 166.102.165.11 Windstream Public
echo                 DNS 3: 8.8.8.8        Google Public
echo.
echo   DNS 1 will fail if you are connecting to a customers WAN connection for 
echo   testing, the next server is public and should work, if all else fails 
echo   the Google server will catch it if you have access to the Internet
echo               ___________________________________________________________
echo              ^|                                                          ^|
echo              ^| 1.   Change IP Address                                   ^|
echo              ^|                                                          ^|
echo              ^| 2.   Reset IP to DHCP                                    ^|
echo              ^|                                                          ^|
echo              ^| 3.   Release / Renew IP                                  ^|
echo              ^|                                                          ^|
echo              ^| 4.   Same as #1, but no prompts, allows disabling of LAN ^|
echo              ^|         computer will have an IP of 10.10.10.xx          ^|
echo              ^| 5.   Future use                                          ^|
echo              ^|                                                          ^|
echo              ^| 6.   Quit                                                ^|
echo              ^|                                                          ^|
echo              ^|_________________________________________________________ ^|


set /p MenuCmd=Enter Option:
if /i {%MenuCmd%}=={1} (goto :command1)
if /i {%MenuCmd%}=={2} (goto :command2)
if /i {%MenuCmd%}=={3} (goto :command3)
if /i {%MenuCmd%}=={4} (goto :command4)
if /i {%MenuCmd%}=={5} (goto :command5)
if /i {%MenuCmd%}=={6} (goto :command6)



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
goto end

:nogw

echo ______________
echo %IP4%
echo %Mask%
echo %GW%
netsh interface ipv4 set address "Local Area Connection" static %IP4% %Mask%
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto end


:command1
goto jump

:command2
netsh interface ipv4 set address "Local Area Connection" source=dhcp


:command3
ipconfig /release
echo.
ipconfig /renew
echo.
goto end

:command4


set /a str="rand=%random% %% 200"
echo IP is 10.10.10.%str%
echo msgbox("10.10.10.%str%" ,0, "IP Address") > c:\ip.vbs
echo.%str%


call c:\windows\system32\wscript.exe c:\ip.vbs
pause

netsh interface ipv4 set address "Local Area Connection" static 10.10.10.%str% 255.255.255.0
netsh interface set interface "Local Area Connection" DISABLED 
netsh interface set interface "Local Area Connection" ENABLED
goto end

:command5

:command6
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