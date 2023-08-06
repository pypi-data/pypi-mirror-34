import paramiko
import time
import os

def ssh_connect(device_ip):
    print("Connecting to: " + device_ip)
    hostname = device_ip
    username = "administrator"
    password = "password"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    channel = client.invoke_shell()

    print("Successfully connected to: " + device_ip)
    return client, channel


def psend(command, channel):

    channel.send(command)


def pwait(waitstr, channel, tout=0):
    startTime = int(time.time())
    stroutput = ''
    while waitstr not in stroutput:
        currentTime = int(time.time())
        if channel.recv_ready():
            try:
                current = channel.recv(9999).decode()
                stroutput += current
                if current.strip() != '':
                    print(current, end='')
            except:
                continue

        if tout != 0:
            if (currentTime - startTime) > tout:
                try:
                    if current.strip() != '':
                        print(current, end='')
                except:
                    pass
                return stroutput

    return stroutput

def twait(phrase, tn, tout = -1, logging = 'off', rcontent = False):

    # Adding code to allow lists for phrase
    finalcontent = ' '

    #This is the time of the epoch
    startTime = int(time.time())
    while True:
        # This is the current time
        currentTime = int(time.time())
        if tout != -1:

            # This is the time since the start of this loop
            # if it exceeds the timeout value passed to it
            # then exit with a return of 0
            if (currentTime - startTime) > tout:
                if logging == 'on':
                    #Adding the -e-e-> to differentiate from device output
                    print('-e-e->It has been ' + str(tout) +  ' seconds. Timeout!')
                if rcontent == False:
                    return 0
                else:
                    return 0, finalcontent
        # Eager reading back from the device
        content = (tn.read_very_eager().decode().strip())

        if content.strip() != '':
            finalcontent += content
        # if the returned content isn't blank. This stops
        # it from spamming new line characters
        if content.strip() != '':
            print (content, end='')
        # content was found! Return a 1 for success
        if type(phrase) is str:
            if phrase in content:
                if rcontent == False:
                    return 1
                else:
                    return 1, finalcontent

        if type(phrase) is list:

            count = 1
            for p in phrase:
                if p in content:

                    if rcontent == False:
                        return count
                    else:
                        return count, finalcontent
                count+=1

def tsend(phrase, tn):

    #Sends the phrase that was passed to it as bytes
    tn.write(phrase.encode())

    return

def shortfiles(parentdir, extensions=[]):
    TotalFiles = []
    if extensions == []:
        for root, directories, filenames in os.walk(parentdir):
            for filename in filenames:
                TotalFiles.append(filename)

    elif extensions != []:
        for root, directories, filenames in os.walk(parentdir):
            for filename in filenames:
                for ext in extensions:
                    if ext in filename:
                        TotalFiles.append(filename)

    return TotalFiles

def longfiles(parentdir, extensions=[]):
    TotalFiles = []
    if extensions == []:
        for root, directories, filenames in os.walk(parentdir):
            for filename in filenames:
                TotalFiles.append(os.path.join(root, filename))

    elif extensions != []:
        for root, directories, filenames in os.walk(parentdir):
            for filename in filenames:
                for ext in extensions:
                    if ext in os.path.join(root, filename):
                        TotalFiles.append(os.path.join(root, filename))

    return TotalFiles