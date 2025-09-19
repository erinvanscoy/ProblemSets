# Problem Set One 
#### Erin Vanscoy

### Question 1a)
* The command I would use to list the files in the current directory while sorting it in reverse order of when they were last edited is `ls -rt`. This command is organizing all files in the current directory in reverse order by time.

### Question 1b)
* To expand on this command and provide the date and time the file was last edited I would add `l`, the new command would follow as such `ls -lrt`. This now changes the command so that the list of files in the current directory will appear reversed by time modified, but the date and time are listed. 

### Question 1c)
* The manual description of the `(-l)`, long format command is below. 
    >> When printing in the long (-l) format, display complete time information
             for the file, including month, day, hour, minute, second, and year.  The
             -D option gives even more control over the output format.  This option is
             not defined in IEEE Std 1003.1-2008 (“POSIX.1”).

### Question 2)
* The three commands that can be used to naviage from the direction `/users/erinvanscoy/documents/` to my home directory are listed below. 
    1. `cd ~/` This command brings the user directly to your home directory.
    2. `cd ../` This command brings the user up a directory, which in this case would bring the user from documents back into erinvanscoy (which is the home directory).
    3. `cd /users/erinvanscoy` This command brings the user back to the root directory and then into users, and then back into the home directory.

### Question 3)
* Commands to do the following are listed below: 
    1. `mkdir data` This command is used to make a new directory. The code `mkdir` is telling the terminal to make a new directory. Following this command, the user must name the directory. 
    2. `touch subj01.txt` This command is used to make a new file. The code `touch` is telling the terminal to make a new file. Following this command, the user must name the file. 
    3. `cp subj01.txt subj02.txt subj05.txt subj11.txt` This command is used to copy an exisiting file. The code `cp` is telling the terminal to copy an exisiting file and make a new file. Following this command the user must implement which exisiting file they want copied and then list new file names (depending on how many copies they need).  
    4. `mv subj01.txt subj02.txt subj05.txt subj11.txt ~/ data` The command is used to move exsiting files into a different directory or folder. The code `mv` is telling the terminal to move exisiting files to a new location. Following this command the user must list all the files they want moved. This command ends with the user specifying where they want to move the files (in this case in the new data folder).
    5. `rm subj01.txt subj02.txt subj05.txt` The command is used to remove exisiting files. The code `rm` is telling the terminal to permenantly remove a file. Following this command the user needs to implement which files they want removed (in this case, every file we made except for subject 11).
    
### Question 4)
* The command I used to implement the `tee` code with a pipe symbol was `echo "Hello" | tee greetings.txt`. This command was used to write text inside an exisiting file. The `echo "Hello"` command is telling the terminal to prepare input, that being the word hello. Following this commend is a pipe character, which was used to direct the command to the tee command. Following the pipe is the  `tee greetings.txt`  command, the tee command takes the information from the pipe and then prints out the written input in the terminal, as well as in the specified file. 

### Question 5) 
* `cd ClassFiles | history > history.txtmain` This is the code used inside the main terminal. This is directing the terminal into the ClassFiles folder and then directing it to create a reccord of previously executed commands in a new file names history.txtmain.
* `cd ClassFiles | history > history.txtscreen` This is the code used when inside the screen. This is directing the terminal into the ClassFiles folder and then directing it to create a reccord of previously executed commands in a new file names history.txtscreen. 
* When examining both files, it becomes clear that they are not the same. The history file established in the screen terminal had included all previously executed commands, that being from both when the user is in the main terminal and using the screen. However, the main terminal history account only consisted of executed commands that occured inside the main terminal.

### Question 6)
! [App Screenshot] (GithubIntroTSC.png) 

### Question 7)
! [App Screenshot] (ForkedSC.png)

### Question 8)
! [App Screenshot] (FinishedCommitSC.png)  
