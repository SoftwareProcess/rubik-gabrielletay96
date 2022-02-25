import rubik.cube as rubik
import rubik.cube as cube

def _check(parms):
    rotate = parms.get('rotate')
    
    status = _isEmpty(rotate)
    if status == 'ok':
        status = _isValidCharacters(rotate)
    
    return status
    
def _isEmpty(rotate):
    if rotate == "":
        return 'F'
    else:
        return 'ok'

def _isValidCharacters(rotate):
    rotation_letters = ['f', 'b', 'r', 'l', 'u', 'd', 'F', 'B','R','L','U','D']
    cleaned_rotate = list(set(rotate))
    count = 0
    
    for letter in cleaned_rotate:
        if letter in rotation_letters:
            count += 1
    
    if count == len(cleaned_rotate):
        return 'ok'
    else:
        return "error: invalid characters"