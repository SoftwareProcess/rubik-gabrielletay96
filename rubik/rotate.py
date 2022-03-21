import rubik.cube as rubik
import rubik.cube as cube
import operator

def _check(parms):
    rotate = parms.get('rotate')
    
    status = _isEmpty(rotate)
    if status == 'ok':
        status = _isString(rotate)
    else:
        return status
    
    if status == 'ok':
        status = _isValidCharacters(rotate)
        
    return status
    
def _isEmpty(rotate):
    if rotate == '':
        return 'error: empty string'
    else:
        return 'ok'
    
def _isString(rotate):
    if isinstance(rotate, str):
        return 'ok'
    else:
        return "error: invalid input type"
    
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


class RotateCube():

    def __init__(self, cube):
        front_clockwise = {1: [7,4,1,8,5,2,9,6,3], 2: [43,11,12,44,14,15,45,17,18], 3: [19,20,21,22,23,24,25,26,27], 4: [28,29,46,31,32,47,34,35,48], 5: [37,38,39,40,41,42,36,33,30], 6: [16,13,10,49,50,51,52,53,54]}
        front_counter_clockwise = {1: [3,6,9,2,5,8,1,4,7], 2: [48,11,12,47,14,15,46,17,18], 3: [19,20,21,22,23,24,25,26,27], 4: [28,29,45,31,32,44,34,35,43], 5: [37,38,39,40,41,42,10,13,16], 6: [30,33,36,49,50,51,52,53,54]}
        right_clockwise = {1: [1,2,48,4,5,51,7,8,54], 2: [16,13,10,17,14,11,18,15,12], 3: [45,20,21,42,23,24,39,26,27], 4: [28,29,30,31,32,33,34,35,36], 5: [37,38,3,40,41,6,43,44,9], 6: [46,47,27,49,50,24,52,53,21]}
        right_counter_clockwise = {1: [1,2,39,4,5,42,7,8,45], 2: [12,15,18,11,14,17,10,13,16], 3: [19,20,54,22,23,51,25,26,48], 4: [28,29,30,31,32,33,34,35,36], 5: [37,38,27,40,41,24,43,44,21], 6: [30,33,3,49,50,6,52,53,9]}
        back_clockwise = {1: [1,2,3,4,5,6,7,8,9], 2: [37,11,12,38,14,15,39,17,18], 3: [21,24,27,20,23,26,19,22,25], 4: [52,29,30,53,32,33,54,35,36], 5: [34,31,28,40,41,42,43,44,45], 6: [16,13,10,49,50,51,52,53,54]}
        back_counter_clockwise = {1: [1,2,3,4,5,6,7,8,9], 2: [10,11,54,13,14,53,16,17,52], 3: [25,22,19,26,23,20,27,24,21], 4: [37,29,46,38,32,47,39,35,48], 5: [12,15,18,40,41,42,36,33,30], 6: [34,31,28,49,50,51,52,53,54]}
        left_clockwise = {1: [37,2,3,40,5,6,43,8,9], 2: [10,11,12,13,14,15,16,17,18], 3: [52,20,21,49,23,24,46,26,27], 4: [34,31,28,35,32,29,36,33,30], 5: [25,38,39,22,41,42,19,44,45], 6: [1,13,10,4,50,51,7,53,54]}
        left_counter_clockwise = {1: [46,2,3,49,5,6,52,8,9], 2: [10,11,12,13,14,15,16,17,18], 3: [43,20,21,40,23,24,37,26,27], 4: [30,33,36,29,32,35,28,31,34], 5: [7,38,39,4,41,42,1,44,45], 6: [19,33,36,22,50,51,25,53,54]}
        up_clockwise = {1: [10,11,12,4,5,6,7,8,9], 2: [19,20,21,13,14,15,16,17,18], 3: [28,29,30,22,23,24,25,26,27], 4: [1,2,3,31,32,47,34,35,48], 5: [34,40,37,44,41,38,45,42,39], 6: [46,47,48,49,50,51,52,53,54]}
        up_counter_clockwise ={1: [28,29,30,4,5,6,7,8,9], 2: [1,2,3,13,14,15,16,17,18], 3: [10,11,12,22,23,24,25,26,27], 4: [19,20,21,31,32,47,34,35,48], 5: [39,42,45,38,41,44,37,40,34], 6: [46,47,48,49,50,51,52,53,54]}
        down_clockwise = {1: [1,2,3,4,5,6,16,17,18], 2: [10,11,12,13,14,15,25,26,27], 3: [19,20,21,22,23,24,34,35,36], 4: [28,29,30,31,32,33,7,8,9], 5: [37,38,39,40,41,42,43,44,45], 6: [52,49,46,53,50,47,54,51,48]}
        down_counter_clockwise = {1: [1,2,3,4,5,6,34,35,36], 2: [10,11,12,13,14,15,7,8,9], 3: [19,20,21,22,23,24,16,17,18], 4: [28,29,30,31,32,33,25,26,27], 5: [37,38,39,40,41,42,43,44,45], 6: [48,51,54,47,50,53,46,49,52]}
        self.rotation_codes = {'F': front_clockwise, 'f': front_counter_clockwise, 'R': right_clockwise, 'r': right_counter_clockwise,
                                'B': back_clockwise, 'b': back_counter_clockwise, 'L': left_clockwise, 'l': left_counter_clockwise,
                                'U': up_clockwise, 'u': up_counter_clockwise, 'D': down_clockwise, 'd': down_counter_clockwise}
        
        self.cube = cube
        

    def _gather_rotation_codes(self, cmd):
        rotator_dict = {}
        cube_rotation_code = self.rotation_codes[cmd]

        for i in range(1,7):
            cube_values = self.cube[i]
            cube_location_keys = cube_rotation_code[i]
        
            rotator_dict.update(zip(cube_location_keys, cube_values))
        #print(rotator_dict)

        return rotator_dict

    def _rotate_cube(self, rotator_dict):
        sorted_rotator_tup = sorted(rotator_dict.items())
        sorted_rotator_dict = dict((x, y) for x, y in sorted_rotator_tup)
        new_cube = ''.join(list(sorted_rotator_dict.values()))

        return new_cube