import tkinter as tk
from PIL import Image, ImageTk

class ImageViewer:
    def _init_(self, root, image_path):
        self.root = root
        self.root.title("Image Viewer")
        root.geometry("800x600")

        # Load the initial image
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        #label to display the image
        self.image_label = tk.Label(root, image=self.photo, width=600, height=400)
        self.image_label.grid(row=0, column=0, columnspan=3, sticky=tk.W + tk.E + tk.N + tk.S)

        # Buttons for zoom and rotate
        self.zoom_in_button = tk.Button(root, text="Zoom In", command=self.zoom_in)
        self.zoom_out_button = tk.Button(root, text="Zoom Out", command=self.zoom_out)
        self.rotate_button = tk.Button(root, text="Rotate 90°", command=self.rotate)

        self.zoom_in_button.grid(row=1, column=0)
        self.zoom_out_button.grid(row=1, column=1)
        self.rotate_button.grid(row=1, column=2)

    def zoom_in(self):
        # anti-aliasing using LANCZOS filter
        self.image = self.image.resize((int(self.image.width * 1.2), int(self.image.height * 1.2)), resample=Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.photo)

    def zoom_out(self):
        #with anti-aliasing using LANCZOS filter
        self.image = self.image.resize((int(self.image.width * 0.8), int(self.image.height * 0.8)), resample=Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.photo)

    def rotate(self):
        # Rotate the image by 90 degrees
        self.image = self.image.rotate(90, expand=True)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.photo)

if __name__ == "_main_":
    root = tk.Tk()
    image_path = "C:/Users/vigne/Desktop/imagecar.jpg"
    viewer = ImageViewer(root, image_path)
    root.mainloop()