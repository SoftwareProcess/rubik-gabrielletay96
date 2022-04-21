from rubik.math import Matrix

'''ROTATION CODES'''
ROT_XY_CW = Matrix(0, 1, 0,
                   -1, 0, 0,
                   0, 0, 1)
ROT_XY_CC = Matrix(0, -1, 0,
                   1, 0, 0,
                   0, 0, 1)

ROT_XZ_CW = Matrix(0, 0, -1,
                   0, 1, 0,
                   1, 0, 0)
ROT_XZ_CC = Matrix(0, 0, 1,
                   0, 1, 0,
                   -1, 0, 0)

ROT_YZ_CW = Matrix(1, 0, 0,
                   0, 0, 1,
                   0, -1, 0)
ROT_YZ_CC = Matrix(1, 0, 0,
                   0, 0, -1,
                   0, 1, 0)


''' ROTATION VALIDATION '''
def _check(parms):
    rotate = parms.get('rotate')
    status =_isString(rotate)
    
    if status == 'ok':
        status = _isValidCharacters(rotate)
        
    return status
    
def _isEmpty(rotate):
    if rotate == '':
        return 'empty'
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
        self.cube = cube
        self.command_seq = ''
        
    def _rotate_face(self, face, matrix):
        self._rotate_squares((self.cube._get_face(face))['face'], matrix)

    def _rotate_slice(self, plane, matrix):
        self._rotate_squares(self._slice(plane), matrix)

    def _rotate_squares(self, squares, matrix):
        for square in squares:
            square.rotate(matrix)
            
    # Rotation commands
    def L_cwise(self):
        self._rotate_face('LEFT', ROT_YZ_CC)
        self.command_seq += 'L'
    def l_ccwise(self):
        self._rotate_face('LEFT', ROT_YZ_CW)
        self.command_seq += 'l'
    def R_cwise(self):
        self._rotate_face('RIGHT', ROT_YZ_CW)
        self.command_seq += 'R'
    def r_ccwise(self):
        self._rotate_face('RIGHT', ROT_YZ_CC)
        self.command_seq += 'r'
    def U_cwise(self):
        self._rotate_face('UP', ROT_XZ_CW)
        self.command_seq += 'U'
    def u_ccwise(self):
        self._rotate_face('UP', ROT_XZ_CC)
        self.command_seq += 'u'
    def D_cwise(self):
        self._rotate_face('DOWN', ROT_XZ_CC)
        self.command_seq += 'D'
    def d_ccwise(self):
        self._rotate_face('DOWN', ROT_XZ_CW)
        self.command_seq += 'd'
    def F_cwise(self):
        self._rotate_face('FRONT', ROT_XY_CW)
        self.command_seq += 'F'
    def f_ccwise(self):
        self._rotate_face('FRONT', ROT_XY_CC)
        self.command_seq += 'f'
    def B_cwise(self):
        self._rotate_face('BACK', ROT_XY_CC)
        self.command_seq += 'B'
    def b_ccwise(self):
        self._rotate_face('BACK', ROT_XY_CW)
        self.command_seq += 'b'