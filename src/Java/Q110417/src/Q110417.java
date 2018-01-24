import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Objects;

public class Q110417 {
	private static final File EXECUTABLE_PATH = Objects.requireNonNull(getExecutablePath());// アプリケーションの実行パス

	private static final File getExecutablePath() {
		File f = null;
		try {
			URL location = Q110417.class.getProtectionDomain().getCodeSource().getLocation();
			f = new File(location.toURI().getPath());
		} catch (java.net.URISyntaxException ex) {
			ex.printStackTrace();
		}
		return f;
	}
	public static void main(String[] args) {
		final int lineNumber = 5 - 1;// 行番号から-1を引いて0オリジンに変換
		// テキストのファイルパス
		Path path = Paths.get(EXECUTABLE_PATH.toString(), "sampretext.txt");
		try{
			try (BufferedReader br = Files.newBufferedReader(path)) {
				String line = br.lines().skip(lineNumber).findFirst().orElse(null);
				System.out.println(line);
			}
		}catch(FileNotFoundException e){
			// エラーの場合は出力先はSystem.outではなく System.errに
			System.err.println(e);
		}catch(IOException e){
			System.err.println(e);
		}
	}
}
