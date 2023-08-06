#!/usr/bin/env python
import os, sys, json, time, datetime, traceback as tb
from fastecdsa import ecdsa, keys, curve
from fastecdsa.point import Point
from cryptography.fernet import Fernet
from b85 import b85_encode, b85_decode
import yaml

__version__ = "1.0.1"

def long_encode(n): return b85_encode(bytearray.fromhex('{:064x}'.format(n)))
def long_decode(s): return long(b85_decode(s).encode('hex'), 16)

def _str2sk(sk):    return long_decode(sk)
def str2sk (st):    return _str2sk(*st.split(','))

def sk2str (sk):    return "%s" % long_encode(sk)

def _str2vk(x, y):  return Point(long_decode(x), long_decode(y), curve.P256)
def str2vk (st):    return _str2vk(*st.split(','))

def vk2str (vk):    return "%s,%s" % (long_encode(vk.x), long_encode(vk.y))

def _str2sig(r, s): return long_decode(r), long_decode(s)
def str2sig (st):   return _str2sig(*st.split(','))

def sig2str (rs):   return "%s,%s" % (long_encode(rs[0]),long_encode(rs[1]))


class Key(object):

    @classmethod
    def generate(_, sk=''):
        if not sk:
            sk = keys.gen_private_key(curve.P256)
        else:
            sk = str2sk(sk)
            pass
        vk = keys.get_public_key(sk, curve.P256)
        return _(vk2str(vk), sk2str(sk))

    def __init__(_, vkey, skey=''):
        if isinstance(vkey, Key):
            if skey: raise TypeError("cannot supply skey with a Key of vkey")
            skey = vkey.secret
            vkey = vkey.public
            pass
        _.vk = str2vk(vkey)
        _.sk = str2sk(skey) if skey else ''
        pass

    def sign(_, msg):
        if not _.sk: raise RuntimeError("Can't sign with no secret")
        return sig2str(ecdsa.sign(msg, _.sk))

    def test_verify(_, msg, sig): return ecdsa.verify(str2sig(sig), msg, _.vk)

    def verify(_, msg, sig):
        if not _.test_verify(msg, sig): raise RuntimeError("Verify Exception")
        return True
    
    def __repr__(_): return _.public

    def  __str__(_): return _.short

    @property
    def  short(_):   return long_encode(_.vk.x)[:16]

    @property
    def secret(_):   return long_encode(_.sk) if _.sk else ''

    @property
    def public(_):   return long_encode(_.vk.x)+','+long_encode(_.vk.y)

    @property
    def keys(_):     return [_.public, _.secret]

    pass # end class Key


class Envelope(object):

    @classmethod
    def raw_verify(_, msg, sig, public):
        return Key(public).verify(msg, sig)
    
    def verify(_, key):
        return _.raw_verify(_.msg, _.sig, key.public)

    @classmethod
    def raw_sign(_, msg, secret):
        key = Key.generate(secret)
        _ = _()
        _.msg = msg
        _.sig = key.sign(msg)
        _.verify(key)
        return _

    @classmethod
    def sign(_, msg, skey):
        return _.raw_sign(msg, skey.secret)

    def __repr__(_):
        return '%s\n%s\n' % (_.sig, _.msg)

    pass # end class Envelope


class YamlKey(Key):
    
    @property
    def yaml_sig(_):
        msg = '%s\n%s\n' % (_.yaml_public, _.yaml_secret)
        sig = _.sign(msg)
        return '- $S: "'+sig+'"'
    
    @property
    def yaml_public(_):
        return '  +V: "'+_.public+'"'
    
    @property
    def yaml_secret(_):
        return '  -P: "'+_.secret+'"'

    def save(_, filename):
        with open(filename,'w') as fil:
            fil.write(_.yaml_sig+'\n')
            fil.write(_.yaml_public+'\n')
            fil.write(_.yaml_secret+'\n')
            pass
        pass

    @classmethod
    def load(_, filename):
        x = yaml.load(open(filename))[0]
        return _(x['+V'], x.get('-P',''))

    pass # end class YamlKey


class YamlEnvelope(Envelope):

    @property
    def full_msg(_): return _.verify_line+'\n'+_.msg

    def verify(_, key):
        return _.raw_verify(_.full_msg, _.sig, key.public)

    @property
    def sig_line(_):
        return "- $S: " + _.sig
    
    @property
    def verify_line(_):
        return "  +V: " + _.vkey
    
    @classmethod
    def raw_sign(_, msg, secret):
        key = Key.generate(secret)
        _ = _()
        _.vkey = key.public
        _.msg = msg
        _.sig = key.sign(_.full_msg)
        _.verify(key)
        return _

    @classmethod
    def xsign(_, msg, skey):
        return _.raw_sign(msg, skey.secret)

    @property
    def entire_msg(_):
        return '%s\n%s\n%s\n' % (_.sig_line, _.verify_line, _.msg)

    def __str__(_): return _.entire_msg

    def __repr__(_): return repr(str(_))

    pass # end class YamlEnvelope


if __name__=='__main__':
    print("pkcrypt2 " + __version__)
