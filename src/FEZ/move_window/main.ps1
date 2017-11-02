#####################################################################
#概要
# FEZ Clientのウィンドウ位置を移動するためのツール
#実行には管理者権限が必要
#use setting.json
#
#Reference
#◆SetWindowPos
# https://msdn.microsoft.com/ja-jp/library/cc411206.aspx
#◆Make it easier to wrap powershell scripts in batch files
# https://connect.microsoft.com/PowerShell/feedback/details/724524/make-it-easier-to-wrap-powershell-scripts-in-batch-files
#####################################################################
Add-Type @"
  using System;
  using System.Runtime.InteropServices;
  
  public class Win32 {
    [DllImport("user32.dll", SetLastError=true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    public static extern bool SetWindowPos(IntPtr hWnd, IntPtr hWndInsertAfter, int X, int Y, int cx, int cy, uint uFlags);
  }
  
"@

# SetWindowPos uFlags
$SWP = @{
    NOSZIE   = 1
    NOZORDER = 4
}
function MoveWindow($title, $x, $y) {
    $hWnd = (Get-Process $title).MainWindowHandle
    Write-Host "  WindowHandle:$hWnd"
    $ret = [Win32]::SetWindowPos($hWnd, -1, $x, $y, 0, 0, $SWP.NOSZIE -bor $SWP.NOZORDER)
    if(!$ret) {
        $LastError = [ComponentModel.Win32Exception][Runtime.InteropServices.Marshal]::GetLastWin32Error()
        Write-Host "$LastError"
        Write-Host "Error"
    }else {
        Write-Host "Success"
    }
}
Write-Host ""
# read json file.
$config = Get-Content (Join-Path $PSScriptRoot "setting.json") | ConvertFrom-Json
Write-Host $config
Write-Host "window search =>"
MoveWindow $config.WINDOW.TITLE $config.WINDOW.X $config.WINDOW.Y
Write-Host "Wait 7secs"
Start-Sleep -s 7