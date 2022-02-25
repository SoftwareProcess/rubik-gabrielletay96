import rubik.cube as rubik
from _pyinstaller_hooks_contrib.tests.scripts.pyi_lib_tensorflow_mnist import model
# dev strategy
#    valdiate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize vube model in string
#    return string + status of 'ok'


def _solve(parms):
    result = {}
    
    result['cube'] = "bbrgrgggyywwbbrrggooyywwbbrggooyywwbooyywwbbryooowrrrg"
    result['status'] = 'ok'                     
    return result
    
    '''
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    '''
def _checkRotations():
    pass

