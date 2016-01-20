import os,getpass

thisdir = os.path.expanduser("~")+os.sep+'.gnupg'
thisusr = os.getenv("USER")
stdname = 'keys.cfg'

class storageinfo(object):
	"""
	This class sets up the storage information that is 
	used by CryptoPickle
	Typical Arguments
		keyuser=<owner of the key>
		home=<where your gnupg keys are>
		fname=<name of the file that will be en/decrypted>
		loc=<where is the file that is going to be en/decrypted>
	"""
	def __init__(self,**kwargs):
		self.kw = kwargs
		self.p = None
		self.u = self.kw.get('keyuser',thisusr)
		self.h = self.kw.get('home',thisdir)
		self.fname = self.kw.get('fname',stdname)
		l = self.kw.get('loc','')
		self.keyloc = l+os.sep if len(l) else l

	def __call__(self,**kwargs):
		info = storageinfo(**kwargs)
		if info.p is None:
			info.p = getpass.getpass()
		return info

	def getcryptname(self):
		tmp = self.fname.split('.')
		return self.keyloc+'.'.join(i for i in tmp[:-1])+'.crypto.'+tmp[-1]
