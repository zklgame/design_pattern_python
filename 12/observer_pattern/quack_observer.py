from observer_pattern.observer import Observer


class QuackObserver(Observer):

    def update(self, duck):
        print('Quackologist: ', duck)
