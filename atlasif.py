#Created by: Nicolas Munoz
#Date Created: 05/01/2013

class atlasIf(dict):
  def __getitem__(self,key):
    return eval(dict.__getitem__(self,key))

#AtlasIf example
if1=atlasIf({True:"5+3",False:'lol'})
print if1[5+4==9]
