class FakeSCPI(object):
    _record = {'*IDN':"TEKTRONIX,DPO3014,C012048,CF:91.1CT FV:v2.16 "}
    def write(self, val):
        if ' ' in val:
            cmd, vals = val.split(' ')
            self._record[cmd] = vals

    def ask(self, val):
        assert val[-1]=='?'
        out = self._record.get(val[:-1], '')
        return out
