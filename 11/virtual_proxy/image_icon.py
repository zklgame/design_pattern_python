from icon import Icon


class ImageIcon(Icon):

    def __init__(self, url, name):
        self.url = url
        self.name = name

    def get_icon_width(self):
        return 1

    def get_icon_height(self):
        return 2

    def paint_icon(self, x, y):
        print("I am Real Image Icon! (x: %d, y: %d)"
              % (x, y))
