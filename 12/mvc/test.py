import unittest
from beat_controller import BeatController
from beat_model import BeatModel


class TestCase(unittest.TestCase):

    def test_MVC(self):
        model = BeatModel()
        controller = BeatController(model)
        controller.start()
        controller.increase_bpm()
        controller.decrease_bpm()
        controller.set_bpm(88)
        controller.stop()


if __name__ == '__main__':
    unittest.main()
