import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
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