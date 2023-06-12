def rewriteCYCLE(NR_PROFILE__):
      if NR_PROFILE__ >= 100:
         NR_PROFILE = str(NR_PROFILE__)
      elif 10 <=  NR_PROFILE__  <= 99:
         NR_PROFILE = str(0) + str(NR_PROFILE__)
      else:
         NR_PROFILE = '00' + str(NR_PROFILE__)
      return(NR_PROFILE)
