@echo off
echo ========================================
echo        JARVIS Installation
echo ========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Creating necessary directories...
mkdir model 2>nul

echo.
echo ========================================
echo    Manual Setup Required:
echo ========================================
echo 1. Download Vosk model from:
echo    https://alphacephei.com/vosk/models
echo.
echo 2. Download 'vosk-model-small-en-us-0.15'
echo.
echo 3. Extract to: model\vosk-model-small-en-us-0.15\
echo.
echo 4. Create .env file with your API keys
echo.
echo 5. Run: python main.py
echo ========================================
pause
