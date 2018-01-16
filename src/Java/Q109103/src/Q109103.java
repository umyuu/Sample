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
	private static final boolean isDebugMode = true;
	private static final File EXECUTABLE_PATH = getExecutablePath();// アプリケーションの実行パス

	private static final File getExecutablePath() {
		File f = null;
		try {
			URL location = Q109103.class.getProtectionDomain().getCodeSource().getLocation();
			f = new File(location.toURI().getPath());
		} catch (java.net.URISyntaxException ex) {
			ex.printStackTrace();
		}
		return f;
	}

	public static void main(String[] args) throws Exception {
		try {
			logWrite(EXECUTABLE_PATH);
			// csvデータを読み取り集約化
			Map<String, Long> grouped = readCsvAndgrouped();
			// 集約結果を表示
			grouped.forEach((k, v) -> System.out.println(k + ":" + String.valueOf(v)));
			// ファイルに出力
			write(grouped);
		} catch (IOException ex) {
			ex.printStackTrace();
		}
	}

	public static Map<String, Long> readCsvAndgrouped() throws IOException {
		Path path = Paths.get(EXECUTABLE_PATH.toString(), "data.csv");
		logWrite(path);
		try (BufferedReader br = Files.newBufferedReader(path)) {
			Map<String, Long> grouped = br.lines().skip(1).map((String line) -> {
				String[] arr = line.split(",");
				return new CsvRow(arr[0], arr[1], Long.parseLong(arr[2]));
			}).collect(Collectors.groupingBy(x -> x.getCategory(), Collectors.summingLong(x -> x.getPrice())));
			return grouped;
		}
	}

	public static void write(Map<String, Long> grouped) throws IOException {
		Path path = Paths.get(EXECUTABLE_PATH.toString(), "grouped.csv");
		logWrite(path);
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

	public static void logWrite(Object message) {
		if (!isDebugMode) {
			return;
		}
		System.out.println(message);
	}
}

// csvの1行単位
class CsvRow {
	private final String category;
	private final String subitem;
	private final Long price;
	public CsvRow(String category, String subitem, Long price) {
		this.category = category;
		this.subitem = subitem;
		this.price = price;
	}
	// @Getter
	public String getCategory() {
		return category;
	}
	// @Getter
	public Long getPrice() {
		return price;
	}

	@Override
	public String toString() {
		String[] array = { this.category, this.subitem, String.valueOf(this.price) };
		return String.join(" ", array);
	}
}