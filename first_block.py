#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Own Block Creation
# Author: Madeline Tippett
# GNU Radio version: 3.9.3.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import first_block_epy_block_0 as epy_block_0  # embedded python block
import first_block_epy_block_1 as epy_block_1  # embedded python block



from gnuradio import qtgui

class first_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Own Block Creation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Own Block Creation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "first_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 50000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, '', 'Input', False, False, '', None)
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.epy_block_1 = epy_block_1.my_sync_block()
        self.epy_block_0 = epy_block_0.my_sync_block()
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\notma\\OneDrive\\Desktop\\School\\KNE401 and 402 Honours\\Simulation\\Simulation Own Code\\nonce.txt', False)
        self.blocks_file_sink_2.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\notma\\OneDrive\\Desktop\\School\\KNE401 and 402 Honours\\Simulation\\Simulation Own Code\\keys.txt', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\notma\\OneDrive\\Desktop\\School\\KNE401 and 402 Honours\\Simulation\\Simulation Own Code\\decrypt_msg.txt', True)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\notma\\OneDrive\\Desktop\\School\\KNE401 and 402 Honours\\Simulation\\Simulation Own Code\\file_sink_ex.txt', False)
        self.blocks_file_sink_0.set_unbuffered(True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.epy_block_0, 'clear_input'), (self.qtgui_edit_box_msg_0, 'val'))
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.epy_block_0, 'msg_in'))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.epy_block_1, 1))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_file_sink_2, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.epy_block_1, 2))
        self.connect((self.epy_block_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.epy_block_0, 1), (self.blocks_throttle_0_0, 0))
        self.connect((self.epy_block_0, 2), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_file_sink_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "first_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)




def main(top_block_cls=first_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
