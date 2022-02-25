import rubik.check as check 

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self):
        self._instantiate()
        
    def _instantiate(self):
        self.cube = {1:[], 2: [], 3: [], 4: [], 5: [], 6: []}
    
    def _get(self, face):
        return self.cube[face]
    
    def _load(self, parms):        
        result = check._check(parms)
        status = result['status']
        
        if status == 'ok':
            cube_parms = parms.get('cube')
    
            self.cube[1] = cube_parms[0:8]
            self.cube[2] = cube_parms[9:17]
            self.cube[3] = cube_parms[18:26]
            self.cube[4] = cube_parms[27:35]
            self.cube[5] = cube_parms[36:44]
            self.cube[6] = cube_parms[45:53]
            return status
        else:
            return status

 