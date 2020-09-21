#------------------------------------------------------------------------------
#ARGOSTrackingTool.py
#
#Description: Reads in an ARGOS tracking data file and allows the user
#   to view the location of the turtle for a specidfied data entered
#   via user input.
#
#Author: Michael Scott (mks71@duke.edu
#Date: Fall 2020
#------------------------------------------------------------------------------
#Create a variable pointing to the data file
file_name= './data/raw/Sara.txt'

# Create a file object from the file
file_obj = open(file_name, 'r')

#Read content of file into a list
line_list = file_obj.readlines()

#Close the file
file_obj.close()

#Pretend we read one line of data from the file
lineString = line_list[130]

#Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

#Assign variables to specific items in the list
record_id = lineData[0]  #ARGOS tracking record id
obs_date = lineData[2] #Observation date
obs_lc = lineData[4] # Observation location class
obs_lat = lineData[6] # Observation latitude
obs_long = lineData[7] # Observation longitude

#Print the location of Sara
print(f'Record {record_id} indicates Sara was seen at lat:{obs_lat}, long:{obs_long} on {obs_date}')


