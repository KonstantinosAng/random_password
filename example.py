from generate import Mongo, pass_gen


if __name__ == '__main__':
  """ Main loop """
  a = Mongo()
  length = input('Password length: ')
  while True:
    password = pass_gen(length)
    if a.search(password):
      a.store(password)
      break
  print('Generated password ---> {}'.format(password))
