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
import pickle
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

textboxValue = ""
key = ""
nonce = ""

class my_sync_block(gr.sync_block):
    """
    reads input from a message port
    outputs encrypted data using AES-GCM 
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name = "AES-GCM Encryption",
            in_sig = None,
            out_sig = [np.byte, np.byte, np.byte])
        self.message_port_register_in(pmt.intern('msg_in'))
        self.message_port_register_out(pmt.intern('clear_input'))
        self.set_msg_handler(pmt.intern('msg_in'), self.handle_msg)

    def handle_msg(self, msg):
        global textboxValue
        global key
        global nonce
        
        message = pmt.symbol_to_string (msg)
        data = bytes(message, 'ascii')
        
        key = AESGCM.generate_key(bit_length=128)
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        encryptText = aesgcm.encrypt(nonce, data, None)
        textboxValue = encryptText
        
        print("---Start of Encrypt---")
        
        print("TextboxValue: ")
        print(textboxValue)
        print("Key: ")
        print(key)
        print("Nonce: ")
        print(nonce)
                
        #convert to string
        #textboxValue = textboxValue.hex()   #changed from .str()
        #key = key.hex()
        #nonce = nonce.hex()
        textboxValue = str(textboxValue)
        key = str(key)
        nonce = str(nonce)
        
        
        print("TextboxValue (Hex): ")
        print(textboxValue)
        print("Key (Hex): ")
        print(key)
        print("Nonce (Hex): ")
        print(nonce)
               

    
    def work(self, input_items, output_items):
        global textboxValue
        global key
        global nonce
        
        # get length of string
        _len = len(textboxValue)
        __len = len(key)
        ___len = len(nonce)
        if (_len > 0):
            
            # store elements in output array
            for x in range(_len):
                output_items[0][x] = ord(textboxValue[x])
            print("---End of Encrypt---")
            textboxValue = ""
            for y in range(__len):
                output_items[1][y] = ord(key[y])
            for z in range(___len):
                output_items[2][z] = ord(nonce[z])
            self.message_port_pub(pmt.intern('clear_input'), pmt.intern(''))
            return (_len)
        else:
            return (0)

