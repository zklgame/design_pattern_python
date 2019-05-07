class Waitress(object):

    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        for i, menu in enumerate(self.menus):
            print('MENU %d:' % (i + 1))
            self.print_menu_with_iterator(menu.create_iterator())

    def print_menu_with_iterator(self, iterator):
        while iterator.has_next():
            menu_item = iterator.next()
            print(menu_item.get_name() + ', ', end='')
            print(str(menu_item.get_price()) + ' -- ', end='')
            print(menu_item.get_description())
