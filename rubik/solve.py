import rubik.rotate as rotate
import rubik.cube as cube

# dev strategy
#    validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'


''' SOLVER '''

class Solver:

    def __init__(self):
        self.results = {}
    
    def _solve(self, parms):
        status = self._validateParms(parms)
    
        if status == 'ok':
            self.cube = cube.Cube()
            results = self.cube._load(parms)
            self.rotator = rotate.RotateCube(self.cube)       
            
            if parms['rotate'] == '':                
                self._cross()
                self._bottom()
                rotation_cmds = self.rotator.command_seq
            else:
                rotation_cmds = list(parms['rotate'])
                self._solve_by_rotation_cmds(rotation_cmds)
                
            # Combine string of faces for final cube
            final_cube = self.cube._get_final_cube()
            
            results = {'status': 'ok', 'cube': final_cube, 'solution': rotation_cmds}
            return results
        else:
            results = {'status': status, 'cube': None}
            return results

    def _layer_two(self):
        pass
    
    def _bottom(self):
        
        #front
        self.current_aim_pos = (1, -1, 1)
        self.current_colors = [self.right_color, self.down_color, self.front_color]
        rght_dwn_frnt_square = self.cube._find_square(*self.current_colors)
        if rght_dwn_frnt_square.pos == self.current_aim_pos and rght_dwn_frnt_square.colors == self.current_colors:
            pass
        elif rght_dwn_frnt_square.pos == (1, 1, 1) or rght_dwn_frnt_square.pos == self.current_aim_pos:
            self._set_corners('R')
        
        else:
            if rght_dwn_frnt_square.pos[1] == -1:
                if rght_dwn_frnt_square.pos[0] == -1:
                    self.rotator.l_ccwise()
                    self.rotator.u_ccwise()
                    self._set_corners('R')
                    
        #right side
        self.current_aim_pos = (1, -1, -1)
        self.current_colors = [self.right_color, self.down_color, self.back_color]
        rght_dwn_bck_square = self.cube._find_square(*self.current_colors )
        
        if rght_dwn_bck_square.pos == self.current_aim_pos and rght_dwn_bck_square.colors == self.current_colors:
            pass
        elif rght_dwn_bck_square.pos == (1, 1, -1) or rght_dwn_bck_square.pos == self.current_aim_pos:
            self._set_corners('B')
            
        else:
            if rght_dwn_bck_square.pos[1] == -1:
                if rght_dwn_bck_square.pos[2] == 1:
                    self.rotator.f_ccwise()
                    self.rotator.u_ccwise()
                    self._set_corners('B')
        
        #back side
        self.current_aim_pos = (-1, -1, -1)
        self.current_colors = [self.left_color, self.down_color, self.back_color]
        lft_dwn_bck_square = self.cube._find_square(*self.current_colors)
        
        if lft_dwn_bck_square.pos == self.current_aim_pos and lft_dwn_bck_square.colors == self.current_colors:
            pass
        elif lft_dwn_bck_square.pos == (-1, 1, -1) or lft_dwn_bck_square.pos == self.current_aim_pos:
            self._set_corners('L')
        else:
            if lft_dwn_bck_square.pos[1] == -1:
                if lft_dwn_bck_square.pos[0] == 1:
                    self.rotator.r_ccwise()
                    self.rotator.u_ccwise()
                    self._set_corners('L')
            
        #left side
        self.current_aim_pos = (-1, -1, 1)
        self.current_colors = [self.left_color, self.down_color, self.front_color]
        lft_dwn_frnt_square = self.cube._find_square(*self.current_colors)
        
        if lft_dwn_frnt_square.pos == self.current_aim_pos and lft_dwn_frnt_square.colors == self.current_colors:
            pass
        elif lft_dwn_frnt_square.pos == (-1, 1, 1) or lft_dwn_frnt_square.pos == self.current_aim_pos:
            self._set_corners('F')
            
        else:
            if lft_dwn_frnt_square.pos[1] == -1:
                if lft_dwn_frnt_square.pos[2] == -1:
                    self.rotator.b_ccwise()
                    self.rotator.u_ccwise()
                    self._set_corners('F')
            
    def _cross(self):
        # Set colors
        self.left_color = self.cube.left_color()
        self.right_color = self.cube.right_color()
        self.down_color = self.cube.down_color()
        self.front_color = self.cube.front_color()
        self.back_color =  self.cube.back_color()
        
        # Gather cross squares
        self.down_lft_square = self.cube._find_square(self.down_color, self.left_color)
        self.down_rght_square = self.cube._find_square(self.down_color, self.right_color)
        self.down_frnt_square = self.cube._find_square(self.down_color, self.front_color)
        self.down_bck_square = self.cube._find_square(self.down_color, self.back_color)
        
        # Begin building cross
        self._check_cross()
        
        if self.correct_positions < 4:
            self._daisy()

            # Correct position and turn 180 degrees to make bottom cross
            down_lft_square = self.cube._find_square(self.cube.down_color(), self.cube.left_color())
            self.current_square = down_lft_square
            self.rotator.L_cwise()
            self.rotator.L_cwise()
            
            down_rght_square = self.cube._find_square(self.cube.down_color(), self.cube.right_color())
            self.current_square = down_rght_square
            self.rotator.R_cwise()
            self.rotator.R_cwise()
            
            down_frnt_square = self.cube._find_square(self.cube.down_color(), self.cube.front_color())
            self.current_square = down_frnt_square
            self.rotator.F_cwise()
            self.rotator.F_cwise()
            
            down_bck_square = self.cube._find_square(self.cube.down_color(), self.cube.back_color())
            self.current_square = down_bck_square
            self.rotator.B_cwise()
            self.rotator.B_cwise()
    
    def _check_cross(self):
        self.correct_positions = 0
        
        if self.down_lft_square.pos == (-1, -1, 0):
            self.correct_positions += 1
            
        if self.down_rght_square.pos == (1, -1, 0):
            self.correct_positions += 1
        
        if self.down_frnt_square.pos == (0, -1, 1):
            self.correct_positions += 1

        if self.down_bck_square.pos == (0, -1, -1):
            self.correct_positions += 1
                   
    def _daisy(self):
        if self.down_lft_square.pos == (-1, 1, 0):
            if self.down_lft_square.colors[1] == self.down_color:
                pass
            else:
                pass # if in correct position but wrong color order do this
        else:
            self._find_daisy_rotation_by_pos(self.down_lft_square, (-1, 1, 0), self.down_color, self.left_color)
            
        if self.down_rght_square.pos == (1, 1, 0):
            if self.down_rght_square.colors[1] == self.down_color:
                pass
        else:
            self._find_daisy_rotation_by_pos(self.down_rght_square, (1, 1, 0), self.down_color, self.right_color)
        
        if self.down_frnt_square.pos == (0, 1, 1):
            if self.down_frnt_square.colors[1] == self.down_color:
                pass
        else:
            self._find_daisy_rotation_by_pos(self.down_frnt_square, (0, 1, 1), self.down_color, self.front_color)
        
        if self.down_bck_square.pos == (0, 1, -1):
            if self.down_bck_square.colors[1] == self.down_color:
                pass
        else:
            self._find_daisy_rotation_by_pos(self.down_bck_square, (0, 1, -1), self.down_color, self.back_color)
        
        
    def _find_daisy_rotation_by_pos(self, square, corr_pos, color1, color2):
        
        if square.pos[1] == 1:
            if square.colors[1] == self.down_color:
                return 0
            else:
                if square.pos[0] == 1:
                    self.rotator.R_cwise()
                    self.rotator.B_cwise()
                    
                elif square.pos[0] == -1:
                    self.rotator.l_ccwise()
                    self.rotator.b_ccwise()
                    
                elif square.pos[2] == 1:
                    self.rotator.f_ccwise()
                    self.rotator.R_cwise()
                    
                elif square.pos[2] == -1:
                    self.rotator.b_ccwise()
                    self.rotator.r_ccwise()
                    
        elif square.pos[1] == -1:    
            if square.colors[1] == self.down_color:
                #rotate 180
                if square.pos[0] == 1:
                    self.rotator.R_cwise()
                    self.rotator.R_cwise()
                    
                elif square.pos[0] == -1:
                    self.rotator.L_cwise()
                    self.rotator.L_cwise()
                    
                elif square.pos[2] == 1:
                    self.rotator.F_cwise()
                    self.rotator.F_cwise()
                    
                elif square.pos[2] == -1:
                    self.rotator.B_cwise()
                    self.rotator.B_cwise()
            else:
                if square.pos[0] == 1:
                    self.rotator.R_cwise()
                    self.rotator.f_ccwise()
                    
                elif square.pos[0] == -1:
                    self.rotator.l_ccwise()
                    self.rotator.F_cwise()
                    
                elif square.pos[2] == 1:
                    self.rotator.f_ccwise()
                    self.rotator.R_cwise()
                    
                elif square.pos[2] == -1:
                    self.rotator.b_ccwise()
                    self.rotator.L_cwise()
            
        else:
            if square.colors[0] == self.down_color:
                if square.pos[2] == -1:
                    self.rotator.B_cwise()
                    new_pos = self._find_new_pos(color1, color2)
                    if new_pos == corr_pos:
                        return 0
                    else:
                        self.rotator.b_ccwise()
                        self.rotator.b_ccwise()
                        
                elif square.pos[2] == 1:
                    self.rotator.F_cwise()
                    new_pos = self._find_new_pos(color1, color2)
                    if new_pos == corr_pos:
                        return 0
                    else:
                        self.rotator.f_ccwise()
                        self.rotator.f_ccwise() 
            else:
                if square.pos[0] == -1:
                    self.rotator.L_cwise()
                    new_pos = self._find_new_pos(color1, color2)
                    if new_pos == corr_pos:
                        return 0
                    else:
                        self.rotator.l_ccwise()
                        self.rotator.l_ccwise()
                        
                elif square.pos[0] == 1:
                    self.rotator.R_cwise()
                    new_pos = self._find_new_pos(color1, color2)
                    if new_pos == corr_pos:
                        return 0
                    else:
                        self.rotator.r_ccwise()
                        self.rotator.r_ccwise()
    
    def _set_corners(self, rotation_letter):
        #check = False
        
        #while check == False:
        self._get_rotation(rotation_letter)
        
        curr_pos = self._find_new_pos()
        if curr_pos == self.current_aim_pos:
            pass
                #check = True
    
    def _find_new_pos(self):
        square = self.cube._find_square(*self.current_colors)
        
        return square.pos

    def _validateParms(self, parms):
        status = rotate._check(parms)
        
        if status == 'ok':
            testCube = cube.Cube()
            results = testCube._load(parms)
            status = results['status']
        
        return status
    
    def _solve_by_rotation_cmds(self, cmds):
        for cmd in cmds:
            if cmd == 'F': self.rotator.F_cwise()
            elif cmd == 'f': self.rotator.f_ccwise()
            elif cmd == 'B': self.rotator.B_cwise()
            elif cmd == 'b': self.rotator.b_ccwise()
            elif cmd == 'L': self.rotator.L_cwise()
            elif cmd == 'l': self.rotator.l_ccwise()
            elif cmd == 'R': self.rotator.R_cwise()
            elif cmd == 'r': self.rotator.r_ccwise()
            elif cmd == 'U': self.rotator.U_cwise()
            elif cmd == 'u': self.rotator.u_ccwise()
            elif cmd == 'D': self.rotator.D_cwise()
            elif cmd == 'd': self.rotator.d_ccwise()
            
    def _get_rotation(self, letter):
        if letter == 'R':
            self.rotator.R_cwise()
            self.rotator.U_cwise()
            self.rotator.r_ccwise()
            self.rotator.u_ccwise()

        elif letter == 'L':
            self.rotator.L_cwise()
            self.rotator.U_cwise()
            self.rotator.l_ccwise()
            self.rotator.u_ccwise()
            
        elif letter == 'B':
            self.rotator.B_cwise()
            self.rotator.U_cwise()
            self.rotator.b_ccwise()
            self.rotator.u_ccwise()

        elif letter == 'F':
            self.rotator.F_cwise()
            self.rotator.U_cwise()
            self.rotator.f_ccwise()
            self.rotator.u_ccwise()
        