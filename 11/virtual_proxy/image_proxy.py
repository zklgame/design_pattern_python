from icon import Icon
from image_icon import ImageIcon


class ImageProxy(Icon):

    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.image_icon = None
        self.retrieving = False

    def get_icon_width(self):
        width = 800
        if self.image_icon:
            width = self.image_icon.get_icon_width()
        return width

    def get_icon_height(self):
        height = 600
        if self.image_icon:
            height = self.image_icon.get_icon_height()
        return height

    def paint_icon(self, x, y):
        if self.image_icon:
            self.image_icon.print_icon(x, y)
        else:
            print('Loading CD cover, please wait ...(x: %d, y: %d)'
                  % (x + 100, y + 100))
            if not self.retrieving:
                self.image_icon = ImageIcon(self.url, self.name)
                self.retrieving = True
                self.image_icon.paint_icon(x, y)
