import unittest
import rubik.rotate as rotate
# sikldfs

class RotateTest(unittest.TestCase):

    #Pass
    def test_check_010_ShouldReturnFstringRotation(self):
        parm = {'op':'check',
                'rotate': "",
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'F')
    
    #Fail
    def test_check_020_ShouldReturnEmptyInput(self):
        parm = {'op':'check',
                'rotate': None,
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'ok')
         
    #Fail
    def test_check_030_ShouldReturnInvalidRotation(self):
        parm = {'op':'check',
                'rotate': "FbUuG",
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'ok')
    
    #Fail
    def test_check_040_ShouldReturnInvalidInput(self):
        parm = {'op':'check',
                'rotate': 34,
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        status = rotate._check(parm)
        self.assertEqual(status, 'ok')
    

