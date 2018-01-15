import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class Q109103 {
	private static final File EXECUTABLE_PATH = getExecutablePath();

	private static File getExecutablePath() {
		try {
			URL location = Q109103.class.getProtectionDomain().getCodeSource().getLocation();
			return new File(location.toURI().getPath());
		} catch (Exception ex) {
			ex.printStackTrace();
			return null;
		}
	}

	public static void main(String[] args) throws Exception {
		try {
			System.out.println(EXECUTABLE_PATH);
			// csvデータを読み取り
			Map<String, Long> grouped = readAndgrouped();
			// 集約結果を表示
			grouped.forEach((k, v) -> System.out.println(k + ":" + String.valueOf(v)));
			// ファイルに出力
			write(grouped);
		} catch (IOException ex) {
			ex.printStackTrace();
		}
	}

	public static Map<String, Long> readAndgrouped() throws IOException {
		Path path = Paths.get(EXECUTABLE_PATH.toString(), "data.csv");
		System.out.println(path);
		try (BufferedReader br = Files.newBufferedReader(path)) {
			Map<String, Long> grouped = br.lines().skip(1).map((String line) -> {
				String[] arr = line.split(",");
				return new CsvData(arr[0], arr[1], Long.parseLong(arr[2]));
			}).collect(Collectors.groupingBy(x -> x.category, Collectors.summingLong(x -> x.price)));
			return grouped;
		}
	}

	public static void write(Map<String, Long> grouped) throws IOException {
		Path path = Paths.get(EXECUTABLE_PATH.toString(), "grouped.csv");
		System.out.println(path);
		Charset encoding = Charset.forName("Windows-31j");
		try (BufferedWriter bw = Files.newBufferedWriter(path, encoding)) {
			// ヘッダー行
			bw.write("カテゴリー,総合");
			bw.newLine();
			// データ行
			for (Entry<String, Long> entry : grouped.entrySet()) {
				bw.write(entry.getKey());
				bw.write(":");
				bw.write(String.valueOf(entry.getValue()));
				bw.newLine();
			}
		}
	}
}
// csvの1行単位
class CsvData {
	final String category;
	final String subitem;
	final Long price;

	public CsvData(String category, String subitem, Long price) {
		this.category = category;
		this.subitem = subitem;
		this.price = price;
	}

	@Override
	public String toString() {
		String[] array = { this.category, this.subitem, String.valueOf(this.price) };
		return String.join(" ", array);
	}
}