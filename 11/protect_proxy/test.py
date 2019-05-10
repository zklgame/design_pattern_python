import unittest
from person_bean import PersonBean
from proxy import Proxy
from owner_invocation_handler import OwnerInvocationHandler
from non_owner_invocation_handler import NonOwnerInvocationHandler


class TestCase(unittest.TestCase):

    def test_protect_proxy(self):
        p1 = PersonBean()
        p1.set_name('p1')
        p1.set_gender('female')
        p1.set_interests('p1 interests')

        p2 = PersonBean()
        p2.set_name('p2')
        p2.set_gender('male')
        p2.set_interests('p2 interests')

        p1_own_handler = OwnerInvocationHandler(p1)
        p1_not_own_handler = NonOwnerInvocationHandler(p2)
        p1_own_proxy = Proxy(p1_own_handler)
        p1_not_own_proxy = Proxy(p1_not_own_handler)

        print('p1 name', p1_own_proxy.get_name())
        print('p2 name', p1_not_own_proxy.get_name())

        print('set p1 name')
        p1_own_proxy.set_name('p11')
        print('set p2 name')
        try:
            p1_not_own_proxy.set_name('p22')
        except Exception as err:
            print(err)

        print('p1 name', p1_own_proxy.get_name())
        print('p2 name', p1_not_own_proxy.get_name())

        print('')

        print('set p1 rating')
        try:
            p1_own_proxy.set_hot_or_not_rating(1)
        except Exception as err:
            print(err)

        print('set p2 rating')
        p1_not_own_proxy.set_hot_or_not_rating(2)

        print('p1 rating', p1_own_proxy.get_hot_or_not_rating())
        print('p2 rating', p1_not_own_proxy.get_hot_or_not_rating())


if __name__ == '__main__':
    unittest.main()
