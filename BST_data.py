from sort_string import sort_string

class Node:
    def __init__(self, username,passcode):
        self.username = username
        self.passcode = passcode
        self.left = None
        self.right = None

# create
def insertData(root, username, passcode):
    if root is None:
        return Node(username, passcode)
    if sort_string(username, root.username) is True:
        print("user is already registered")
        return root
    elif sort_string(username, root.username) == 'first':
        root.left = insertData(root.left, username, passcode)
    elif (sort_string(username, root.username) == 'second') or (sort_string(username, root.username) is False):
        root.right = insertData(root.right, username, passcode)
    return root

#read
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(f"username: {root.username}, passcode: {root.passcode}")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(f"username: {root.username}, passcode: {root.passcode}")
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(f"username: {root.username}, passcode: {root.passcode}")

def searching(root, username):
    if root is None:
        return root
    if root.username == username:
        return root
    if  sort_string(username, root.username) == 'first':
        return searching(root.left, username)
    if (sort_string(username, root.username) == 'second') or (sort_string(username, root.username) is False):
        return searching(root.right, username)


#delete
def delete(root, username):
    if root is None:
        return root
    elif sort_string(username, root.username) == 'first':
        root.left = delete(root.left, username)
    elif (sort_string(username, root.username) == 'second') or (sort_string(username, root.username) is False):
        root.right = delete(root.right, username)
    else:
        if root.right is None:
            root = None
            return None
        temp = minValue(root.right)
        root.username = temp.username
        root.passcode = temp.passcode
        root.right = delete(root.right, root.username)
    return root

def minValue(root):
    temp = root
    while(temp.left is not None):
        temp = temp.left
    return temp

root = Node("biden", 'admin')
root = insertData(root, "aung", 'password2')
root = insertData(root, "brohn", 'password3')
root = insertData(root, "zaw", 'passcode')
root = insertData(root, 'zawyehan', '3541')
# create user from clients

root = insertData(root, 'aungkyawtun', '1234')