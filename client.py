#client
import socket
import ast
class Client:
    def __init__(self, client_mes):
        self.target_ip = 'localhost'
        self.target_port = 8000
        self.message = client_mes

    def runClient(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        if self.message == '1':
            user = {}
            user['username'] = input("Enter your username : ").strip()
            user['passcode'] = input("Enter your passcode : ").strip()
            user_str = f"{user}"
            to_send = bytes(user_str, 'utf-8')
            client.send(to_send)
        elif self.message == '2':
            user = {}
            user['username'] = input("Enter your username : ").strip()
            user['passcode'] = input("Enter your passcode : ").strip()
            user['passcode2'] = input("retype your passcode for comfirm : ").strip()
            if user['passcode'] == user['passcode2']:
                user_str = f"{user}"
                to_send = bytes(user_str, 'utf-8')
                client.send(to_send)
            else:
                print("wrong passcode re sign up")
                client.send(bytes(" ", 'utf-8'))
        elif self.message == '3':
            user = {}
            user['username']= input("Enter your username : ").strip()
            user['check'] = True
            user_str = f"{user}"
            to_send = bytes(user_str, 'utf-8')
            client.send(to_send)
        elif self.message == '4':
            user = {}
            user['username'] = input("Enter your username : ").strip()
            user['passcode'] = input("Enter your passcode : ").strip()
            user['delete'] = True
            user_str = f"{user}"
            to_send = bytes(user_str, 'utf-8')
            client.send(to_send)
        elif self.message == '5':
            client.send(bytes("Have a nice day!", 'utf-8'))
        else:
            client.send(bytes("please type 1 or 2 or 3 or 4 or 5: ", 'utf-8'))
        print(f"{client.recv(1024).decode('utf-8')}")
        client.close()


if __name__ == '__main__':
    stop = False
    while not stop:
        client_message = input("1.login | 2.sign up | 3.check username is already registered | 4.delete account | 5.exit\n $: ").strip()
        client = Client(client_mes=client_message)
        client.runClient()
        if client_message == '5':
            stop = True