import unittest
import rubik.rotate as rotate


class RotateTest(unittest.TestCase):


    def test_check_010_ShouldReturnFstringRotation(self):
        parm = {'op':'check',
                'rotate': "",
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'F')
