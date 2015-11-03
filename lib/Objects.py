class HoneyToken():
  def __init__(self, token, action="drop", alert=False, caseInsensitive=False, isBinary=False):
    self.token=token
    self.action=action
    self.alert=alert
    self.isCaseInsensitive=caseInsensitive
    self.isBinary=isBinary

class invalidVariableTypes(Exception):
  pass
