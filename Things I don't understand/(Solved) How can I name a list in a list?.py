"""
let's say
there is a list in a list.
stockstotrade = [["AAPL","Technology"],["KORU","leveraged"],["NFLX","Technology"],["KO","Consumer"]]
and I want to find a list that has "Techology" and print it
How can I do this?
"""

stockstotrade = [["AAPL","Technology"],["KORU","leveraged"],["NFLX","Technology"],["KO","Consumer"]]

#access to each element in a stockstotrade
for eachstock in stockstotrade:
  
  #access again in that each element 
  for sector in eachstock:
    
    #Find if each element in a nested element has "Technology", if it is true, print the whole list.
    if sector == "Technology":
        print(eachstock)
