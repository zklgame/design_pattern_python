class Waitress(object):

    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        self.menus.print()

    def print_vegetarian_menu(self):
        iterator = self.menus.create_iterator()
        print('---- Vegetarian Menu ----')
        while iterator.has_next():
            menu_component = iterator.next()
            #print(menu_component.get_name() + ', ' + menu_component.get_description())
            try:
                if menu_component.is_vegetarian():
                    menu_component.print()
            except:
                pass
