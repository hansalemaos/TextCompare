# TextCompare
Right click on 2 files (Windows Context Menu) to compare their content


## How to use the precompiled version

If you want to use it without compiling anything, download the zip files and extract them. Click on textcompare.exe - the app will copy itself to "C:\ProgramData\RCTools\textcompare.exe" and create an uninstaller "C:\ProgramData\RCTools\textcompare_uninstall.cmd" - The whole process takes about 30 seconds, you won't see anything (Task Manager only), there is no install screen. (You may need administrator rights to install the app.) After the app has been installed, you can access it via the Windows context menu (clicking on folders/drives)

How to compile the source code
Create an env (I use Anaconda) Install the requirements https://github.com/hansalemaos/fflist/raw/main/requirements.txt

Download the source code https://github.com/hansalemaos/TextCompare/blob/main/textcompare.pyw

Compile it using this script https://github.com/hansalemaos/TextCompare/blob/main/textcomparecomp.py
