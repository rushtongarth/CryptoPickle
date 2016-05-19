import os,json,gnupg,cPickle as cpk
import getpass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
thisdir = os.path.expanduser("~")+os.sep+'.gnupg'
thisusr = os.getenv("USER")
stdname = 'keys.cfg'

class CryptoPickle(dict):
	defaultGpgHome = os.path.join('~','.gnupg')
	defaultUser = os.getenv('USER')
	defaultDirList = [os.getcwd(),os.getcwd()]
	defaultInfile = 'keys.cfg'
	defaultOutfile = 'keys.crypto.cfg'
	def __init__(self,**kwargs):
		self.gpg = gnupg.GPG()
		self.ci = PKCS1_OAEP.new(RSA.generate(2048))
		self.u = kwargs.get('user',self.defaultUser)
		h = kwargs.get('gpghome',self.defaultGpgHome)
		if not h.startswith('~'):
			self.gpg.gnupghome = h
		else:
			self.gpg.gnupghome = os.path.expanduser(h)
	def __call__(self,pswd=None,**kwargs):
		dirlist = kwargs.pop('inoutdirs',self.defaultDirList)
		if not isinstance(dirlist,list):
			dirlist = [dirlist]
		if len(dirlist)==1:
			indir,outdir=dirlist,dirlist
		elif len(dirlist)==2:
			indir,outdir=dirlist
		else:
			msg = 'Directory listing must be length 1 or 2\n'
			msg +='received argument of length %i'%len(dirlist)
			raise IOError(msg)
		indir,outdir = dirlist
		infile = kwargs.pop('infile',self.defaultInfile)
		outfile= kwargs.pop('outfile',self.defaultOutfile)
		self.infile = os.path.join(indir,infile)
		self.outfile = os.path.join(outdir,outfile)
		self.pswd = self.ci.encrypt(pswd if pswd else getpass.getpass())
		return self
	def __getitem__(self,key):
		try:
			with open(self.infile,'rb') as __f:
				pkl = cpk.load(__f)
				__D = str(self.gpg.decrypt(pkl,passphrase=self.ci.decrypt(self.pswd)))
				return json.loads(__D)[key]
		finally:
			__f.close()

	def __setitem__(self,key,val):
		try:
			
			__e = self.gpg.encrypt(json.dumps({key:val}),self.c.u)
			with open(self.c.getcryptname(),'wb') as __f:
				cpk.dump(str(__e),__f,-1)
		except KeyError as e:
			raise e
		finally:
			__f.close()
