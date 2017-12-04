Imports System.Net.Http

Public Class Form1
    '↓Asyncを付けるのをお忘れなく。
    Private Async Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim url As String = "http://www.example.com/"
        Dim result As String = String.Empty
        Try
            result = Await DownloadString(url)
        Catch ex As TaskCanceledException
            ' タイムアウト時の処理
            Console.WriteLine(ex)
            Console.WriteLine("タイムアウト")
        End Try

        Console.WriteLine(result)
    End Sub
    Async Function DownloadString(url As String) As Task(Of String)
        Using client As New HttpClient()
            ' タイムアウト値の設定
            client.Timeout = TimeSpan.FromMilliseconds(10000D)
            Return Await client.GetStringAsync(url)
        End Using
    End Function
End Class
