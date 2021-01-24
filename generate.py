import random
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
from string import digits as numbers
from string import punctuation as punctuation
import pymongo


class Mongo:
  
  def __init__(self):
    """ Connection to the database """
    self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")

  def store(self, password):
    """ Store passwords in database named unique_passwords and in a collection called passwords """
    mydb = self.myclient["unique_passwords"]
    x = mydb["passwords"].insert_one({ "pass": password })
    if x.inserted_id:
      return True
    return False

  def search(self, password):
    """ Search if generated password is unique in order to store it """
    mydb = self.myclient["unique_passwords"]
    for p in mydb["passwords"].find():
      if password == p['pass']:
        return False
    return True

def pass_gen(length):
  """ generate password based on given length """
  if not length.isdigit(): return 'invalid length input'
  return ''.join(_ for _ in random.sample(''.join(c for c in (lower + upper + numbers + punctuation)), int(length)))

if __name__ == "__main__":
  """ Main loop """
  a = Mongo()
  length = input('Password length: ')
  while True:
    password = pass_gen(length)
    if a.search(password):
      a.store(password)
      break
  print('Generated password ---> {}'.format(password))
