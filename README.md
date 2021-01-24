# Random password generator

Generate a random password with a given length. The algorithm stores the password in a mongodb
database and checks everytime if the generated passwords are uniques.

## Installation

```
pip install -r requirements.txt
```

## Usage

```

a = Mongo()
length = input('Password length: ')
while True:
  password = pass_gen(length)
  if a.search(password):
    a.store(password)
    break
print('Generated password ---> {}'.format(password))

```

Run (example.py)[example.py] to see the above example.