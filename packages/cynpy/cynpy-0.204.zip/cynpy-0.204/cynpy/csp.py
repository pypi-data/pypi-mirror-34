
from cynpy.canm0 import canm0
from cynpy.atm import atm

from cynpy.can11xx import can11xx

class tstcsp (can11xx, atm):
    def __init__ (me, busmst, rpt=0):
        me.busmst = busmst # SFR master (canm0)
        super(me.__class__, me).__init__ () # SFR target

        if me.sfr.revid and rpt:
            print 'CSP master finds %s, %d' % (me.sfr.name, me.busmst.TxOrdrs)


    def is_master_rdy (me):
        ''' Is this master ready for issuing things?
        '''
        return me.busmst.busmst.handle


    def sfrwx (me, adr, wdat):
        return me.busmst.cspw (adr, 1, wdat)


    def sfrwi (me, adr, wdat):
        return me.busmst.cspw (adr, 0, wdat)


    def sfrrx (me, adr, cnt):
        return me.busmst.cspr (adr, 1, cnt)


    def sfrri (me, adr, cnt):
        return me.busmst.cspr (adr, 0, cnt)


    def insert_dummy (me, rawcod, block):
        '''
        load the memory file 'memfile' and insert dummys
        '''
        lowcod = [] # low-byte
        wrcod = []
        for xx in rawcod:                
            if len(lowcod)>0 or me.sfr.nbyte==1:
                if len(wrcod)%block > 0:
                    for yy in range(me.sfr.dummy):
                        wrcod += [0xdd]
                wrcod += lowcod + [xx]
                lowcod = []
            else:
                lowcod = [xx]

        return (len(rawcod), wrcod)


    def nvm_prog_block (me, addr, wrcod, rawsz, hiv=0):
        """
        override atm's method
        calc. block length
        insert dummy byte(s)
        """
        w_unit = (me.sfr.bufsz - me.sfr.nbyte - 2) \
                              / (me.sfr.nbyte + me.sfr.dummy) # CSP command needs 2 bytes
        block = (me.sfr.nbyte + me.sfr.dummy) * w_unit \
               + me.sfr.nbyte # optimize block size by CSP buffer

        (rawsz, dmycod) = me.insert_dummy (wrcod, block)
        super(me.__class__, me).nvm_prog_block (addr, dmycod, rawsz, hiv, block)


    def nvm_comp_block (me, args, block=32):
        '''
        limit block size by CSP buffer
        '''
        super(me.__class__, me).nvm_comp_block (args, block)

        

if __name__ == '__main__':
    '''
    % python csp.py [cmd|SOP*] [cmd] [...]
    % python csp.py query
    % python csp.py 1 read bb
    '''
    import cynpy.i2c as i2c
    i2cmst = i2c.choose_i2cmst (rpt=i2c.FALSE)

    import sys
    import cynpy.basic as cmd
    if not cmd.no_argument ():
        if i2cmst != 0:
            if sys.argv[1]=='query' : # query SOP*
                cspbdg = canm0(i2cmst, 0x70) # no SOP*
                print cspbdg.probe (1)
            else:
                if cmd.argv_hex[1]>0 and cmd.argv_hex[1]<=5: # assign SOP* by command line
                    cspbdg = canm0(i2cmst, 0x70, cmd.argv_hex[1])
                    sys.argv = sys.argv[1:]
                    cmd.argv_hex = cmd.argv_hex[1:]
                    cmd.argv_dec = cmd.argv_dec[1:]
                else:
                    cspbdg = canm0(i2cmst, 0x70, 5)

                cspbdg.prltx.msk (0xff, 0x08) # enable auto-RX-GoodCRC
                tstmst = tstcsp(cspbdg)
                cmd.tstmst_func (tstmst)
                cspbdg.prltx.pop ()
