
from cynpy.can11xx import cani2c
from cynpy.atm import atm

class tsti2c (cani2c, atm):
    pass



if __name__ == '__main__':
    '''
    % python isp.py [cmd] [argv2] [...]
    % python isp.py rev
    % python isp.py write bc 8
    '''
    import cynpy.i2c as i2c
    i2cmst = i2c.choose_i2cmst (rpt=i2c.FALSE)
    tstmst = tsti2c(busmst=i2cmst, deva=0x70)

    import cynpy.basic as cmd
    if not cmd.no_argument ():
        if i2cmst!=0:
            cmd.tstmst_func (tstmst)
