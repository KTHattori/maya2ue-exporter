@echo off
chcp 65001
  
set py=.\resource.py
  
:: Create QRC
echo Create QRC
"C:\Python24\python.exe" .\createQRC.py ./
  
:: Convert QRC to PY
echo Convert QRC to PY
"C:\Program Files\Autodesk\Maya2024\bin\pyside2-rcc.exe" -o %py% .\resource.qrc
 
echo "Done!"
pause