import os.path
#
# To DO:  rebuild parsing to make two runs through the file, the first run
#         will create an array of all line numbers where "Building Config" is in
#         that line.  The second pass will set flag to true starting at the last
#         array element.
Repo = input("Enter Repository to store output to:  ")
InputFile = input("Enter filename of tech support dump file:  ")
InputFile = "c:\\configs\\" + InputFile
hostname = ""
print (InputFile)




i = 0            # Building Config line index
idx = 0          # line counter
flag = 2         # start flag
endprep = 2      # end check 1
#------------  Index the last instance of Show Running-Config in the log file -------------
with open(InputFile) as fp:
    for line in fp:
        idx = idx + 1
        #print ('Index = ', idx)
        if (line.find("Building configuration...") >= 0):
            i = idx
            print ('---------------------------------------------')
            print (i)
       
#             break  
       

idx = 0  # reset line counter to 0

#-------------- Output the Start Config -----------------------------------------------------
text_file = open("c:\Output.txt", "w")        
with open(InputFile) as fp:
    for line in fp:
        idx = idx + 1
        if (idx == i):
          flag = 1
        if (line.find("hostname") >= 0 and line.find("hostname") < 45):
            hostname = line[9:]
            hostname = hostname.strip()
           
        if(flag == 1): 
            print (line)
            text_file.write(line)
#         if (line.find("!") >= 0):
#             endprep = 1
        if (flag == 1 and line.find("end") >= 0 and line.find('-') < 0):
            flag = 0
            print (line)
            text_file.write(line)
#         else endprep = 0:
#             print (line)
#             text_file.write(line)
            break 
text_file.close()                     
 
#output = "c:\\version-control\\" + hostname + ".cfg"

#Build output path and filename from user and file input
start_path = 'c:\\version-control\\'
#hostname = hostname[:-1]
hostname = Repo + "\\" + hostname 
hostname = hostname + ".cfg"
final_path = os.path.join(start_path, hostname)
      

       
text_file2 = open(final_path, "w")
with open('c:\output.txt') as fp:
    for line in fp:
        text_file2.write(line)
text_file2.close

DumpFile = input("Press enter to continue  ")     # pause
os.remove("C:\output.txt")         