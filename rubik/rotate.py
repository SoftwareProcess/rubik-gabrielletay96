import rubik.cube as rubik
import rubik.cube as cube

def _check(parms):
    rotate = parms.get('rotate')
    
    status = _isEmpty(rotate)
    return status
    
    
def _isEmpty(rotate):
    if rotate == "":
        return 'F'
    else:
        return 'ok'
