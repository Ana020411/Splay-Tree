
#HOLAAAAAAAA CREO QUE NO ESTA TAN MAL EL CODIGO  PERO SI HAY AUN ERRORES, HAY QUE CHECAR:
#*EL CASO DE QUE HIJO DERECHO E HIJO IZQUIEDO SEAN NONE PARA LAS ROTACIONES
#COMO SE ESTA IMPRIMIENDO PORQUE LA PRIMERA VEZ LO HACE BIEN PERO YA QUE LE METES DESPUES UN NUEVO NODO CREO QUE YA NO TANTO
#BUENO ESO CONSIDERANDO QUE ES COMO EL BINARY TREE Y LOS NODOS MAS GRANDES VAN A LA DERECHA
"""GRACIASSSS PERDON, ES LO UNICO QUE PUDE ADELANTAR, YA NO ALACANZO A MAS, PERO OBVIO REGRESANDO TE AYUDO EN TODO LO QUE PUEDA MIL GRACIASSS TQ"""
# Y SI NO SIRVE ALGO, TU BORRA TODO SIN PROBLEMA :))) MUCHAS GRACIAS 
# Y SI QUIERAS DEJAME ALGO,NO PASA NADAAA O CUALQUIER COSA ME HABLAS Y EL PRIMER LUNES LO VEOO
#GRACIAAAAAAAAAAAAAAAS

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
            return None,("checar")
    # ---------------- ZAG ---------------------
    def right_rotation(self, curr_node):
        if curr_node.left is not None:  # Check if the left child exists
            y = curr_node.left
            curr_node.left = y.right

            if y.right is not None:  # Check if the right child of 'y' exists
                y.right.parent = curr_node

            y.parent = curr_node.parent

            if curr_node.parent is None:  # curr_node is root
                self.root = y
            elif curr_node == curr_node.parent.right:  # curr_node is right child
                curr_node.parent.right = y
            else:  # curr_node is left child
                curr_node.parent.left = y

            y.right = curr_node
            curr_node.parent = y
        else:
            return None,("checar")

    # ---------------- ZIG-ZIG ------------------
    def zig_zig(self, curr_node):
        self.right_rotation(curr_node)
        self.right_rotation(curr_node.parent)

    # ---------------- ZAG-ZAG ------------------
    def zag_zag(self, curr_node):
        self.left_rotation(curr_node)
        self.left_rotation(curr_node.parent)

    # ---------------- ZIG-ZAG ------------------
    def zig_zag(self, curr_node):
        self.right_rotation(curr_node)
        self.left_rotation(curr_node.parent)

    # ---------------- ZAG-ZIG ------------------
    def zag_zig(self, curr_node):
        self.left_rotation(curr_node)
        self.right_rotation(curr_node.parent)

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

tree = SplayTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)

# Print the root of the tree
print(tree.root.value)
print(tree.root.right.value)
print(tree.root.right.left.value)
print("----------------")
tree.insert(4)

print(tree.root.value)
