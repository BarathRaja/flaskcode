class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.right = None
        self.left = None

class bst:
    def __init__(self):
        self.root = None
    
    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return
        

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    
    def _search_recursive(self, blog_post_id, node):
        if node.data["id"] == blog_post_id:
            return node.data
        if node.data["id"] < blog_post_id:
            return self._search_recursive(blog_post_id,node.right)
        if node.data["id"] > blog_post_id:
            return self._search_recursive(blog_post_id,node.left)
        return False
        
    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id, self.root)
        

