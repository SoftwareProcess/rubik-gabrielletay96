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

def get_rotation_from_face(face):
    """
    :param face: One of FRONT, BACK, LEFT, RIGHT, UP, DOWN
    :return: A pair (CW, CC) given the clockwise and counterclockwise rotations for that face
    """
    if face == RIGHT:   return "R", "r"
    elif face == LEFT:  return "L", "l"
    elif face == UP:    return "U", "u"
    elif face == DOWN:  return "D", "d"
    elif face == FRONT: return "F", "f"
    elif face == BACK:  return "B", "b"
    return None

class Square:

    def __init__(self, pos, colors):
        assert all(type(x) == int and x in (-1, 0, 1) for x in pos)
        assert len(colors) == 3
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
        else:
            raise ValueError(f"Must have 1, 2, or 3 colors - given colors={self.colors}")

    def rotate(self, matrix):
        original_pos = self.pos
        self.pos = matrix * self.pos

        rotation = self.pos - original_pos
        if not any(rotation):
            return  # no change occurred
        if rotation.count(0) == 2:
            rotation += matrix * rotation

        assert rotation.count(0) == 1, ("error: Invalid rotation")

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
        """
        :face: One of LEFT, RIGHT, UP, DOWN, FRONT, BACK
        :return: A list of squares on the given face
        """
        
        valid_face = self._is_face_valid(face)
        if valid_face != 'error: Invalid input':
            status = 'valid'
            
            cube = [s for s in self.squares if s.pos.dot(valid_face) > 0]
            results = {'status': status, 'cube': cube}
            return results
        else:
            status = 'error: Invalid input'
            results = {'status': status}
            return results
        

    def _slice(self, plane):
        """
        :param plane: A sum of any two of X_AXIS, Y_AXIS, Z_AXIS (e.g. X_AXIS + Y_AXIS)
        :return: A list of squares in the given plane
        """
        assert plane.count(0) == 1
        i = next((i for i, x in enumerate(plane) if x == 0))
        return [s for s in self.squares if s.pos[i] == 0]
    

    def _is_face_valid(self, face):
        valid_faces = ['RIGHT','LEFT', 'UP', 'DOWN', 'FRONT', 'BACK']
        
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
        """
        :return: A set containing the colors of all stickers on the cube
        """
        return set(c for square in self.squares for c in square.colors if c is not None)

    def left_color(self): return self[LEFT].colors[0]
    def right_color(self): return self[RIGHT].colors[0]
    def up_color(self): return self[UP].colors[1]
    def down_color(self): return self[DOWN].colors[1]
    def front_color(self): return self[FRONT].colors[2]
    def back_color(self): return self[BACK].colors[2]

    def _color_list(self):
        right = [p.colors[0] for p in sorted(self._get_face(RIGHT), key=lambda p: (-p.pos.y, -p.pos.z))]
        left  = [p.colors[0] for p in sorted(self._get_face(LEFT),  key=lambda p: (-p.pos.y, p.pos.z))]
        up    = [p.colors[1] for p in sorted(self._get_face(UP),    key=lambda p: (p.pos.z, p.pos.x))]
        down  = [p.colors[1] for p in sorted(self._get_face(DOWN),  key=lambda p: (-p.pos.z, p.pos.x))]
        front = [p.colors[2] for p in sorted(self._get_face(FRONT), key=lambda p: (-p.pos.y, p.pos.x))]
        back  = [p.colors[2] for p in sorted(self._get_face(BACK),  key=lambda p: (-p.pos.y, -p.pos.x))]

        return (up + left[0:3] + front[0:3] + right[0:3] + back[0:3]
                   + left[3:6] + front[3:6] + right[3:6] + back[3:6]
                   + left[6:9] + front[6:9] + right[6:9] + back[6:9] + down)
        
        