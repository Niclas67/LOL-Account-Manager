Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c .venv\Scripts\activate && pythonw main.py", 0