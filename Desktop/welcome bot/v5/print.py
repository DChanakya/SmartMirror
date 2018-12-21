import subprocess


##img2pdf new.jpg --imgsize 58mmx74mm -o new.pdf
subprocess.run(["img2pdf","new.jpg","--imgsize","58mmx74mm","-o","new.pdf"])
subprocess.run(["lpr","-P","Usb-Printer","new.pdf"])
##subprocess.run(["lpr","-o"," landscape" ,"-o ","fit-to-page","-P", "Usb-Printer", "new.jpg"])
##subprocess.run(["lpr", "-P", "Usb-Printer", "details.txt"])
