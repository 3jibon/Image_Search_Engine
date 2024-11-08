class SearchEngine:
    def __init__(self):
        self.head = None 
    class Node:
        def __init__(self, image):
            self.image = image  
            self.next = None 

    def add_image(self, image):
        new_node = self.Node(image)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def search_by_keyword(self, keyword):
        temp = self.head
        while temp:
            if keyword in temp.image.tags: 
                 temp.image.show_image()
            temp = temp.next
