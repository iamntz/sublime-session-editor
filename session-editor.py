import json
import os

the_file = '../Session.sublime_session'

options_file = open( the_file )
json_file    = json.load( options_file, strict = False )
workspaces   = json_file['workspaces']['recent_workspaces']
user_choice  = None

def ask_user():
  clear = lambda: os.system('cls')
  clear()

  title = "Select Workspace you want to delete (X to abort)"
  print( len(title) * "=" )
  print( title )
  print( len(title) * "=" )

  for i in range(0, len( workspaces ) ):
    print( "[%d] %s" % ( i, workspaces[i] ) )

  choice = input()

  if choice == 'x':
    exit()

  return choice


while not user_choice or int( user_choice ) > len( workspaces ):
  user_choice = ask_user()

user_choice = int( user_choice )
del workspaces[user_choice]

write_options = open( the_file, 'w' )
write_options.write( json.dumps( json_file ) )

write_options.close()
options_file.close()