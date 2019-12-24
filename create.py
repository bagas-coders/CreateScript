#!/usr/bin/python
mess = """[+]======================================================[+]
[+]                Script Deface Creator                 [+]
[+]                 <> By ./Bagass. </>                  [+]
[+]======================================================[+]"""
print mess
print "[+] Created by ./BagasCoders [+]"
print "[+] Version : 1.5            [+]"
title =        raw_input("[+] Judul title             : ")
print "Link gambar tengah/logo jpg, png, jpeg, gif,"
print "(kalo gapunya bikin abis tu upload di https://up.top4top.net )"
gambartengah = raw_input("[+] Link gambar tengah/logo : ")
print "Ukuran gambar/logo (biasanya 400-500an tapi suka2 kalian aja dah"
ukurangambar = raw_input("[+] Ukuran gambar/logo      : ")
print "Note khusus warna warna an pake bahasa inggris ya"
warnaheked = raw_input  ("[+] Warna Hacked By         : ")
print "Ukuran font mek jangan gede gede nanti jelek kek muka lu awikwok:v"
hackedby = raw_input    ("[+] Hacked By?              : ")
print "Warna text biar ngeri ya nggak?:v"
warnateks = raw_input   ("[+] Warna text              : ")
print "Gunakan <br> untuk mengganti baris"
kata = raw_input        ("[+] Kata-kata               : ")
greets = raw_input      ("[+] Thanks To?              : ")
print "Kalo mau upload music di https://up.top4top.net"
musiclink = raw_input   ("[+] Music Link??            : ")
#Open the index
fo = open("index.html","w")

messagescript1 = """<html>
    <link href="http://fonts.googleapis.com/css?family=New Rocker" rel="stylesheet" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=0.75, shrink-to-fit=no">
    <meta property="og:image" content='"""
messagescript2 = gambartengah 
messagescript3 = """'>
    <meta property="og:description" content="#IndoesianDefacerRuler">
    <meta property="og:site_name" content="#IndonesianHackerRuler">
    <link rel="icon" type="image/png" href='"""
messagescript4 = gambartengah 
messagescript5 = """'><html><head><title>"""
messagescript6 = title 
messagescript7 ="""</title><br><br><br><br><center><img src='"""
messagescript8 = gambartengah 
messagescript9 = """'width='"""
messagescript10 = ukurangambar
messagescript11 = """'>
<body bgcolor="black">
<script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"></script>
<br><br><center><font face='Courier New' size='4' color='"""
messagescript12 = warnaheked 
messagescript13 = """'>Hacked By"""
messagescript14 = hackedby
messagescript15 = """<br><font face='Courier New' size='5px' color='"""
messagescript16 = warnateks
messagescript17 = """'>"""
messagescript18 = kata
messagescript19 = """</font></center>"""
messagescript20 = """<br>"""
messagescript21 = """<center><font face="Courier New" size="5" color="white"> -::GREETS::- <br><br>
        <marquee scrollamount="10">"""
messagescript22 = greets
messagescript23 = """</marquee>
<center><audio src='"""
messagescript24 = musiclink
messagescript25 = """' controls></audio><br><br><center><font face="Courier New" color="red" size="5" >#<font face="Courier New" color="white" size="5" >IndonesianDefacerRulers</center><hr color="red"></hr></html>"""

fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)
fo.write(messagescript17)
fo.write(messagescript18)
fo.write(messagescript19)
fo.write(messagescript20)
fo.write(messagescript21)
fo.write(messagescript22)
fo.write(messagescript23)
fo.write(messagescript24)
fo.write(messagescript25)

print "Script Jadi Tinggal Pindahin"

print "Cara memindahkan $ mv index.html /sdcard"
