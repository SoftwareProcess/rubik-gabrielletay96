import unittest
import rubik.cube as cube
from _pyinstaller_hooks_contrib.tests.scripts.pyi_lib_boto import skip

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
    @unittest.skip
    def test_init_0101_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)
        
    def test_init_0102_ShouldReturnValidCube(self):
        parm = {'op':'check',
                'rotation': 'F',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        
        myCube = cube.Cube(parm)
        self.assertEqual(myCube, 'ok')