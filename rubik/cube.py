import rubik.check as check

from rubik.math import Point

RIGHT = X_AXIS = Point(1, 0, 0)
LEFT           = Point(-1, 0, 0)
UP    = Y_AXIS = Point(0, 1, 0)
DOWN           = Point(0, -1, 0)
FRONT = Z_AXIS = Point(0, 0, 1)
BACK           = Point(0, 0, -1)

FACE = 'face'
EDGE = 'edge'
CORNER = 'corner'

class Square:

    def __init__(self, pos, colors):
        self.pos = pos
        self.colors = list(colors)
        self._set_square_type()


    def _set_square_type(self):
        if self.colors.count(None) == 2:
            self.type = FACE
        elif self.colors.count(None) == 1:
            self.type = EDGE
        elif self.colors.count(None) == 0:
            self.type = CORNER

    def rotate(self, matrix):
        original_pos = self.pos
        self.pos = matrix * self.pos

        rotation = self.pos - original_pos
        if not any(rotation):
            return  # no change
        if rotation.count(0) == 2:
            rotation += matrix * rotation

        i, j = (i for i, x in enumerate(rotation) if x != 0)
        self.colors[i], self.colors[j] = self.colors[j], self.colors[i]
        
class Cube:
    '''
    Rubik's cube looks like:
            UUU                       36 37 38
            UUU                       39 40 41
            UUU                       42 43 44
        LLL FFF RRR BBB     27 28 29  0  1  2   9 10 11  18 19 20
        LLL FFF RRR BBB     30 31 32  3  4  5  12 13 14  21 22 23
        LLL FFF RRR BBB     33 34 35  6  7  8  15 16 17  24 25 26
            DDD                      45 46 47
            DDD                      48 49 50
            DDD                      51 52 53
    
    '''

    def __init__(self):
        self._instantiate()
        
    def _instantiate(self):
        self.cube = {}
        
        return self.cube
    
    def _load(self, parms):
        result = check._check(parms)
        status = result['status']
        
        if status == 'ok':
            cube_parms = parms.get('cube')
            cube_parms = list(cube_parms)
                        
            faces = (
                Square(pos=RIGHT, colors=(cube_parms[13], None, None)),
                Square(pos=LEFT,  colors=(cube_parms[31], None, None)),
                Square(pos=UP,    colors=(None, cube_parms[40],  None)),
                Square(pos=DOWN,  colors=(None, cube_parms[49], None)),
                Square(pos=FRONT, colors=(None, None, cube_parms[4])),
                Square(pos=BACK,  colors=(None, None, cube_parms[22])))
            edges = (
                Square(pos=RIGHT + UP,    colors=(cube_parms[10], cube_parms[41], None)),
                Square(pos=RIGHT + DOWN,  colors=(cube_parms[16], cube_parms[50], None)),
                Square(pos=RIGHT + FRONT, colors=(cube_parms[12], None, cube_parms[5])),
                Square(pos=RIGHT + BACK,  colors=(cube_parms[14], None, cube_parms[21])),
                Square(pos=LEFT + UP,     colors=(cube_parms[28], cube_parms[39], None)),
                Square(pos=LEFT + DOWN,   colors=(cube_parms[34], cube_parms[48], None)),
                Square(pos=LEFT + FRONT,  colors=(cube_parms[32], None, cube_parms[3])),
                Square(pos=LEFT + BACK,   colors=(cube_parms[30], None, cube_parms[23])),
                Square(pos=UP + FRONT,    colors=(None, cube_parms[43], cube_parms[1])),
                Square(pos=UP + BACK,     colors=(None, cube_parms[37], cube_parms[19])),
                Square(pos=DOWN + FRONT,  colors=(None, cube_parms[46], cube_parms[7])),
                Square(pos=DOWN + BACK,   colors=(None, cube_parms[52], cube_parms[25])),
            )
            corners = (
                Square(pos=RIGHT + UP + FRONT,   colors=(cube_parms[9], cube_parms[44], cube_parms[2])),
                Square(pos=RIGHT + UP + BACK,    colors=(cube_parms[11], cube_parms[38], cube_parms[18])),
                Square(pos=RIGHT + DOWN + FRONT, colors=(cube_parms[15], cube_parms[47], cube_parms[8])),
                Square(pos=RIGHT + DOWN + BACK,  colors=(cube_parms[17], cube_parms[53], cube_parms[24])),
                Square(pos=LEFT + UP + FRONT,    colors=(cube_parms[29], cube_parms[42], cube_parms[0])),
                Square(pos=LEFT + UP + BACK,     colors=(cube_parms[27], cube_parms[36], cube_parms[20])),
                Square(pos=LEFT + DOWN + FRONT,  colors=(cube_parms[35], cube_parms[6], cube_parms[45])),
                Square(pos=LEFT + DOWN + BACK,   colors=(cube_parms[33], cube_parms[51], cube_parms[26])),
            )
    
            self.squares = faces + edges + corners
            self.cube['faces'] = faces
            self.cube['edges'] = edges
            self.cube['corners'] = corners
            
            results = {'status': status, 'cube': self.cube}
            return results
        else:
            results = {'status': status}
            return results
      
    def _get_face(self, face):
        valid_face = self._is_face_valid(face)
        if valid_face != 'error: Invalid input':
            status = 'valid'
            
            face_list = [s for s in self.squares if s.pos.dot(valid_face) > 0]
            results = {'status': status, 'face': face_list}
            return results
        else:
            status = 'error: Invalid input'
            results = {'status': status}
            return results
    
    def _get_final_cube(self):
        final_cube = [''] * 54

        for square in self.squares:
            if square.pos == RIGHT:
                final_cube[13] = square.colors[0]
            elif square.pos == LEFT:
                final_cube[31] = square.colors[0]
            elif square.pos == UP:
                final_cube[40] = square.colors[1]   
            elif square.pos == DOWN:
                final_cube[49] = square.colors[1]
            elif square.pos == FRONT:
                final_cube[4] = square.colors[2]
            elif square.pos == BACK:
                final_cube[22] = square.colors[2]
            elif square.pos == RIGHT + UP:
                final_cube[10] = square.colors[0]
                final_cube[41] = square.colors[1]
            elif square.pos == RIGHT + DOWN:
                final_cube[16] = square.colors[0]
                final_cube[50] = square.colors[1]
            elif square.pos == RIGHT + FRONT:
                final_cube[12] = square.colors[0]
                final_cube[5] = square.colors[2]
            elif square.pos == RIGHT + BACK:
                final_cube[14] = square.colors[0]
                final_cube[21] = square.colors[2]
            elif square.pos == LEFT + UP:
                final_cube[28] = square.colors[0]
                final_cube[39] = square.colors[1]
            elif square.pos == LEFT + DOWN:
                final_cube[34] = square.colors[0]
                final_cube[48] = square.colors[1]
            elif square.pos == LEFT + FRONT:
                final_cube[32] = square.colors[0]
                final_cube[3] = square.colors[2]
            elif square.pos == LEFT + BACK:
                final_cube[30] = square.colors[0]
                final_cube[23] = square.colors[2]
            elif square.pos == UP + FRONT:
                final_cube[43] = square.colors[1]
                final_cube[1] = square.colors[2]
            elif square.pos == UP + BACK:
                final_cube[37] = square.colors[1]
                final_cube[19] = square.colors[2]
            elif square.pos == DOWN + FRONT:
                final_cube[46] = square.colors[1]
                final_cube[7] = square.colors[2]
            elif square.pos == DOWN + BACK:
                final_cube[52] = square.colors[1]
                final_cube[25] = square.colors[2]
            elif square.pos == RIGHT + UP + FRONT:
                final_cube[9] = square.colors[0]
                final_cube[44] = square.colors[1]
                final_cube[2] = square.colors[2]
            elif square.pos == RIGHT + UP + BACK:
                final_cube[11] = square.colors[0]
                final_cube[38] = square.colors[1]
                final_cube[18] = square.colors[2]
            elif square.pos == RIGHT + DOWN + FRONT:
                final_cube[15] = square.colors[0]
                final_cube[47] = square.colors[1]
                final_cube[8] = square.colors[2]
            elif square.pos == RIGHT + DOWN + BACK:
                final_cube[17] = square.colors[0]
                final_cube[53] = square.colors[1]
                final_cube[24] = square.colors[2]
            elif square.pos == LEFT + UP + FRONT:
                final_cube[29] = square.colors[0]
                final_cube[42] = square.colors[1]
                final_cube[0] = square.colors[2]
            elif square.pos == LEFT + UP + BACK:
                final_cube[27] = square.colors[0]
                final_cube[36] = square.colors[1]
                final_cube[20] = square.colors[2]
            elif square.pos == LEFT + DOWN + FRONT:
                final_cube[35] = square.colors[0]
                final_cube[6] = square.colors[1]
                final_cube[45] = square.colors[2]
            elif square.pos == LEFT + DOWN + BACK:
                final_cube[33] = square.colors[0]
                final_cube[51] = square.colors[1]
                final_cube[26] = square.colors[2]
        
        return ''.join(final_cube)

    def _is_face_valid(self, face):
        valid_faces = ['RIGHT', 'LEFT', 'UP', 'DOWN', 'FRONT', 'BACK']
        
        if type(face) == str:
            for valid_face in valid_faces:
                if face.upper() == valid_face:
                    return self._face_with_name(valid_face)
        else:
            return 'error: Invalid input'
    
    def _face_with_name(self, name):
        if name == 'RIGHT':
            return RIGHT
        elif name == 'LEFT':
            return LEFT
        elif name == 'UP':
            return UP
        elif name == 'DOWN':
            return DOWN
        elif name == 'FRONT':
            return FRONT
        elif name == 'BACK':
            return BACK
    
    def _find_square(self, *colors):
        
        for s in self.squares:
            if s.colors.count(None) == 3 - len(colors) and all(c in s.colors for c in colors):
                return s
    
    def colors(self):
        return set(c for square in self.squares for c in square.colors if c is not None)

    def left_color(self): return self.cube['faces'][1].colors[0]
    def right_color(self): return self.cube['faces'][0].colors[0]
    def up_color(self): return self.cube['faces'][2].colors[1]
    def down_color(self): return self.cube['faces'][3].colors[1]
    def front_color(self): return self.cube['faces'][4].colors[2]
    def back_color(self): return self.cube['faces'][5].colors[2]

    def _color_list(self):
        right = [p.colors[0] for p in sorted(self._get_face(RIGHT), key=lambda p: (-p.pos.y, -p.pos.z))]
        left  = [p.colors[0] for p in sorted(self._get_face(LEFT),  key=lambda p: (-p.pos.y, p.pos.z))]
        up    = [p.colors[1] for p in sorted(self._get_face(UP),    key=lambda p: (p.pos.z, p.pos.x))]
        down  = [p.colors[1] for p in sorted(self._get_face(DOWN),  key=lambda p: (-p.pos.z, p.pos.x))]
        front = [p.colors[2] for p in sorted(self._get_face(FRONT), key=lambda p: (-p.pos.y, p.pos.x))]
        back  = [p.colors[2] for p in sorted(self._get_face(BACK),  key=lambda p: (-p.pos.y, -p.pos.x))]

        return (up + left[0:3] + front[0:3] + right[0:3] + back[0:3] + left[3:6] + front[3:6] + right[3:6] + back[3:6]
                   + left[6:9] + front[6:9] + right[6:9] + back[6:9] + down)
        
        