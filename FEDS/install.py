import subprocess

def wai():
        WAI = open("WAI.txt", "r+")

        if WAI.read() == "NO":

                WAI = open("WAI.txt", "r+")
                loc = input("Where is the location of this file? Example: C://Desktop/FEDS")
                WAI.write(loc)
                loc = ""
wai()
cd
copy "C:\Users\TNTUSER55\Desktop\SOFTWARE DEV\FEDS\FEDS" "C:\Users\TNTUSER55\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\FEDS_Server.py"
