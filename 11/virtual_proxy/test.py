import unittest
from image_proxy import ImageProxy


class TestCase(unittest.TestCase):

    def test_virtual_proxy(self):
        icon = ImageProxy('url', 'CD Cover')
        print('h: %d, w: %d' % (icon.get_icon_height(), icon.get_icon_width()))
        icon.paint_icon(100, 200)
        print('h: %d, w: %d' % (icon.get_icon_height(), icon.get_icon_width()))


if __name__ == '__main__':
    unittest.main()
