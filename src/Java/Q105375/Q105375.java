import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Q105375 {

	public static void main(String[] args) {
        String n1 = "テスト県";
        String n2 = "テスト区テスト　テスト丁目テスト番テスト号　テスト101";
        String n3 = "テストユーザー";
		System.out.println(Arrays.toString(fixedLength(n1)));
		System.out.println(Arrays.toString(fixedLength(n2)));
		System.out.println(Arrays.toString(fixedLength(n3)));
	}

	public static String[] fixedLength(String str) {
		final Matcher m = Pattern.compile(".{1,15}").matcher(str);
		List<String> result = new ArrayList<>();
		while (m.find()) {
			result.add(str.substring(m.start(), m.end()));
		}
		return result.toArray(new String[0]);
	}

}
