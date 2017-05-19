
if __name__ == "__main__":
  import sys
  import io
  import os

  file = open('pipe.txt','r')
#  for line in fileinput.input(['pipe.txt']):
#    print(line)
  if file:
    while True: 
      line = file.readline()
      if "ON_START_FINISHED" in line:
        print('Started')
        os.spawnlp(os.P_WAIT, 'fbi', 'fbi', '-T','1','-a','-noverbose','pensive.png')

      if "ON_CONVERSATION_TURN_STARTED" in line:
        print('awake')
        os.spawnlp(os.P_WAIT, 'fbi', 'fbi', '-T','1','-a','-noverbose', 'neutral.png')

      if "ON_RESPONDING_STARTED" in line:
        print('Talking')
        os.spawnlp(os.P_WAIT, 'fbi', 'fbi', '-T','1','-a','-noverbose', 'neutral_open.png')

      if "ON_CONVERSATION_TURN_FINISHED" in line:
        print('Done')
        os.spawnlp(os.P_WAIT, 'fbi', 'fbi', '-T','1','-a','-noverbose', 'pensive.png')

      if not line:
        break

