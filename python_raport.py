import sys
import os
nazwa = str(sys.argv[1])
plikWyjsciowy = open("index.html", "a+")
template =""
if(os.stat("index.html").st_size == 0):
    template = """
    <html>
    <head>
    <title>Raport</title>
    <link rel="stylesheet" href="styl.css">
    <style>
    body{
    background: #a0d8ef;
    background: -moz-linear-gradient(top,  #a0d8ef 0%, #ddffff 80%);
    background: -webkit-linear-gradient(top,  #a0d8ef 0%,#ddffff 80%);
    background: linear-gradient(to bottom,  #a0d8ef 0%,#ddffff 80%);
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#a0d8ef', endColorstr='#ddffff',GradientType=0 );
    }

    *{
    font-family: "Arial";
    }
    table{
	
    margin: auto;
    margin-top: 20px;
    border-collapse: collapse;
    }

    .lewa, .t-lewa{
    text-align: right;
    padding-right: 10px;
    border-right: 1px solid #8c8c8c;
    padding-top: 3px;
    }

    .prawa, .t-prawa{
    text-align: left;
    padding-left: 10px;
    border-left: 1px solid #8c8c8c;
    padding-top: 3px;
    }

    .t-lewa, .t-prawa{
    border-bottom: 1px solid #8c8c8c;
    padding-bottom: 10px;
    }

    .suma{
    border-top: 1px solid #8c8c8c;
    }

    .true, .false, .error {
    font-weight: 700;
    }

    .true{
    color: #2d862d;
    }

    .false{
    color: #b30000;
    }
    </style>
    </head>
    <body>"""
    

plikWejsciowy = open(nazwa, "r")
template += "<p>Plik:  "+str(nazwa)+"</p>"
wiersz = plikWejsciowy.readlines()
blad = 0
zapr = 0
niezap = 0
for linia in wiersz:
    if("b" in linia):
        template += """
        <p class="error">Wiersz w pliku wejsciowym zawiera bledne dane</p>
        """
        blad += 1
    else:
        liczby = linia.split()
        if(liczby[2] == "t"):
            template += """
            <p class="true"> Liczby """ + str(liczby[0]) + """ oraz """ + str(liczby[1]) + """ sa zaprzyjaznione </p>
            """
            zapr += 1
        else:
            template += """
            <p class ="false"> Liczby """ + str(liczby[0]) + """ oraz """ + str(liczby[1]) + """ nie sa zaprzyjaznione </p>
            """
            niezap += 1
template += "<p>Ilosc blednych danych w pliku: " + str(blad) + "</p>"
template += "<p>Ilosc par zaprzyjaznionych: " + str(zapr) + "</p>"
template += "<p>Ilosc par niezaprzyjaznionych: " + str(niezap) + "</p>"
plikWyjsciowy.write(template)
plikWejsciowy.close()
plikWyjsciowy.close()