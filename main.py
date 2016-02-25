import player
import room

Master_Rrm = {}
start_rm = Room("start", "foo", [Entity("daquan"), Entity("stev")], ['death', 'acla'])

def main_loop():
  exit = False
  currnt_room = start_rm
  
  while(not(exit)):
    print("room discription:\n")
    print(currnt_room.get_discription() + "\n")
    
    
    
    

