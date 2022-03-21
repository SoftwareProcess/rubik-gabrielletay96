import rubik.rotate as rotate
import rubik.cube as cube

# dev strategy
#    validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'


def _solve(parms):
    status = _validateParms(parms)
    results = {}
    
    if status == 'ok':
        myCube = cube.Cube()
        results = myCube._load(parms)
        cube_dict = results['cube']
        rotation_cmds = list(parms['rotate'])
        
        rotator = rotate.RotateCube(cube_dict)

        for cmd in rotation_cmds:
            rotator_dict = rotator._gather_rotation_codes(cmd)
            final_cube = rotator._rotate_cube(rotator_dict)
        
        results = {'status': status, 'cube': final_cube}
        return results
    else:
        results = {'status': status}
        return results

    

def _validateParms(parms):
    status = rotate._check(parms)
    
    if status == 'ok':
        testCube = cube.Cube()
        results = testCube._load(parms)
        status = results['status']
    
    return status
