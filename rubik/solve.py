import rubik.rotate as rotate
import rubik.cube as cube
from pickle import TRUE

# dev strategy
#    validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'


''' SOLVER '''

class Solver:

    def __init__(self, parms):
        status = self._validateParms(parms)
        results = {}
    
        if status == 'ok':
            self.cube = cube.Cube()
            results = self.cube._load(parms)        
            
            rotation_cmds = list(parms['rotate'])
            if '' == rotation_cmds:
                self.left_square  = self.cube._find_square(self.cube.left_color())
                self.right_square = self.cube._find_square(self.cube.right_color())
                self.up_square   = self.cube._find_square(self.cube.up_color())
                self.down_square  = self.cube._find_square(self.cube.down_color())
                
                results = self.solve()
            else:
                results = self._solve_by_rotation_cmds(rotation_cmds)
            
            return results
        else:
            results = {'status': status}
            return results

    def _solve_by_rotation_cmds(self, cmds):
        for cmd in cmds:
            pass
            #rotator_dict = rotator._gather_rotation_codes(cmd)
            #final_cube = rotator._rotate_cube(rotator_dict)
            #results = {'status': status, 'cube': final_cube}
            #return results
    
    def solve(self):
        self.cross()
        
        front_face_squares = cube.Cube._get_face('FRONT')
        right_face_squares = cube.Cube._get_face('RIGHT')
        back_face_squares = cube.Cube._get_face('BACK')
        left_face_squares = cube.Cube._get_face('LEFT')
        up_face_squares = cube.Cube._get_face('UP')
        down_face_squares = cube.Cube._get_face('DOWN')
        
        final_cube = front_face_squares + right_face_squares + back_face_squares + left_face_squares + up_face_squares + down_face_squares
        
        results = {'status': 'ok', 'cube': final_cube}
        return results  

    def cross(self):
        self.up_daisy()
        
        # Correct position and turn 180 degrees to make bottom cross
        up_lft_square = self.cube._find_square(self.cube.up_color(), self.cube.left_color())
        self.current_square = up_lft_square
        self._correct_pos(cube.LEFT)
        rotate.RotateCube.L_cwise()
        rotate.RotateCube.L_cwise()
        
        up_rght_square = self.cube._find_square(self.cube.up_color(), self.cube.right_color())
        self.current_square = up_rght_square
        self._correct_pos(cube.RIGHT)
        rotate.RotateCube.R_cwise()
        rotate.RotateCube.R_cwise()
        
        up_frnt_square = self.cube._find_square(self.cube.up_color(), self.cube.front_color())
        self.current_square = up_frnt_square
        self._correct_pos(cube.FRONT)
        rotate.RotateCube.F_cwise()
        rotate.RotateCube.F_cwise()
        
        up_bck_square = self.cube._find_square(self.cube.up_color(), self.cube.back_color())
        self.current_square = up_bck_square
        self._correct_pos(cube.BACK)
        rotate.RotateCube.B_cwise()
        rotate.RotateCube.B_cwise()
        
    def up_daisy(self):
        up_lft_square = self.cube._find_square(self.cube.up_color(), self.cube.left_color())
        up_rght_square = self.cube._find_square(self.cube.up_color(), self.cube.right_color())
        up_frnt_square = self.cube._find_square(self.cube.up_color(), self.cube.front_color())
        up_bck_square = self.cube._find_square(self.cube.up_color(), self.cube.back_color())
        
        self._find_daisy_rotation_by_pos(up_lft_square.pos)
        self._find_daisy_rotation_by_pos(up_rght_square.pos)
        self._find_daisy_rotation_by_pos(up_frnt_square.pos)
        self._find_daisy_rotation_by_pos(up_bck_square.pos)
    
    def _find_daisy_rotation_by_pos(self, pos):
        #in_corr_pos = 0
        if pos == cube.RIGHT + cube.FRONT:
            rotate.RotateCube.f_ccwise()
        
        elif pos == cube.RIGHT + cube.UP:
            rotate.RotateCube.R_cwise()
            rotate.RotateCube.B_cwise()
        
        elif pos == cube.RIGHT + cube.DOWN:
            rotate.RotateCube.R_cwise()
            rotate.RotateCube.f_ccwise()
            
        elif pos == cube.RIGHT + cube.BACK:
            rotate.RotateCube.B_cwise()
            
        elif pos == cube.LEFT + cube.UP:
            rotate.RotateCube.l_ccwise()
            rotate.RotateCube.b_ccwise()
        
        elif pos == cube.LEFT + cube.DOWN:
            rotate.RotateCube.L_cwise()
            rotate.RotateCube.b_ccwise()
            
        elif pos == cube.LEFT + cube.FRONT:
            rotate.RotateCube.F_cwise()
            
        elif pos == cube.LEFT + cube.BACK:
            rotate.RotateCube.b_ccwise()
        
        elif pos == cube.FRONT + cube.UP:
            rotate.RotateCube.f_ccwise()
            rotate.RotateCube.l_ccwise()
            
        elif pos == cube.BACK + cube.UP:
            rotate.RotateCube.b_ccwise()
            rotate.RotateCube.r_ccwise()
        
        elif pos == cube.DOWN + cube.FRONT:
            rotate.RotateCube.F_cwise()
            rotate.RotateCube.F_cwise()
            
        elif pos == cube.DOWN + cube.FRONT:
            rotate.RotateCube.B_cwise()
            rotate.RotateCube.B_cwise()
    
    def _correct_pos(self, side):
        zeros = self.current_square.pos - side
        if zeros.count == 2:
            return True
        else:
            rotate.RotateCube.U_cwise()
            result = self._correct_pos(side)
            return result
    
    def _validateParms(self, parms):
        status = rotate._check(parms)
        
        if status == 'ok':
            testCube = cube.Cube()
            results = testCube._load(parms)
            status = results['status']
        
        return status