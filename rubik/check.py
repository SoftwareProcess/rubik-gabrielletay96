import rubik.cube as rubik

# checks important aspects of rubiks cube
def _check(parms):
    result={}
    encodedCube = parms.get('cube', None)
           
    if(encodedCube == None):
        result['status'] = 'error: cube is missing'          
    else:
        status = _isStr(encodedCube)
        if status == True:
            result['status'] = 'ok'
        else:
            result['status'] = status
        
    return result

# checks if input is a string
def _isStr(encodedCube):
    if type(encodedCube) == str:
        status = _size_check(encodedCube)
        return status
    else:
        return "'error: Invalid type"
 
# checks size of cube   
def _size_check(encodedCube):
    if len(encodedCube) == 54:
        status = _size_check(encodedCube)
        return status
    else:
        return "'error: Invalid size"

# checks for unique colors
def _colors_check(encodedCube):
    unique_colors = len(list(set(encodedCube)))
    if unique_colors == 6:
        status = _color_count_check(encodedCube, unique_colors)
        return status
    else:
        return "'error: Invalid number of unique colors"

# checks for number of unique colors
def _color_count_check(encodedCube, unique_colors):
    for color in unique_colors:
        count = encodedCube.count(color)
    
    if count == 9:
        return True
    else:
        return "'error: Invalid number of colors"
    
    