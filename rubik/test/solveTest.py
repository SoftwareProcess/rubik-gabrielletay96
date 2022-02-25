import unittest
import rubik.solve as solve


class SolveTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testName(self):
        pass
    
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
    @unittest.skip('skipping this test until cube model is complete')
    def test_solve_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['cube'] = 'bbrrggggyywwbbrrggooyywwbbrggooyywwbooyywwbbryooowrrrg'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbrgrgggyywwbbrrggooyywwbbrggooyywwbooyywwbbryooowrrrg'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'),actualResult.get('status'))