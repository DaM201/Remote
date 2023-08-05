import sys, time, socket, threading, os

os.system('clear')

class colors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[31m'
    pink = '\033[35m'





def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


nickname = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 4444
client.connect((server, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print(bcolor.red + "[ERROR] An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}{}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

hreading.Thread(target=write)
write_thread.start()