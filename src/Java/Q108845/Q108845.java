import static java.util.stream.Collectors.joining;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Q108845 {
	public static void main(String[] args) {

		List<Integer> list = Arrays.stream(new int[] { 0, -1, -2, -3, Integer.MIN_VALUE, Integer.MAX_VALUE, 2, 3 })
				.boxed().collect(Collectors.toList());

		System.out.println(list);
		// ソート
		// Collections.sort(list, getComparator(false)); //NG
		Collections.sort(list, getComparator(true)); // OK

		// ソート結果を表示
		System.out.println(repeat("#", 40));
		System.out.println(list);
	}

	public static String repeat(String str, int times) {
		return Stream.generate(() -> str).limit(times).collect(joining());
	}

	public static Comparator<Integer> getComparator(boolean b) {
		Comparator<Integer> c;
		if (b) {
			c = (n1, n2) -> Integer.compare(n1, n2);
		} else {
			c = (n1, n2) -> n1 - n2;
		}
		return c;
	}
}