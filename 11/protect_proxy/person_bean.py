from subject import Subject


class PersonBean(Subject):

    def __init__(self):
        super().__init__()

        self.name = ''
        self.gender = ''
        self.interests = ''
        self.rating = 0
        self.rating_count = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_interests(self):
        return self.interests

    def set_interests(self, interests):
        self.interests = interests

    def get_hot_or_not_rating(self):
        if self.rating_count == 0:
            return 0
        else:
            return self.rating / self.rating_count

    def set_hot_or_not_rating(self, rating):
        self.rating += rating
        self.rating_count += 1
