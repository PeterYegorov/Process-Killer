# Process-Killer

Process killer using Windows API

'''
For studying purposes only
'''

A program asks for a window name input. Then it uses:
1) FindWindowA - to grab a base handle to the window
2) GetWindowThreadProcessId - to grab the PID
3) OpenProcess - to grab an open handle
4) TerminateProcess - to kill the process
