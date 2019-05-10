from subject import Subject


class Proxy(Subject):

    def __init__(self, handler):
        super().__init__()

        self.handler = handler

    def get_name(self):
        return self.handler.invoke(self, 'get_name')

    def set_name(self, name):
        self.handler.invoke(self, 'set_name', name=name)

    def get_gender(self):
        return self.handler.invoke(self, 'get_gender')

    def set_gender(self, gender):
        self.handler.invoke(self, 'set_gender', gender=gender)

    def get_interests(self):
        return self.handler.invoke(self, 'get_interests')

    def set_interests(self, interests):
        self.handler.invoke(self, 'set_interests', interests=interests)

    def get_hot_or_not_rating(self):
        return self.handler.invoke(self, 'get_hot_or_not_rating')

    def set_hot_or_not_rating(self, rating):
        self.handler.invoke(self, 'set_hot_or_not_rating', rating=rating)
