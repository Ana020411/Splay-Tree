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
        y = curr_node.right
        curr_node.right = y.left 

        if y.left is not None:  # Se checa si el hijo izquierdo de "y" existe
            y.left.parent = curr_node

        y.parent = curr_node.parent

        if curr_node.parent is None:  # curr_node es raíz
            self.root = y
        elif curr_node == curr_node.parent.left:  # curr_node es hijo izquierdo
            curr_node.parent.left = y
        else:  # curr_node es hijo derecho
            curr_node.parent.right = y

        y.left = curr_node
        curr_node.parent = y

        
    # ---------------- ZAG ---------------------
    def right_rotation(self, curr_node):
        y = curr_node.left
        curr_node.left = y.right

        if y.right is not None:  # Se checa si el hijo derecho de "y" existe
            y.right.parent = curr_node

        y.parent = curr_node.parent

        if curr_node.parent is None:  # curr_node es raíz
            self.root = y
        elif curr_node == curr_node.parent.right:  # curr_node es hijo derecho
            curr_node.parent.right = y
        else:  # curr_node es hijo izquierdo
            curr_node.parent.left = y

        y.right = curr_node
        curr_node.parent = y
   

    #------------------------------ SPLAYING ------------------------------------

    def splay_tree(self, node):
        while node.parent is not None:
            if node.parent == self.root:
                if node == node.parent.left:
                    self.right_rotation(node.parent)
                else:
                    self.left_rotation(node.parent)
            else:
                parent_node = node.parent
                grand_parent = parent_node.parent

                if node == parent_node.left and parent_node == grand_parent.left:
                    # ---------------- ZIG - ZIG --------------------
                    self.right_rotation(grand_parent)
                    self.right_rotation(parent_node)
                elif node == parent_node.right and parent_node == grand_parent.right:
                    # ----------------- ZAG - ZAG ---------------------
                    self.left_rotation(grand_parent)
                    self.left_rotation(parent_node)
                elif node == parent_node.right  and parent_node == grand_parent.left:
                    # ----------------- ZAG - ZIG ---------------------
                    self.left_rotation(parent_node)
                    self.right_rotation(grand_parent)
                else:
                    # ----------------- ZIG - ZAG ----------------------
                    self.right_rotation(parent_node)
                    self.left_rotation(grand_parent)

        self.root = node
    

    # --------------------------------------------- INSERCIÓN -------------------------------------------
    def insert(self, node):
        new_node = Node(node, parent=None)
        
        raiz = self.root
        y = None

        while raiz is not None:
            y = raiz
            if new_node.value < raiz.value:
                raiz = raiz.left
            else:
                raiz = raiz.right

        new_node.parent = y

        if y is None:
            self.root = new_node
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node

        self.splay_tree(new_node)


    # ------------------------------------------------ BÚSQUEDA ------------------------------------------
    def search(self, value):
        if self.root is None: # El árbol está vacío
            return "El árbol está vacío"
        
        curr_node = self.root
        while curr_node is not None:
            if value == curr_node.value:
                self.splay_tree(curr_node)
                return f"Valor {curr_node.value} encontrado"
            elif value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
        
        return "No se encontró"
    

    # ------------------------------------------ ELIMINACIÓN ------------------------------------------
    def delete(self, value):
        # Top - down 
        node = self.search_node(value)

        if node is None:
            return None
        
        self.splay_tree(node) # Para que quede como raíz

        left_subtree = SplayTree()
        left_subtree.root = self.root.left

        if left_subtree.root is not None:
            left_subtree.root.parent = None # Se elimina la raíz, que en este caso es node

        right_subtree = SplayTree()
        right_subtree.root = self.root.right

        if right_subtree.root is not None:
            right_subtree.root.parent = None # Se quitan las referencias al node para que se elimine

        if left_subtree.root is not None:
            max_node = left_subtree.max(left_subtree.root) # Se saca el nodo con mayor valor del subárbol izquierdo
            left_subtree.splay_tree(max_node)
            
            # Referencias
            left_subtree.root.right = right_subtree.root # Se une el subarbol derecho y el izquierdo
            if right_subtree.root is not None: # Si existe un subarbol derecho
                right_subtree.root.parent = left_subtree.root # Se une la raíz del derecho con el izquierdo
                
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

        if self.root is not None:
            self.root.parent = None

    # ------------------------------------- FUNCIONES DEL DELETE -----------------------------
    def search_node(self, value):
        if self.root is None: # El árbol está vacío
            return None
        
        curr_node = self.root
        while curr_node is not None:
            if value == curr_node.value:
                self.splay_tree(curr_node)
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
        
        return None

    def max(self, node):
        if node is None:
            return False
        
        while node.right is not None:
            node = node.right

        return node

    # ------------------------------------- IMPRESIÓN DEL ÁRBOL ---------------------------------
    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, current_node):
        if current_node.left is not None:
            self.__inorder(current_node.left)

        print(current_node.value)

        if current_node.right is not None:
            self.__inorder(current_node.right)


# --------------------------------- CASO PRUEBA--------------------------------------
tree = SplayTree()
tree.insert(10)
tree.insert(8)
tree.insert(20)
tree.insert(5)
tree.insert(4)


print("Raíz:")
print(tree.root.value)
print("Recorrido inorder del árbol:")
print(tree.inorder())
print("¿Se encontró?")
print(tree.search(8))
print("--------------------------------------------------------")
tree.delete(5)
tree.delete(8)
print("Raíz:")
print(tree.root.value)
print("Recorrido inorder del árbol sin el eliminado:")
print(tree.inorder())


