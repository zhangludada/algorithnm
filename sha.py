import hashlib
import os.path


class Sha:
	#计算文件的sha值
	def shakey(self,filename):
		"""
	        用于获取文件的md5值
	        :param filename: 文件名
	        :return: MD5码
	        """
		if not os.path.isfile(filename):  # 如果校验md5的文件不是文件，返回空
		    return
		myhash = hashlib.sha256()
		f = open(filename, 'rb')
		while True:
		    b = f.read(8096)
		    if not b:
		        break
		    myhash.update(b)   
		f.close()

		return myhash.hexdigest()
    

	def sha_write(self,source_filename,new_filename):
		with open(new_filename,mode='w',encoding='utf-8') as f:
			f.write(self.shakey(source_filename))
		print('写入完成')

	def sha_check(self,filename1,filename2):
		sha1=self.shakey(filename1)
		sha2=self.shakey(filename2)
		if sha1==sha2:
			print('文件一致')
		else:
			print('文件不同')
		print(sha1)
		print(sha2)


filename=str(input('请输入原文件名'))
filename2=filename+'.md5'
file=Sha()
file.sha_write(filename,filename2)