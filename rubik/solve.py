import rubik.cube as rubik

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

