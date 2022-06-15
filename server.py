import socket
import ast
from BST_data import root, searching, insertData, delete
# create Server
class Server:
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 8000

    def runserver(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.server_ip, self.server_port))
        sock.listen(1)
        print(f"[*] Server is starting on {self.server_ip}:{self.server_port}")
        while True:
            client, address = sock.accept()
            print(f"[*] Server is accepted from {address}")
            self.handle_client(client)

    def handle_client(self, client):
        with client:
            message = client.recv(1024)
            print(f"[*] Message from Client: {message.decode('utf-8')}")
            message = message.decode('utf-8')
            try:
                # try method is use for user_dict variable if message is not dictionary get an error
                user_dict = ast.literal_eval(message)
                # sign up
                if 'passcode2' in user_dict.keys():
                    print("I am sign up")
                    global root
                    user = searching(root, user_dict['username'])
                    if user is None:
                        # for temporary
                        username = user_dict['username']
                        passcode = user_dict['passcode']
                        root = insertData(root, username, passcode)
                        with open('BST_data.py', 'a') as file:
                            file.write(f"\nroot = insertData(root, '{user_dict['username']}', '{user_dict['passcode']}')")
                        client.send(bytes("sign in successfully1", 'utf-8'))
                    else:
                        client.send(bytes("user is already registered please login", 'utf-8'))

                # check account
                elif 'check' in user_dict.keys():
                    if searching(root, user_dict['username']):
                        client.send(bytes("You can log in", 'utf-8'))
                    else:
                        client.send(bytes("There is no user", 'utf-8'))
                # delete account
                elif 'delete' in user_dict.keys():
                    user = searching(root, user_dict['username'])
                    if user is not None:
                        username = user_dict['username']
                        passcode = user_dict['passcode']
                        if user.passcode == passcode:
                            delete(root, username)
                            with open('BST_data.py', 'a') as file:
                                file.write(f"\ndelete(root, '{username}')")
                            client.send(bytes("delete account successfully", 'utf-8'))
                        else:
                            client.send(bytes("wrong password try again..", 'utf-8'))
                    else:
                        client.send(bytes("There is no User", 'utf-8'))

                # login account
                elif searching(root, user_dict['username']):
                    user = searching(root, user_dict['username'])
                    if user_dict['passcode'] == user.passcode:
                        client.send(bytes("login successfully", 'utf-8'))
                    else:
                        client.send(bytes("wrong passcode login again", 'utf-8'))
                else:
                    client.send(bytes("There is no user ", 'utf-8'))
            except:
                client.send(bytes(message, 'utf-8'))


if __name__ == '__main__':
    server = Server()
    server.runserver()