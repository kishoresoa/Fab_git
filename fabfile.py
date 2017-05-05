from fabric.api import local

def test():
  local("./manage.py")
def commit():
  local("git add . && git commit -m 'testing 123' ")
def push():
  local("git push origin master")

def deploy():
  print "Executing manage script."
  print "------------------------"
  test()
  print "Commiting git code locally."
  print "---------------------------"
  commit()
  print "Pushing local git repository to Github."
  print "---------------------------------------"
  push()
