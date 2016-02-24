import palyer


class Room:
  
  def __init__(self, name, key_wrd, mobs = [], childern):
    
      self.name = name
      self.key_word = key_wrd
    
      if(self.check_mobs(mobs)):
        raise TypeError("use type Entity for mobs")
      self.mops = mobs
    
  def check_mobs(self, m):
      if len(mobs) <= 1:
        return True
      for i in mobs:
        if not(type(i) is Entity):
          return False
      return True
