class Node:
    def __init__(self, value, parent=None) -> None:
        self.value = value
        self.parent = parent # Referencia al padre
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    # ---------------  ZIG -------------------
    def left_rotation(self, curr_node):
        if curr_node.right is not None:  # Check if the right child exists
            y = curr_node.right
            curr_node.right = y.left 

            if y.left is not None:  # Check if the left child of 'y' exists
                y.left.parent = curr_node

            y.parent = curr_node.parent

            if curr_node.parent is None:  # curr_node is root
                self.root = y
            elif curr_node == curr_node.parent.left:  # curr_node is left child
                curr_node.parent.left = y
            else:  # curr_node is right child
                curr_node.parent.right = y

            y.left = curr_node
            curr_node.parent = y
        else:
            print("Cannot perform left rotation as the right child of the current node does not exist.")


    # ---------------- ZAG ---------------------
    def right_rotation(self, curr_node):
        y = curr_node.left # Se guarda la referencia del nodo izquierdo de curr_node en y
        curr_node.left = y.right

        if y.right != None: # Si el hijo derecho de "y" existe
            y.right.parent = curr_node

        y.parent = curr_node.parent

        if curr_node.parent == None:  # curr_node es raíz
            self.root = y

        elif curr_node == curr_node.parent.right: # curr_node es hijo derecho
            curr_node.parent.right = y

        else: # curr_node es hijo izquierdo
            curr_node.parent.left = y

        y.right = curr_node # Se actualizan referencias
        curr_node.parent = y

    # ---------------- ZIG-ZIG ------------------
    def zig_zig(self, curr_node):
        self.left_rotation(curr_node.parent)
        self.left_rotation(curr_node)

    # ---------------- ZAG-ZAG ------------------
    def zag_zag(self, curr_node):
        self.right_rotation(curr_node.parent)
        self.right_rotation(curr_node)

    # ---------------- ZIG-ZAG ------------------
    def zig_zag(self, curr_node):
        self.right_rotation(curr_node)
        self.left_rotation(curr_node)

    # ---------------- ZAG-ZIG ------------------
    def zag_zig(self, curr_node):
        self.left_rotation(curr_node)
        self.right_rotation(curr_node)

    #-----------Para hacerle splay despues de cada operacion y que la raiz sea el nodo usado-----------
    def splay_tree(self, node):
        while node.parent is not None:
            if node.parent == self.root:
                if node == node.parent.left:
                    self.right_rotation(node.parent)
                else:
                    self.left_rotation(node.parent)
            else:
                parent = node.parent
                g = parent.parent
                if parent.left == node and g.left == parent:
                    self.zig_zig(node)
                elif parent.right == node and g.right == parent:
                    self.zag_zag(node)
                elif parent.right == node and g.left == parent:
                    self.zig_zag(node)
                else:
                    self.zag_zig(node)
        self.root = node

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            raiz = self.root
            parent = None
            while raiz is not None:
                parent = raiz
                if value < raiz.value:
                    raiz = raiz.left
                else:
                    raiz = raiz.right

            new_node.parent = parent
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

        self.splay_tree(new_node)

    '''def search(self, node):
        pass

    def delete(self, node):
        pass'''

tree = SplayTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)
