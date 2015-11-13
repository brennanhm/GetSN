# SCRIPT NAME: GetSN.py
# DESCRIPTION: Download a specified number of SecurityNow (SN) episodes to the current directory
# LAST MODIFIED: Nov 12, 2015
# CHANGELOG:
# Nov 12, 2015	- Wrote introductary message which includes instructions
#		- Downloads now display progress

# TODO
# Change the MP3 metatags for consistency (requires eyeD3 module)

# Import required modules
import urllib 	# urllib.urlretrieve()
import os 	# os.listdir(), os.path.join()
import shutil	# shutil.move()
import eyed3	# eyed3.load()
import sys	# sys.stdout.write() & sys.stdout.flush()

# This function displays the download progress
def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100 / totalSize)
	sys.stdout.write("\r" + remoteFile + "...%d%%" % percent)
	sys.stdout.flush()

# Display introductory message and the instructions
print "#########################################################"
print "This script downloads a specified number of Security Now "
print "episodes to current directory."
print " "
print "Step 1: Enter the number of episodes you wish to download"
print "Step 2: Enter the episode to start downloading from"
print "Step 3: Confirm your selection"
print "Step 4: Wait for downloads to complete"
print "#########################################################"
print " "
print "Press enter to begin."
# raw_input() pauses the screen until the user presses the enter key
raw_input()

# Ask user how many episodes they want and which episode to start from
# Make sure the input can be converted to integers, otherwise throw an error
while True:
	try:
		quantity = int(raw_input("How many episodes would you like to download? "))
		episode = int(raw_input("Starting at which episode? "))
	except ValueError:
		# Invalid input		
		print "Invalid input. Please enter a number."
		continue
	else:
		# Correct input, exit loop.
		break

# Confirm the input received from the user
print " "
print "You asked to download " + str(quantity) + " episodes."
print "Starting from episode " + str(episode)
confirm = "Continue? [y/n] "
answer = raw_input(confirm)
# Make sure we understood the user's answer
while answer not in ['y', 'Y', 'n', 'N']:
	print "Invalid choice. Please answer yes (y/Y) or no (n/N)."
	answer = raw_input(confirm);
print " "

# If the user answers yes, continue with the downloads
if answer == 'y' or answer == 'Y':
	# Download the specified number of episodes from the starting point the user gave us	
	for x in xrange(quantity):
		#Convert episode number to string value
		episodeStr = str(episode + x)
		#Pad the episode with zeros to obey Twit's naming convention
		episodeNo = episodeStr.rjust(4, '0')
		#Concatenate the remote CacheFly URL
		remoteFile = 'http://twit.cachefly.net/audio/sn/sn' + episodeNo + '/sn' + episodeNo + '.mp3'
		#Concatenate the local filename
		localFile = 'SN-' + episodeNo + '.mp3'
		#Print informational messages
		print "Downloading podcast ", remoteFile
		print "Saving to ", localFile
		# Download the file and display progress
		urllib.urlretrieve(remoteFile, localFile, reporthook=dlProgress)
		print " "
		print "Download of ", localFile, " complete."
		print " "
		# Modify MP3 tags
		# audiofile = eyed3.load(localFile) #load the new MP3
		# audiofile.tag.album = u"Security Now" #Change album metatag, using unicode, to "Security Now"
		# audiofile.tag.artist = u"Steve Gibson"
		# audiofile.tag.save()
		# print "MP3 metatags modified."

	print "All downloads complete."
	print "Press enter to exit this script."
	raw_input()

# Otherwse, exit the program
elif answer == 'n' or answer == 'N':
	print "Exiting script..."
# Script shouldn't reach this point due to the validation performed earlier
else:
	print "User input validation error. Check input validation loop."
	raw_input()



### Python notes ###

#For loops -> http://www.learnpython.org/en/Loops
#Convert string to int -> http://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers-in-python
#How to print a backslash -> http://stackoverflow.com/questions/19095796/how-to-print-backslash-with-python
#Validating user input -> http://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#Moving files (see sneekula's post) -> https://www.daniweb.com/software-development/python/threads/176391/how-to-move-files-to-another-directory-in-python
#Combining strings together (concatenation) -> http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
#Downloading files from the web -> http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
#Display an MP3 file's metadata -> eyeD3 song.mp3 -> https://askubuntu.com/questions/226773/how-to-read-mp3-tags-in-shell
#How to pad zeros to a string -> http://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string
#How to write download progress indicator -> # http://stackoverflow.com/questions/51212/how-to-write-a-download-progress-indicator-in-python

