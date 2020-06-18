from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64, hashlib, random
from libs.salt import alphabet

class AESCipher(object):
    def __init__(self):
        """ 
        Static and Ghost Functions 
        """
        self._salt = lambda x: [random.choice(x) for i in range(16)]

    def __main__(self, KEY, SALT=''):
        self.SALT = SALT if SALT else "".join(self._salt(alphabet))
        self.KEY = hashlib.pbkdf2_hmac('sha256', KEY.encode(), self.SALT.encode(), 100000)[:32]

    def __encrypt__(self, RAW):
        _raw = pad(RAW, AES.block_size)
        IV = Random.new().read(AES.block_size)
        Cipher = AES.new(self.KEY, AES.MODE_CBC, IV)

        return base64.b64encode(self.SALT.encode() + base64.b64encode(IV + Cipher.encrypt(_raw)))

    def __decrypt__(self, CPT):
        CPT = base64.b64decode(CPT)
        IV = CPT[:AES.block_size]
        Cipher = AES.new(self.KEY, AES.MODE_CBC, IV)

        return unpad(Cipher.decrypt(CPT[AES.block_size:]), AES.block_size)

# Key
#
# ('DtXGahSmQNT-AE2')
#
