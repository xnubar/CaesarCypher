def shift_isvalid(shift):
    try:
          if -25<=int(shift)<=25:
             return True
          return False
    except:
        return False
