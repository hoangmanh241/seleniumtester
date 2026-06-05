@echo off
echo ==================================================
echo   QualityTest Pro - Setup Environment for Windows
echo ==================================================
echo.

:: 1. Kiểm tra Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python chua duoc cai dat. Vui long cai dat Python tai: https://www.python.org/
    pause
    exit /b
)

:: 2. Cài đặt thư viện Python
echo [1/2] Dang cai dat cac thu vien Python (Selenium, Openpyxl)...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Khong the cai dat thu vien. Kiem tra ket noi mang.
    pause
    exit /b
)

:: 3. Thông báo về Chrome
echo.
echo [2/2] Kiem tra trinh duyet Chrome...
echo [LUU Y] Ban can cai dat Google Chrome phien ban moi nhat de Selenium hoat dong.
echo.
echo ==================================================
echo   THIET LAP HOAN TAT!
echo   Ban co the chay cac file test trong thu muc backend.
echo ==================================================
pause
