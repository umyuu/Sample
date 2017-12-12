import java.io.BufferedReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class Q104138 {

	public static void main(String[] args) throws IOException, URISyntaxException {
		final String search_key = "2017-11-30";
		final URL url = Q104138.class.getClassLoader().getResource("resources/indices_I101.csv");

		try (BufferedReader br = Files.newBufferedReader(Paths.get(url.toURI()), Charset.forName("Windows-31j"));
				Stream<String> lines = br.lines()) {
			lines.filter(line -> line.startsWith(search_key)).forEach(line -> {
				System.out.println(line);
			});
		}
	}
}
