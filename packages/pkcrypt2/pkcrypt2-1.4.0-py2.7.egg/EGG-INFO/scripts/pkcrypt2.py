#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
"""

Public key encryption utility library, simplified.
Mostly tested with python2.7

- Examples:

    Here are most likely the most common things you want to do
    with this library:

        pkcrypt2.py -g >g # generate a key

        pkcrypt2.py --ykey g -sign     --yenv<makefile | tee makefile.sig # sign a document

        pkcrypt2.py --ykey g -sign --full --yenv<makefile | tee makefile.sig2 # signature + original file

        pkcrypt2.py --ykey g -sign  -r --yenv<makefile # same as above but ripemd160 added on start
        pkcrypt2.py --ykey g -sign -r --full --yenv<makefile

        pkcrypt2.py --ykey g -verify   --yenv<makefile.sig2 # verify aforementioned makefile against g

        pkcrypt2.py          -verify2  --yenv<makefile.sig2 # verify aforementioned makefile

        pkcrypt2.py  -mine makefile.sig2 --skip # this will mine for a RIPEMD160 starting with --prefix

        pkcrypt2.py --ykey g -mine2<makefile # this will mine for a RIPEMD160 starting with --prefix
	
"""
import os, sys, json, time, datetime as dt, traceback as tb, hashlib
from fastecdsa import ecdsa, keys, curve
from fastecdsa.point import Point
from cryptography.fernet import Fernet
from x85 import x85_encode, x85_decode

__version__ = "1.4.0"

def long_encode(n): return x85_encode(bytearray.fromhex('{:064x}'.format(n)))
def long_decode(s): return long(x85_decode(s).encode('hex'), 16)

def _str2vk (x, y): return Point(long_decode(x), long_decode(y), curve.P256)
def _str2sig(r, s): return long_decode(r), long_decode(s)

def str2sk  (st):   return long_decode(st)
def str2vk  (st):   return  _str2vk(*st.split(','))
def str2sig (st):   return _str2sig(*st.split(','))

def sk2str  (sk):   return long_encode(sk)
def vk2str  (vk):   return long_encode(vk.x) +','+long_encode(vk.y)
def sig2str (rs):   return long_encode(rs[0])+','+long_encode(rs[1])


class RipeMD160HashMixin:

    @property
    def hash(_): h = hashlib.new('ripemd160'); h.update(_.freeze); return h

    @property
    def hexdigest(_):     return _.hash.hexdigest()

    def __hash__(_):      return hash(_.hexdigest)

    def __eq__(_, other): return _.hexdigest == other.hexdigest

    def __lt__(_, other): return _.hexdigest <  other.hexdigest

    def __gt__(_, other): return _.hexdigest  > other.hexdigest

    pass # end class RipeMD160Mixin


class SaveLoadFileMixin:

    def save_fname(_, filename): open(filename,'w').write(_.freeze)

    @classmethod
    def load_fname(_, filename): return _.thaw(open(filename).read())

    pass # end class SaveLoadFileMixin


class BaseKey(object):

    def __init__(_, vkey='', skey=''):

        if not vkey:
            vkey, skey = _._gen_pair(skey)
        elif isinstance(vkey, Key):
            if skey: raise TypeError("cannot supply skey with a Key of vkey")
            vkey, skey = vkey.public, vkey.secret
        elif ',' not in vkey:
            vkey, skey = _._gen_pair(vkey)
            pass
        _.vk, _.sk = str2vk(vkey), str2sk(skey) if skey else ''
        pass

    @staticmethod
    def _gen_pair(skey):
        sk = keys.gen_private_key(curve.P256) if not skey else str2sk(skey)
        vk = keys.get_public_key(sk, curve.P256)
        vkey, skey = vk2str(vk), sk2str(sk)
        return vkey, skey            

    def sign(_, msg):
        if not _.sk: raise RuntimeError("Can't sign with no secret")
        return sig2str(ecdsa.sign(msg, _.sk))

    def verify(_, msg, sig, raise_error=True):
        if ecdsa.verify(str2sig(sig), msg, _.vk): return True
        if not raise_error: return False
        raise RuntimeError("Verify Exception")

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

    @property
    def freeze(_):   return _.public+'/'+_.secret+'\n'

    @classmethod
    def thaw(_, s):  return _(*s.strip().split('/', 1))

    pass # end class BaseKey


class Key(BaseKey, SaveLoadFileMixin, RipeMD160HashMixin):

    pass # end class Key


class YamlKey(Key):

    @property
    def full_msg(_):     return _.yaml_public+'\n'+_.yaml_secret+'\n'
    
    @property
    def yaml_sig(_):     return '- $S: "%s"' % _.sign(_.full_msg)
    
    @property
    def yaml_public(_):  return '  $V: "%s"' % _.public
    
    @property
    def yaml_secret(_):  return '  P: "%s"' % _.secret

    @property
    def freeze(_):       return(_.yaml_sig+'\n'+_.full_msg)

    @classmethod
    def thaw(_, str):
        from yaml import load
        x = load(str)[0]
        return _(x['$V'], x.get('P',''))

    pass # end class YamlKey


class BaseEnvelope(object):

    def __init__(_, msg, prefix='', suffix=''):
        _.msg, _.prefix, _.suffix, _.sig = (
            msg, prefix, suffix, '')

    @property
    def full_msg(_): return _.prefix + _.msg + _.suffix

    @classmethod
    def _mk_key(_, secret):
        return secret if isinstance(secret, Key) else Key(secret)

    def verify(_, secret):
        key = _._mk_key(secret)
        return key.verify(_.full_msg, _.sig)

    def sign(_, secret):
        key = _._mk_key(secret)
        _.sig = key.sign(_.full_msg)
        Envelope.verify(_, key)
        return _

    @property
    def sig_line(_):  return _.sig + '\n'

    def __str__(_):   return _.sig

    def __repr__(_):  return _.freeze

    @property
    def freeze(_):    return _.sig_line + _.full_msg

    @classmethod
    def thaw(_, str):
        sig, msg = str.split('\n', 1)
        e = _(msg)
        e.sig = sig
        if e.sig != sig:
            raise RuntimeError("Verify Mismatch")
        return e

    pass # end class BaseEnvelope


class Envelope(BaseEnvelope, SaveLoadFileMixin, RipeMD160HashMixin):

    pass # end class Envelope


class YamlEnvelope(Envelope):

    def __init__(_, msg, *a, **kw):
        if 'suppress_date' in kw:
            del kw['suppress_date']
        else:
            msg = _.mk_date_line() + msg
            pass
        super(YamlEnvelope, _).__init__(msg, *a, suffix='\n', **kw)
        
    def sign(_, secret):
        key = _._mk_key(secret)
        _.vkey = key.public
        _.prefix = _.verify_line
        return super(YamlEnvelope, _).sign(key)

    def verify(_, k=None):
        return super(YamlEnvelope, _).verify(k or Key(_.vkey))

    @property
    def sig_line(_):
        return "- $S: " + _.sig + '\n'
    
    @property
    def verify_line(_):
        return "  $V: " + _.vkey + '\n'

    @classmethod
    def mk_date_line(_):
        return '  Date: %sZ\n' % dt.datetime.now().isoformat()

    @classmethod
    def thaw(_, str):
        sig_line, vfy, msg = str.split('\n', 2)
        sig = sig_line.split()[-1]
        _ = _(msg[:-1], suppress_date=True)
        _.vkey = vfy.split()[-1]
        _.prefix = _.verify_line
        _.sig = sig
        _.verify()
        return _

    pass # end class YamlEnvelope


def decode(key, encoded_text):
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(encoded_text)
    return key, decoded_text


def encode(key, decoded_text):
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(decoded_text)
    return key, encoded_text


def decode_cli():
    key = sys.stdin.readline()
    encoded_text = sys.stdin.read().encode()
    _, decoded_text = decode(key, encoded_text)
    sys.stdout.write(decoded_text.decode())


def encode_cli():
    key = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(key)
    decoded_text = sys.stdin.read().encode()
    key, encoded_text = encode(key, decoded_text)
    print(key.decode())
    print(encoded_text.decode())


def mine_string(inp, prefix='f00f'):
    h0 = hashlib.new('ripemd160'); h0.update(inp)
    for n in xrange(0x10000000, 0xffffffff):
        nce = '%x'%n; h1 = h0.copy(); h1.update(nce); hd = h1.hexdigest()
        if hd.startswith(prefix):
            open('out2', 'w').write(inp + nce)
            open('out1', 'w').write(nce)
            return nce + ' ' + hd
        if (n%0x100000)==0:
            sys.stderr.write('%s %s %s\n' % (nce, hd, prefix))


def mine_file(filename, prefix='f00f', skip_line=True):
    with open(filename) as f:
        if skip_line: f.readline()
        return mine_string(f, read(), prefix)


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='pkcrypt2.py', description='public key cryptography')
    parser.add_argument('--skip',   action='store_true',    help= 'skip first line')
    parser.add_argument('--prefix', dest='prefix', default='000000',help='mining hash prefix')
    parser.add_argument('-mine',    dest='mine',            help='mine')
    parser.add_argument('--okey',   dest='okey',            help= 'old key')
    parser.add_argument('--ykey',   dest='ykey',            help='yaml key')
    parser.add_argument('--oenv',   action='store_true',    help= 'old envelope')
    parser.add_argument('--yenv',   action='store_true',    help='yaml envelope')
    parser.add_argument('--B',      action='store_true',    help='block nonce format')
    parser.add_argument('-r',       action='store_true',    help= 'ripemd160')
    parser.add_argument('--full',   action='store_true',    help='full output')
    parser.add_argument('-sign',    action='store_true',    help='sign a message')
    parser.add_argument('-verify',  action='store_true',    help='verify a message')
    parser.add_argument('-verify2',  action='store_true',    help='verify a message')
    parser.add_argument('-g',       action='store_true',    help='generate old key')
    parser.add_argument('-G',       action='store_true',    help='generate YAML key')
    parser.add_argument('-Y',       action='store_true',    help='print key in YAML format')
    parser.add_argument('-O',       action='store_true',    help='print key in old format')
    parser.add_argument('--version',action='version', version='%(prog)s '+__version__)
    args = parser.parse_args()
    
    def key():
        if args.ykey:
            return YamlKey.thaw(open(args.ykey).read().strip())
        else:
            return     Key.thaw(open(args.okey).read().strip())
    def env_class():
        return YamlEnvelope if args.yenv else Envelope
    def suffix():
        if args.B:      return '\n- Nonce: '
        elif args.yenv: return '\n  ~~Nonce: '
        else:           return '\n'

    if args.mine:
        x = env_class()(open(args.mine).read()).sign(key())
        x.suffix = suffix()
        x.suffix += mine_string(x.full_msg, args.prefix).split()[0]
        x = x.sign(key())
        if args.full:
            sys.stdout.write(repr(x))
        else:
            sys.stdout.write(x.suffix)
    elif args.g:
        sys.stdout.write(YamlKey().freeze)
    elif args.G:
        sys.stdout.write(    Key().freeze+'\n')
    elif args.Y:
        sys.stdout.write(YamlKey(key().secret).freeze)
    elif args.O:
        sys.stdout.write(    Key(key().secret).freeze+'\n')
    elif args.sign:
        x = env_class()(sys.stdin.read()).sign(key())
        if args.r:
            print('- ' + x.hexdigest)
        if args.full:
            sys.stdout.write(repr(x))
        else:
            sys.stdout.write(x.sig_line)
    elif args.verify:
        print(env_class().thaw(sys.stdin.read()).verify(key()))
    elif args.verify2:
        print(env_class().thaw(sys.stdin.read()).verify())
    else:
        print("ARGS", args)


if __name__=='__main__': main()
