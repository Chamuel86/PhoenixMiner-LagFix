import os, time, subprocess

target_miner = 'start_miner.bat' #miner start file, works with .bat extension
time_woke = 1.5 #time that this python script will run the miner, in hours
counter = 0 

def runMiner(miner):
    print(u"\u001b[32m" + "Starting Miner..." + u"\u001b[0m")
    subprocess.Popen(\
    [target_miner],
    creationflags = subprocess.CREATE_NEW_CONSOLE,
    ).pid

while True:    
    runMiner(target_miner)
    time.sleep(time_woke * 3600)
    print(u"\u001b[33m" + "Stopping miner..." + u"\u001b[0m")
    os.system("TASKKILL /F /im cmd.exe")
    os.system("TASKKILL /F /im PhoenixMiner.exe")
    print(u"\u001b[35m" + "Miner Finished." + u"\u001b[00m")
    time.sleep(1)
    if counter == 2: # 2 -> times that the script will run the miner before restart windows
        os.system("shutdown /r /t 0")
    else:
        counter += 1