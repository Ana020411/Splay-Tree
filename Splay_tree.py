class Node:
    def __init__(self, key, parent) -> None:
        self.key = key
        self.parent = parent # Referencia al padre
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    # ---------------  ZIG -------------------
    def left_rotation(self, curr_node):
        y = curr_node.right # Se guarda la referencia del nodo derecho de curr_node en y
        curr_node.right = y.left 

        if y.left != None: # Si el hijo izquiero de "y" existe
            y.left.parent = curr_node

        y.parent = curr_node.parent

        if curr_node.parent == None: # curr_node es raíz
            self.root = y

        elif curr_node == curr_node.parent.left: # curr_node es hijo izquierdo
            curr_node.parent.left = y

        else: # curr_node es hijo derecho
            curr_node.parent.right = y

        y.left = curr_node # Se actualizan referencias
        curr_node.parent = y 

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

    def splay_tree(self, node):
        pass

    def insert(self, node):
        pass

    def search(self, node):
        pass

    def delete(self, node):
        pass