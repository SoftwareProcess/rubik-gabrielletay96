import rubik.cube as rubik

# dev strategy
#    validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'


def _solve(parms):
    _validateParms(parms)
    
    '''
    result = {}
    result['cube'] = "bwbybgrygyogyrrobwogrbgooggbworwogwwybygrroyowbwyrrb"
    result['status'] = 'ok'                     
    return result
    '''
    

def _validateParms(parms):
    rotate = parms.get('rotate')
    cube = parms.get('cube')
    
    

