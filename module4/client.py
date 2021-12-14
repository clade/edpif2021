import rpyc

class RemoteSCPI(object):
 
    def __init__(self, host, port):
        self._conn = rpyc.connect(host, port)
        self._inst = self._conn.root.instrument()
 
    def write(self, command):
        self._inst.write(command);
 
    def read(self):
        return self._inst.read()

    def ask(self, command):
        return self._inst.ask(command)        


#scope = RemoteSCPI('localhost', 18861)
