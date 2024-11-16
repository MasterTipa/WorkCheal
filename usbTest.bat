@echo off 
CD c:\Program1\Utils\avpassinit
AvPassInit.exe -pin=AAAAAAAAA
CD C:\Program Files (x86)\Bel VPN Client AdminTool av
cryptocont.exe n -n=av:AVPAAAAAAAAA:uUUUU-2024 -p=AAAAAAAAA
cryptocont.exe l
cryptocont.exe r -f=c:\BVPN\uUUUU_AVPAAAAAAAAA\uUUUU-2024_LNLLLLL.req -n=av:AVPAAAAAAAAA:uUUUU-2024 -p=AAAAAAAAA -cn=uUUUU -c=BY -o=BELTELECOM -t=RSMOB -e=uUUUU@rsmob.beltelecom.by
pause