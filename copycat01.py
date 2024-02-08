#!/usr/bin/env python3

#These linesd import the shutil and os
import shutil
import os

#This line calls the forces the program to work from the mycode folder
os.chdir("/home/student/mycode")


#The following statements will copy and backup the sdn_network txt file, and the 5g_research folders
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")