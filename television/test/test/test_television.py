import unittest
from television.television import television as tv


class MyTelevision(unittest.TestCase):

    def setUp(self):
        self.television = tv.Television()

    def test_if_my_television_is_off(self):
        self.assertFalse(self.television.is_on)

    def test_if_my_television_can_on(self):
        self.television.turn_on()
        self.assertTrue(self.television.is_on)

    def test_that_i_can_turn_on_and_off_my_television(self):
        self.assertFalse(self.television.is_on)
        self.television.turn_on()
        self.assertTrue(self.television.is_on)
        self.television.turn_off()
        self.assertFalse(self.television.is_on)

    def test_that_my_television_can_increase_volume(self):
        with self.assertRaises(Exception): self.television.increase_volume()
        self.assertEqual(50,self.television.volume)

    def test_that_television_raises_an_error_to_increase_volume_when_off(self):
        self.assertFalse(self.television.is_on)
        with self.assertRaises(Exception): self.television.increase_volume()

    def test_that_my_television_cannot_increase_volume_above_100_when_on(self):
        self.assertFalse(self.television.is_on)
        self.television.turn_on()
        for count in range(5):
            self.television.increase_volume()
        self.assertEqual(100,self.television.volume)
        with self.assertRaises(Exception): self.television.increase_volume()

    def test_that_television_volume_can_be_decreased(self):
        self.television.turn_on()
        self.television.increase_volume()
        self.television.increase_volume()
        self.assertEqual(70,self.television.volume)
        self.television.decrease_volume()
        self.assertEqual(60,self.television.volume)

    def test_that_my_television_cannot_decrease_volume_when_off(self):
        self.assertFalse(self.television.is_on)
        with self.assertRaises(Exception): self.television.decrease_volume()

    def test_that_television_raises_an_error_to_decrease_volume_below_0(self):
        self.television.turn_on()
        self.assertEqual(50,self.television.volume)
        for count in range(5):
            self.television.decrease_volume()
        self.assertEqual(0,self.television.volume)
        with self.assertRaises(Exception): self.television.decrease_volume()

    def test_that_my_volume_can_be_muted(self):
        self.television.turn_on()
        self.assertEqual(50,self.television.volume)
        self.television.mute()
        self.assertEqual(0,self.television.volume)
    def test_that_television_raises_an_error_to_mute_volume_when_off(self):
        self.assertFalse(self.television.is_on)
        with self.assertRaises(Exception): self.television.mute()

    def test_that_television_can_be_un_muted(self):
        with self.assertRaises(Exception): self.television.unmute()
        self.television.turn_on()
        self.assertEqual(50,self.television.volume)
        self.television.mute()
        self.assertEqual(0,self.television.volume)
        self.television.unmute()
        self.assertEqual(50,self.television.volume)

    def test_that_television_return_back_to_the_actual_value_when_un_muted(self):
        self.television.turn_on()
        self.assertEqual(50,self.television.volume)
        self.television.increase_volume()
        self.assertEqual(60,self.television.volume)
        self.television.mute()
        self.assertEqual(0,self.television.volume)
        self.television.unmute()
        self.assertEqual(60,self.television.volume)

    def test_that_television_can_change_my_channel_(self):
        self.television.turn_on()
        self.television.channel_up()
        self.assertEqual(2, self.television.channel)

    def test_that_television_cannot_channel_up_when_off(self):
        with self.assertRaises(Exception): self.television.channel_up()

    def test_that_television_cannot_channel_up_when_its_at_channel_10(self):
        self.television.turn_on()
        for count in range (9):
            self.television.channel_up()
        self.assertEqual(10, self.television.channel)
        with self.assertRaises(Exception): self.television.channel_up()

    def test_that_television_can_chanel_down(self):
        self.television.turn_on()
        self.television.channel_up()
        self.assertEqual(2, self.television.channel)
        self.television.channel_down()
        self.assertEqual(1, self.television.channel)

    def test_that_television_cannot_channel_down_when_off(self):
        with self.assertRaises(Exception): self.television.channel_down()
        self.assertEqual(1, self.television.channel)
    def test_that_television_can_set_chanel(self):
        self.television.turn_on()
        self.television.channel=10
        self.assertEqual(10, self.television.channel)


