This folder is awaiting code to process tipping bucket rainfall data from the ASPA tipping bucket network. 

Raw data should be uploaded into the "Raw_Data" folder



Processing steps:
1) read each file into memory
2) create a 1 minute date sequence starting at file start and ending at file end
3) merge the file and the index
4) consolidate/resample aggrigate (see streamflow sheet) into 15 minute datasets  (double check that the other Wx data is in 15 minute intervals
5) stitch 15 minute files together
6) develop a quick auto QaQc routine
7) name them by key 
8) print out a csv of the data

