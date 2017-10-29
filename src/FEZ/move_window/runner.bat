@powershell -NoProfile -ExecutionPolicy Unrestricted "$s=[scriptblock]::create((gc \"%~f0\"|?{$_.readcount -gt 1})-join\"`n\");&$s" %*&goto:eof
#####################################################################
#概要
# FEZ Clientのウィンドウ位置を移動するためのツール
#実行には管理者権限が必要
#ref
#◆SetWindowPos
# https://msdn.microsoft.com/ja-jp/library/cc411206.aspx
#
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
function MoveWindow($title) {
    $hWnd = (Get-Process $title).MainWindowHandle
    "  WindowHandle:$hWnd"
    $ret = [Win32]::SetWindowPos($hWnd, -1, 20, 0, 0, 0, $SWP.NOSZIE -bor $SWP.NOZORDER)
    if(!$ret) {
        $LastError = [ComponentModel.Win32Exception][Runtime.InteropServices.Marshal]::GetLastWin32Error()
        "$LastError"
        "Error"
    }else {
        "Success"
    }
}
"window search =>"
#MoveWindow "notepad"
MoveWindow "FEzero_Client"
"Wait 7secs"
Start-Sleep -s 7