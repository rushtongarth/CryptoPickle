import os,getpass

thisdir = os.path.expanduser("~")+os.sep+'.gnupg'
thisusr = os.getenv("USER")
stdname = os.path.join(os.getcwd(),'keys.cfg')

class storageinfo(object):
	"""
	This class sets up the storage information that is 
	used by CryptoPickle
	Typical Arguments
		keyuser=<owner of the key>
		home=<where your gnupg home>
		loc=<full path to file that is going to be en/decrypted>
	"""
	def __init__(self,**kwargs):
		self.u = kwargs.get('keyuser',thisusr)
		self.h = kwargs.get('home',thisdir)
		f = kwargs.get('loc',stdname)
		self.keydir,self.keyfile=os.path.split(f)

	def __call__(self,**kwargs):
		info = storageinfo(**kwargs)
		if not hasattr(info,'p'):
			info.p = getpass.getpass()
		return info

	def getcryptname(self):
		if not 'crypto' in self.keyfile:
			tmp = self.keyfile.rsplit('.',1)
			tmp.insert(1,'crypto')
			self.keyfile = '.'.join(tmp)
		return os.path.join(self.keydir,self.keyfile)
