"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


import pmt
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

msg = ""

class my_sync_block(gr.sync_block):
    """
    reads encrypted data from a message port
    outputs decrypted message
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name = "AES-GCM Decryption",
            in_sig = [np.byte, np.byte, np.byte],
            out_sig = [np.byte])
        self.message_port_register_out(pmt.intern('msg_out'))
    
    def work(self, input_items, output_items):
        #global msg
        
        data = input_items[0]
        key = input_items[1]
        nonce = input_items[2]
        
        print("---Raw received data---")
        print("Type: ")
        print(type(data))
        print(type(key))
        print("TextboxValue: ")
        print(data)
        print("Key: ")
        print(key)
        print("Nonce: ")
        print(nonce)
        
        # AES-GCM        
        data = data.tostring()
        key = key.tostring()
        nonce = nonce.tostring()  
        
        print("---Array to string---")
        print("TextboxValue: ")
        print(data)
        print("Key: ")
        print(key)
        print("Nonce: ")
        print(nonce)
        
        data = data.decode('utf-8')
        key = key.decode('utf-8')
        
        print("---Just having hex values---")
        print(data)
        
        data = bytes.fromhex(data)
        key = bytes.fromhex(key)
        
        print("---Byte format from Hex format---")
        print("TextboxValue: ")
        print(data)
        print("Key: ")
        print(key)
        print("Nonce: ")
        print(nonce)
        
        aesgcm = AESGCM(key)
        msg = aesgcm.decrypt(nonce, data, None)
        #print(msg)
        
        _len(msg)
        
        #save to folder I guess
        if _len > 0:
            _len += 1
            msg += "/n"
            for x in range(_len):
                output_items[0][x] = ord(msg[x])
                msg = ""
                return(_len)
        else:
            return(0)
        