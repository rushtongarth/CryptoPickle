
import json,os,gnupg,getpass,cPickle as cpk


class CryptoPickle(object):
	def __init__(self,configinfo):
		self.gpg = gnupg.GPG()
		self.gpg.gnupghome = configinfo.h
		self.c = configinfo

	def fwrite(self,towrite):
		_ftoUse = self.c.getcryptname()
		_js = json.dumps(towrite)
		_encrypted = str(self.gpg.encrypt(_js,self.c.u))
		with open(_ftoUse,'wb') as _f:
			cpk.dump(_encrypted,_f,-1)
		
	def fread(self):
		_ftoUse = self.c.getcryptname()
		with open(_ftoUse,'rb') as _f:
			_cj = cpk.load(_f)
		_decrypted = str(self.gpg.decrypt(_cj))
		return json.loads(_decrypted)

	def getkeys(self):
		return self.fread().keys()
	def keycheck(self,indict):
		keys = self.getkeys()
		return [(i in keys,i) for i in indict.keys()]

	def update(self,direct,changedict):
		_updatelist = self.keycheck(changedict)
		if direct=='add':
			self._push({j:changedict[j] for i,j in _updatelist if not i})
		elif direct=='remove':
			self._pop({j:changedict[j] for i,j in _updatelist if i})
		elif direct=='keyval':
			self._upkey({j:changedict[j] for i,j in _updatelist if i})
		else:
			raise KeyError("Unknown Command: %s"%(direct))

	def _push(self,toadd):
		_dcDict = self.fread()
		_dcDict.update(toadd)
		self.fwrite(_dcDict)
	def _pop(self,torm):
		_dcDict = self.fread()
		_ = map(lambda k: _dcDict.pop(k),torm.keys())
		self.fwrite(_dcDict)
	def _upkey(self,toupdate):
		_dcDict = self.fread()
		_dcDict.update(toupdate)
		self.fwrite(_dcDict)
