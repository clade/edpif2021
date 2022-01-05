from pyqtgraph.Qt import QtCore, QtGui
import threading
from time import time, sleep

class PeriodicCallback(threading.Thread):
    want_to_terminate = False
    def __init__(self, display_time, period=0.1):
        self.period = period
        self.display_time = display_time
        threading.Thread.__init__(self)
    
    def run(self):
        self.t0 = time()
        while not self.want_to_terminate:
            self.display_time(time() - self.t0)
            sleep(self.period)



class StopWatchWindows(QtGui.QWidget):
    def __init__(self):
        self.app = QtGui.QApplication([])
        QtGui.QWidget.__init__(self)
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)
        
        startstop = QtGui.QPushButton('Start', self)
        label = QtGui.QLabel(self)
        
        main_layout.addWidget(startstop)
        main_layout.addWidget(label)

        startstop.clicked.connect(self.on_startstop_clicked)
        
        self.label = label
        self.startstop = startstop

        self.set_time(0)

        
    def on_startstop_clicked(self):
        if self.startstop.text()=='Start':
            self.thread = PeriodicCallback(display_time=self.set_time)
            self.thread.start()
            self.startstop.setText('Stop')
        else:
            self.thread.want_to_terminate = True
            self.startstop.setText('Start')
            
            
    def set_time(self, t):
        hour = t//3600
        t = t%3600
        minutes = t//60
        t = t%60
        seconds = t//1
        rest = t%1
        self.label.setText(f'{int(hour):02d}:{int(minutes):02d}:{int(seconds):02d}:{int(rest*100):02d}')
        
if __name__=='__main__':
    main = StopWatchWindows()
    main.show()
    main.app.exec_()
    
        