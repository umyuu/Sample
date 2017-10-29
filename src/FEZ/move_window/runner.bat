@echo off
powershell -NoProfile -ExecutionPolicy Unrestricted %~dp0%client.ps1
timeout /T 15