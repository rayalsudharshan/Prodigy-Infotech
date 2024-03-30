import win32api
import win32con
import time

def log_key(event):
    if event.wParam == win32con.VK_RETURN:
        print("Enter")
    elif event.wParam == win32con.VK_SPACE:
        print("Space")
    elif event.wParam == win32con.VK_BACK:
        print("Backspace")
    elif event.wParam == win32con.VK_TAB:
        print("Tab")
    elif event.wParam == win32con.VK_ESCAPE:
        print("Escape")
    elif event.wParam == win32con.VK_SHIFT:
        print("Shift")
    elif event.wParam == win32con.VK_CONTROL:
        print("Control")
    elif event.wParam == win32con.VK_MENU:
        print("Alt")
    elif event.wParam == win32con.VK_CAPITAL:
        print("Caps Lock")
    elif event.wParam == win32con.VK_NUMLOCK:
        print("Num Lock")
    elif event.wParam == win32con.VK_SCROLL:
        print("Scroll Lock")
    elif event.wParam == win32con.VK_PRIOR:
        print("Page Up")
    elif event.wParam == win32con.VK_NEXT:
        print("Page Down")
    elif event.wParam == win32con.VK_END:
        print("End")
    elif event.wParam == win32con.VK_HOME:
        print("Home")
    elif event.wParam == win32con.VK_LEFT:
        print("Left arrow")
    elif event.wParam == win32con.VK_UP:
        print("Up arrow")
    elif event.wParam == win32con.VK_RIGHT:
        print("Right arrow")
    elif event.wParam == win32con.VK_DOWN:
        print("Down arrow")
    elif event.wParam == win32con.VK_INSERT:
        print("Insert")
    elif event.wParam == win32con.VK_DELETE:
        print("Delete")
    elif event.wParam == win32con.VK_LWIN:
        print("Left Windows key")
    elif event.wParam == win32con.VK_RWIN:
        print("Right Windows key")
    elif event.wParam == win32con.VK_APPS:
        print("Context menu key")
    elif event.wParam == win32con.VK_SNAPSHOT:
        print("Print Screen")
    elif event.wParam == win32con.VK_OEM_PERIOD:
        print(".")
    elif event.wParam == win32con.VK_OEM_COMMA:
        print(",")
    elif event.wParam == win32con.VK_OEM_MINUS:
        print("-")
    elif event.wParam == win32con.VK_OEM_PLUS:
        print("+")
    elif event.wParam == win32con.VK_OEM_1:
        print(";")
    elif event.wParam == win32con.VK_OEM_2:
        print("/")
    elif event.wParam == win32con.VK
    