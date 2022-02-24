import rubik.cube as rubik

# checks important aspects of rubiks cube
def _check(parms):
    result={}
    encodedCube = parms.get('cube', None)
    
    status = _isMissing(encodedCube)
    
    if status == 'ok':
        status = _isStr(encodedCube)
    if status == 'ok':
        status = _size_check(encodedCube)     
    if status == 'ok':
        status = _colors_check(encodedCube)
        
    result['status'] = status
    
    return result

def _isMissing(encodedCube):   
    if(encodedCube == None):
        return "error: cube is missing"
    else:
        return 'ok'
        
# checks if input is a string
def _isStr(encodedCube):
    if type(encodedCube) == str:
        return 'ok'
    else:
        return "error: Invalid type"
 
# checks size of cube   
def _size_check(encodedCube):
    if len(encodedCube) == 54:
        return 'ok'
    else:
        return "error: Invalid size"

# checks for unique colors
def _colors_check(encodedCube):
    unique_colors = list(set(encodedCube))
    if len(unique_colors) == 6:
        status = _color_count_check(encodedCube, unique_colors)
        return status
    else:
        return "error: Invalid number of unique colors"

# checks for number of unique colors
def _color_count_check(encodedCube, unique_colors):
    for color in unique_colors:
        count = encodedCube.count(color)
    
    if count == 9:
        return 'ok'
    else:
        return "error: Invalid number of colors"
    
    