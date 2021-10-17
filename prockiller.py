import ctypes

def main():
    h_user = ctypes.WinDLL("User32.dll")
    h_kernel = ctypes.WinDLL("Kernel32.dll")
    
    winname_inp = input("Input a window to kill: ")
    winname_inp_enc = winname_inp.encode()
    lpClassName = None
    lpWindowName = ctypes.c_char_p(winname_inp_enc)

    hWnd = h_user.FindWindowA(None, lpWindowName)
    
    if hWnd == 0:
        print(f"Failed to find a window named \"{winname_inp}\"")
        print(f"Error code {ctypes.get_last_error()}")
        exit(1)
        
    print(f"Window \"{winname_inp}\" found...")

    lpdwProcessId = ctypes.c_ulong()
    gwtid_check = h_user.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

    if gwtid_check == 0:
        print(f"Failed to get the process ID for \"{winname_inp}\"")
        print(f"Error code {ctypes.get_last_error()}")
        exit(1)

    print(f"PID for \"{winname_inp}\" found ({lpdwProcessId.value})...")

    ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)     # Setting up access rights
    dwDesiredAccess = ALL_ACCESS
    bInheritHandle = False

    hProcess = h_kernel.OpenProcess(dwDesiredAccess, bInheritHandle, lpdwProcessId)

    if hProcess <= 0:
        print(f"Failed to get the process ID for \"{winname_inp}\"")
        print(f"Error code {ctypes.get_last_error()}")
        exit(1)
        
    print(f"Process handle for \"{winname_inp}\" acquired...")

    uExitCode = 0x1

    result = h_kernel.TerminateProcess(hProcess, uExitCode)

    if result == 0:
        print(f"Failed to terminate the process \"{winname_inp}\"")
        print(f"Error code {ctypes.get_last_error()}")
        exit(1)

    print("terminated successfully")
    exit(0)
    
if __name__ == '__main__':
    main()
