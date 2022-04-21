from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
    # Valid
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    # Invalid because of integer
    def test_check_011_ShouldReturnInvalidOnisStr(self):
        parm = {'op':'check',
                'cube': 68}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Invalid type')
       
    # Invalid number of unique colors 
    def test_check_100_ShouldReturnInvalidOnsizeCheck(self):
        parm = {'op':'check',
                'cube': '111aaabbb222cccddd1ab2cd333444ddd1234abcde12345edcb'}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Invalid size')
        
    # Valid 
    def test_check_101_ShouldReturnOkOnUnsolvedCube(self):
        parm = {'op':'check',
                'cube': 'bbrrggggyywwbbrrggooyywwbbrggooyywwbooyywwbbryooowrrrg'}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    # Invalid size 
    def test_check_110_ShouldReturnInvalidOncheckSize(self):
        parm = {'op':'check',
                'cube': 'bbrywwbbrggooyywwbooowrrrg'}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Invalid size')
    
    # Invalid number of colors
    def test_check_111_ShouldReturnInvalidColorCount(self):
        parm = {'op':'check',
                'cube':'bbbbbbbrrrrrrrrrrrgggggooogoooooooooyyyyyyyyyyywwwwwww'}
        result = check._check(parm)
       
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Invalid number of colors')
        
    # Missing cube
    def test_check_112_ShouldReturnCubeMissing(self):
        parm = {'op':'check',
                'cube':''}
        result = check._check(parm)
        
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Cube is missing')