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

    def test_solve_010_ShouldRotateValidNominalCubeWithEmptyStringRotation(self):
        inputDict = {}
        inputDict['cube'] = 'JJJJJJJJJfffffffffLLLLLLLLLbbbbbbbbbAAAAAAAAAGGGGGGGGG'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'JJJJJJJJJfffffffffLLLLLLLLLbbbbbbbbbAAAAAAAAAGGGGGGGGG'
        expectedResult['status'] = 'ok'
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)
        
        
        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])


    def test_solve_020_ShouldSolveCrossFromDaisy(self):
        inputDict = {}
        inputDict['cube'] = 'n55n55n55WMMWMMWMM5nn5nn5nnWWMWWMWWMH000H0H000HHH0H0HH'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = '55n55nH5nWMMWMMWMMnn5nn50n5WWMWWMWWM0HHHHH0HH500000H0n'
        expectedResult['status'] = 'ok'
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)

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
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)
        
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
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)

        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
    
    def test_solve_050_ShouldRotateValidNominalCubeWithEmptyStringRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bbbrrroooggggbbbwwwwggooorrrbbbrrryyygggyyywwooowwwyyy'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'orborbbrbyggwbbwwwwwggooorrrbobroryoygggyyyrboggwwwyyy'
        expectedResult['status'] = 'ok'
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
    
        
    def test_solve_060_ShouldReturnBottomCross(self):
        inputDict = {}
        inputDict['cube'] = 'aaIaIIaII7CCC77C77aIIaaIaaIC777CC7CCffffzfzfzzzzzfzfzf'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'aIIaIIfaIC7777C7CCaaIaaIzII7CCCC7C77zzzzzzfzfafffffzfa'
        expectedResult['status'] = "ok"
        
        solver = solve.Solver()
        actualResult = solver._solve(inputDict)
        
        self.assertEqual(expectedResult['status'],actualResult['status'])
        self.assertEqual(expectedResult['cube'], actualResult['cube'])