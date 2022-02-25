import unittest
import rubik.rotate as rotate


class RotateTest(unittest.TestCase):


    def test_check_010_ShouldReturnFstringRotation(self):
        parm = {'op':'check',
                'rotate': "",
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'F')
        
    def test_check_020_ShouldReturnInvalidRotation(self):
        parm = {'op':'check',
                'rotate': "FbUuG",
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'ok')

