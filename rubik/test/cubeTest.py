import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):
# Analysis: Cube    class
#            methods: instantiate
#                     load
#                     get
#
# Analysis: Cube.__init__
#    inputs:    no input parameter
#    outputs:
#        side effects: none
#        nominal: empty instance of cube
#        abnormal: NA

    def test_init_0101_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)
        
    def test_init_0102_ShouldReturnInvalidInputCube(self):
        parm = {'op':'check',
                'rotation': 'F',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        
        myCube = cube.Cube()
        status = myCube._load(parm)
        self.assertEqual(status, 'error: invalid input')
        
    def test_init_0103_ShouldReturnInvalidSizeCube(self):
        parm = {'op':'check',
                'rotation': 'F',
                'cube':'bbbgbbbbrrrrrrrrrgggggggoooooyooyyyyyyyyywwwwwwwww'}
        
        myCube = cube.Cube()
        status = myCube._load(parm)
        self.assertEqual(status, 'ok')
        
    def test_init_0104_ShouldReturnInvalidInputCube(self):
        myCube = cube.Cube()
        results = myCube._get(7)
        status = results['status']
        self.assertEqual(status, 'error: invalid input')