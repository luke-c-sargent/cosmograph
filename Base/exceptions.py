class Abstract:
  @staticmethod
  def unimplemented(msg="ABSTRACTION: function not implemented", fmts=[]):
    if fmts:
      raise Exception(str(msg+"\n{}").format(*fmts))
    else:
      raise Exception(msg)
