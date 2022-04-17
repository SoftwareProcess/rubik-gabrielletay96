import unittest
import rubik.solve as solve


class SolveTest(unittest.TestCase):
    
    # Analysis: solve
#    inputs:
#        parms:    dictionary; mandatory; arrives validated
#        parms['op']    string , "solve"; mandatory; arrives validated
#        parms['cube']  string; len=54, [azAZ09], ...; mandatory, arrives unvalidated
#        parms['rotate] string; len>=0, [FfRrBbLlUuDd]; optional, default to F is missing; arrives unvalidated

#    outputs:
#        side-effects: no state change; no external effects
#        returns: dictionary
#        nominal:
#            dictionary['cube']:    string, len=54
#            dictionary['status']:  'ok'
#        abnormal:
#            dictionary['status']: 'error: xxx' where xxx is a dev-selected message
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: nominal cube with F rotation
#        test 020: nominal cube with f rotation
#        test 030: nominal cube with missing rotation
#        test 040: nominal cube with "" rotation
#
#    sad path:
#        test 910: missing cube
#        test 920: valid cube, invalid rotation
#        test 930: 

    def test_solve_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve.Solver(inputDict)
        
        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
    def test_solve_020_ShouldRotateValidNominalCubeWithEmptyStringRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve.Solver(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
    def test_solve_030_ShouldReturnInvalidRotationInputType(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 780
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = None
        expectedResult['status'] = "error: invalid input type"
        
        actualResult = solve.Solver(inputDict)
        
        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
        
    def test_solve_040_ShouldReturnInvalidRotationRotationCharacters(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 'QvW'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = None
        expectedResult['status'] = "error: invalid characters"
        
        actualResult = solve.Solver(inputDict)
        
        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
    def test_solve_050_ShouldRotateValidNominalCubeWithEmptyStringRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bbbrrroooggggbbbwwwwggooorrrbbbrrryyygggyyywwooowwwyyy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbbrrroooggggbbbwwwoggooorrrbbbrrryyygggyyyywowowwwywy'
        expectedResult['solution'] = 'FF'
        expectedResult['status'] = 'ok'
        
        actualResult = solve.Solver(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        