'''Threat Intel Core Module'''
import vt
from filehash import FileHash


'''
Global Variables
'''


sha256hasher = FileHash('sha256')
sha512hasher = FileHash('sha512')

# b27061fcf6a573a3df78e0652cbb4610609d8cfd14aac4846b7ef4ef87eb1c86
class Intel():
    def __init__(self, apikey, client):
        self.apikey = apikey
        self.client = client
        self.client = vt.Client(apikey)
        
        self.md5hasher = FileHash('md5')
        self.sha256hasher = FileHash('sha256')
        self.sha512hasher = FileHash('sha512')
        self.sha1hasher = FileHash('sha1')

    # Takes the file path as an argument and returns with specifed hash
    def calculateHash_file(self, path):
        self.file = path 
        self.hash = sha256hasher.hash_dir(self.file)
        return hash
    def returnInfo(self, sha256):
        self.sha256 = sha256
        sha256 = self.client.get_object(self.file)

    


    


        

        

    

        

        





        



