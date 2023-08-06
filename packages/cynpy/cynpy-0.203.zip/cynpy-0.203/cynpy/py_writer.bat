
rem *** pre-start ***
rem power-on the I2C-to-CC (CSP) bridge
rem try the CSP bridge
rem try the CSP target (DUT)
rem ===============================================================================
rem python -mcynpy.aardv   sw
rem python -mcynpy.can11xx rev
rem python -mcynpy.can11xx dump
rem python -mcynpy.csp     query
rem python -mcynpy.csp     rev
rem python -mcynpy.csp     dump
rem python -mcynpy.csp 1   dump b0 30
rem python -mcynpy.csp     stop
rem python -mcynpy.csp     nvm


rem prepare the bin file for temporary
rem ===============================================================================
rem python -B c:\Python27\Scripts\hex2bin.py ..\fw\cy2311r3\Objects\cy2311r3_x004.hex > temp.bin
    python -B c:\Python27\Scripts\hex2bin.py z:\RD\Project\CAN1112\Ray\fw\cy2332r0_20180807.hex > temp.bin


rem stop MCU
rem ===============================================================================
    python -mcynpy.csp stop


rem ES may be not fully trimmed but OSC. Complete the row of CP trim
rem ===============================================================================
rem python -mcynpy.csp prog_hex 1 940    ff 00 0a 00 00 ff
rem python -mcynpy.csp prog_hex 1 944 ff 4d 00 0a 00 00
rem python -mcynpy.csp prog_hex 1 94a    4d 00 0a 00 00 ff
    python -mcynpy.csp trim


rem upload FW
rem ===============================================================================
    python -mcynpy.csp upload temp.bin 1
rem python -mcynpy.csp upload ..\fw\cy2311r3\Objects\cy2311r3_20180606.2.memh 1
rem python -mcynpy.csp upload ..\fw\scp\phy20180605a_prl0605\scp\Objects\scp_20180613.2.memh 1


rem compare
rem ===============================================================================
    python -mcynpy.csp comp   temp.bin ^
                                       900=CAN1112A-000 ^
                                       910=AP4377-14L ^
                                       33=\90 34=\09 35=\40 36=\E4 37=\93 38=\F5 39=\A2 3A=\80 3B=\FE ^
                                       940=\00 941=\FF 942=\FF 943=\FF 944=\FF


rem FT information
rem writer information
rem option table
rem PDO table
rem mapping table
rem ===============================================================================
rem python -mcynpy.csp prog_asc 1 910 CAN1112A28L_BIN1
    python -mcynpy.csp prog_str 1 930 PY187_%DATE:~2,2%%DATE:~5,2%%DATE:~8,2%%TIME:~0,2%%TIME:~3,2%
    python -mcynpy.csp prog_hex 1 960 02 08 00 00

rem 2-PDO (5V/3A, 3.3-5.9V/3A, 15W)
    python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  3C 21 76 C0

rem 3-PDO (5V/3A, 9V/3A, 3.3-11V/3A, 27W)
rem python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  2C D1 02 00  3C 21 DC C0
rem python -mcynpy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE 13 E8 C1 F4 11 F4 B2 E4

rem 5-PDO (3.5V/3A, 5V/3A, 6V/3A, 7.3V/3A, 10V/2.2A, 22W)
rem python -mcynpy.csp   prog_hex 1 970 2C 19 01 0A  2C 91 01 00  2C E1 01 00  2C 49 02 00  DC 20 03 00
rem python -mcynpy.csp   prog_hex 1 a20    10 AF        50 FA        01 2C        11 6D        C1 F4     11 F4 62 E4

rem python -mcynpy.csp 1 prog_hex 1 98c 2C 19 01 0A  2C 91 01 00  2C E1 01 00  2C 49 02 00  DC 20 03 00
rem python -mcynpy.csp 1 prog_hex 1 98c 2C 91 01 0A  3C 21 76 C0
rem python -mcynpy.csp 1 prog_hex 1 9a8 2C 91 01 0A  3C 21 76 C0


rem reset MCU
rem ===============================================================================
rem python -mcynpy.csp write F7 01 01 01
rem python -mcynpy.csp reset

    del temp.bin
