import cv2

class Image:
    def __init__(self, filename, tags, path):
        self.filename = filename
        self.tags = tags  
        self.path = path

    def show_image(self):
        img = cv2.imread(self.path)  
        if img is not None:
            cv2.imshow(self.filename, img)
            cv2.waitKey(0)  
            cv2.destroyAllWindows() 
        else:
            print(f"Error: Image {self.filename} not found.")
