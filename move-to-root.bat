@echo off
REM Batch script to move contents from Gau folder to repository root
REM Run this script from e:\Site1 directory

echo ============================================
echo Moving files from Gau to repository root
echo ============================================
echo.

REM Check if we're in the right directory
if not exist "Gau" (
    echo ERROR: Gau folder not found!
    echo Please run this script from e:\Site1 directory
    echo.
    pause
    exit /b 1
)

echo Moving files...
echo.

REM Move all files and folders from Gau to current directory
for /d %%D in (Gau\*) do (
    echo Moving folder: %%~nxD
    move "%%D" . >nul 2>&1
)

for %%F in (Gau\*.*) do (
    echo Moving file: %%~nxF
    move "%%F" . >nul 2>&1
)

REM Move hidden files
for %%F in (Gau\.*) do (
    echo Moving hidden file: %%~nxF
    move "%%F" . >nul 2>&1
)

echo.
echo Checking if Gau folder is empty...

dir /a /b Gau >nul 2>&1
if errorlevel 1 (
    echo Gau folder is empty, removing...
    rmdir Gau
    echo.
    echo SUCCESS: All files moved and Gau folder removed!
) else (
    echo WARNING: Gau folder still contains some files
    echo Please check manually: dir Gau
)

echo.
echo ============================================
echo Next steps:
echo ============================================
echo 1. Review the moved files
echo 2. Run: git add .
echo 3. Run: git commit -m "Restructure: move project to repository root"
echo 4. Run: git push origin main
echo.
pause
