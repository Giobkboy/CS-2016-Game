import player

class Room:
  
  def __init__(self, name, key_wrd, mobs = [], childern):
    
      self.name = name
      self.key_word = key_wrd
    
      if(self.check_mobs(mobs)):
        raise TypeError("use type Entity for mobs")
        quit(-1)
      self.mops = mobs
      self.childern = childern
    
  def check_mobs(self, m):
      if len(mobs) <= 1:
        return True
      for i in mobs:
        if not(type(i) is Entity):
          return False
      return True
      
  def next_room(self, ms_list, key):
    
    is_chlid = False
    for(i in self.childern):
      if(i == key):
        is_chlid = True
        
    if(is_chlid):
      return ms_list[key]
    else:
      return -1
        
