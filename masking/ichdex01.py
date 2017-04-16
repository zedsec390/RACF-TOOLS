# the original racf encoding / masking algorithm #
#  used to be the ichdex01 exit / program #
#  usage  python ichdex01.py PASSWORD
#      example hashes
#
#      F5478251A02C4C4C ==  XCFTS
#      C16337002C4C4C4C ==  OMVS
#      F09B70807C4C4C4C ==  SYS1

import sys
from a2e_converter import a2e 

class ichdex01:
    def __init(self):
        return

    def enc(self,val):
        n = ""
        pn = list()
        if len(val) > 8:
            val = val[0:8]
        val = val + (" " * (8 - len(val)))
        for i in range(0,8):
            n = n + a2e(val[i])

        #  Blown up for show and tell purposes
        #  A ret {0:08X}".format((((n<<1) ^ n)>>4) ^ n)
        #  would suffice to replace the below

        i_pass = int(n.encode('hex'),16)  # convert pass to integer
        i_tmp = i_pass << 1               # Left shift by 1
        i_tmp = i_tmp ^ i_pass            # XOR step1 output with orig pass
        i_tmp = i_tmp >> 4                # Right shift step2 by 4
        i_tmp = i_tmp ^ i_pass            # XOR step3 output with orig pass
        i_fin = "{0:X}".format(i_tmp)     # convert int back to bytes

        return i_fin                      # return


if __name__ == "__main__":

    e = ichdex01()
    if len(sys.argv) > 1:
        val = sys.argv[1]
        print e.enc(val)
    else:
        test = e.enc("XCFTS")
        if test == "F5478251A02C4C4C":
            print("Test succeeded")
        else:
            print("Test failed")
            sys.exit(-1)
