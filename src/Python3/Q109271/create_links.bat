REM シンボリックリンクの作成は管理者権限で実行する必要があります。
SET PARENT_DIR=
SET TARGET_DIR=
mklink /D "%PARENT_DIR%\src\img\0" %TARGET_DIR%
mklink /D "%PARENT_DIR%\src\img\1" %TARGET_DIR%
mklink /D "%PARENT_DIR%\src\img\2" %TARGET_DIR%
mklink /D "%PARENT_DIR%\src\img\3" %TARGET_DIR%
timeout /t 20