import string

def is_hex(data):
  if type(data) is not str: return False
  if not all(c in string.hexdigits for c in data): return False
  if not len(data)%2==0: return False
  return (data.uper()).replace(" ", "")
