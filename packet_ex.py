#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Packet Exploration
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
from gnuradio import zeromq



from gnuradio import qtgui

class packet_ex(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Packet Exploration", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Packet Exploration")
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

        self.settings = Qt.QSettings("GNU Radio", "packet_ex")

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
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_msg_sink_0 = zeromq.push_msg_sink('tcp://127.0.0.1:50261', 100, True)
        self.zeromq_pull_msg_source_0 = zeromq.pull_msg_source('tcp://127.0.0.1:50261', 100, False)
        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, 'Send', 'Input', False, True, '', None)
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.blocks_message_debug_0 = blocks.message_debug(True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.zeromq_push_msg_sink_0, 'in'))
        self.msg_connect((self.zeromq_pull_msg_source_0, 'out'), (self.blocks_message_debug_0, 'print'))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "packet_ex")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=packet_ex, options=None):

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
