#!/usr/bin/python
mess = """======================================================
             Deface Script Creator        
                        ./Bagas.
======================================================"""
print mess
print "Created by ./BagasCoders"
title = raw_input("Judul title: ")
alertmessage = raw_input("Pesan nya: ")
bgimage = raw_input("link gambar (background): ")
hacked = raw_input("Hacked By: ")
team = raw_input("Team: ")
message = raw_input("Pesan. gunakan kode <br> untuk text selanjutnya! : ")
thanks = raw_input("Thanks To: ")
soundcloudid = raw_input("soundcloud id (MUSIK): ")


#Open the index
fo = open("script.html","w")

messagescript1 = """<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
     <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.75, shrink-to-fit=no">
    <meta name="description" content="I Am Sadd Boy">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Mali:400i,700i" rel="stylesheet" type="text/css">
    <link rel="icon" href="https://images4.alphacoders.com/220/220444.jpg" type="image/jpg">
    <link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.7.1/css/all.css' integrity='sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr' crossorigin='anonymous'><title>"""

messagescript2 = title

messagescript3 = """</title></head>"""

messagescript4 = """<body><script>alert('"""

messagescript5 = alertmessage

messagescript6 = """')</script>"""

messagescript7 = """<style>
    	html,body,.container{
    		background: url("""

messagescript8 = bgimage 

messagescript9 = """) no-repeat center center/cover;
    		position: fixed;
    		margin: auto;
    		height: 100%;
    		top: 0; bottom: 0; left: 0; right:0;
    	}
    	.page{
    		position: absolute;
    		margin: auto;
    		height: 50%;
    		top: 0; bottom: 0; left: 0; right:0;
    	}
    	.mek{
    		background-color:rgba(0,0,0,0.7);
    	}
    	h1{
    		transform:rotate(-12deg); 
    		-moz-transform:rotate(-12deg); 
    		-webkit-transform:rotate(-12deg); 
    		-o-transform:rotate(-12deg);
    		font-family: "Mali";
    		font-size: 2em;
    		font-weight: bold;
    		margin-bottom: 15%;
    	}
    	h5{
    		font-family: "Mali";
    	}
    	.logo{
    		text-decoration: none;
    		color: white;
    		font-size: 22px;
    		margin: 10px;
    	}
    	.logo:hover{
    		text-decoration: none;
    		color: white;
    		cursor: pointer;
    	}
    	.hastag{
    		text-decoration: none;
    		color: white;
    	}
    </style>
  </head>
  <body>
  	
    <div class="container">"""

messagescript10 = """       <div class="page">
<h1 class="text-center text-white">"""

messagescript11 = hacked

messagescript12 = """</h1>"""

messagescript13 = """<div class="mek">
    		<h5 class="text-center text-white mb-3"><hr>"""

messagescript14 = message 

messagescript15 = """</div><marquee class="mr-5 ml-5"><a class="hastag" href="#">"""

messagescript16 = thanks

messagescript17 = """</a></marquee></h5>
    		<center>
    		<a class="logo" href="">
    			<i class="fab fa-whatsapp"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-hackerrank"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-github"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fas fa-globe"></i>
    		</a>
    		<a class="logo" href="">
    			<i class="fab fa-blogger"></i>
    		</a>
    		</center>
    	</div>
    </div>
"""

messagescript18 = """<iframe width="0" height="0" scrolling="no" frameborder="no" allow="autoplay" src="https://api.soundcloud.com/tracks/"""

messagescript19 = soundcloudid

messagescript20 = """/stream?client_id=a3e059563d7fd3372b49b37f00a00bcf" ></iframe>
  </body>
  </html>"""


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

print "Script Jadi Tinggal Pindahin"
 
print "Kontak? : +6282228270627"

fo.close()
