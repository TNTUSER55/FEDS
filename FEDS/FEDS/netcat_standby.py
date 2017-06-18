import subprocess #imports the subprocess module
def nc():

    subprocess.call("nc -lvp 6666>outputfromstandyby.txt", shell=True)

    print("after the subp")
