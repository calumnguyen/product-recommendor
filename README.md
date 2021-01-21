# SUTYGON RECOMMENDER SYSTEM

### The purpose of SimBetObj
* Generates the similarity matrix between objects read from a JSON file. 
* Argument:   
  - Agrv[0]: the location of the JSON file  
  - Argv[1]: the choice of the user. If user enters 1, they want to find similar object
  to an existing item. If user enters 2, they want to find items close to the descriptive 
  that they will type in later  
  - Argv[3]: the number of relative items user wants to see (to generate top-N)  
  - Argv[4]: Optional. If the user enters 1 for argv[1], then argv[4] is a place holder for 
  the item's ID  
