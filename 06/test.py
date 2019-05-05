import unittest
from simple_remote_control import SimpleRemoteControl
from remote_control import RemoteControl
from light import Light
from stereo import Stereo
from light_on_command import LightOnCommand
from light_off_command import LightOffCommand
from stereo_on_with_cd_command import StereoOnWithCDCommand
from stereo_off_command import StereoOffCommand
from micro_command import MicroCommand


class TestCase(unittest.TestCase):

    def tearDown(self):
        print('##################################')


class TestRemoteControl(TestCase):

    def test_SimpleRemoteControl(self):
        remote = SimpleRemoteControl()
        light = Light()
        light_on_command = LightOnCommand(light)

        remote.set_command(light_on_command)
        remote.button_was_pressed()

    def test_RemoteControl(self):
        remote_control = RemoteControl()

        living_room_light = Light('Living Room')
        kitchen_light = Light('Kitchen')
        stereo = Stereo('Living Room')

        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)
        kitchen_light_on = LightOnCommand(kitchen_light)
        kitchen_light_off = LightOffCommand(kitchen_light)
        stereo_on_with_CD = StereoOnWithCDCommand(stereo)
        stereo_off = StereoOffCommand(stereo)

        remote_control.set_command(0, living_room_light_on, living_room_light_off)
        remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
        remote_control.set_command(2, stereo_on_with_CD, stereo_off)

        print(remote_control)

        remote_control.on_button_was_pushed(0)
        remote_control.off_button_was_pushed(0)
        remote_control.on_button_was_pushed(1)
        remote_control.off_button_was_pushed(1)
        remote_control.undo_button_was_pushed()
        remote_control.on_button_was_pushed(2)
        remote_control.off_button_was_pushed(2)
        remote_control.undo_button_was_pushed()

    def test_MicroCommand(self):
        remote_control = RemoteControl()

        living_room_light = Light('Living Room')
        kitchen_light = Light('Kitchen')
        stereo = Stereo('Living Room')

        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)
        kitchen_light_on = LightOnCommand(kitchen_light)
        kitchen_light_off = LightOffCommand(kitchen_light)
        stereo_on_with_CD = StereoOnWithCDCommand(stereo)
        stereo_off = StereoOffCommand(stereo)

        micro_on = MicroCommand([living_room_light_on, kitchen_light_on, stereo_on_with_CD])
        micro_off = MicroCommand([living_room_light_off, kitchen_light_off, stereo_off])

        remote_control.set_command(0, micro_on, micro_off)

        print(remote_control)

        remote_control.on_button_was_pushed(0)
        remote_control.off_button_was_pushed(0)
        remote_control.undo_button_was_pushed()


if __name__ == '__main__':
    unittest.main()
