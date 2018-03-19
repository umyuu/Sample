import java.util.Random;
import java.util.StringJoiner;

public class A118044 {
	public static void main(String[] args) {
		int data[] = initialize();
		StringJoiner all = new StringJoiner(" ");
		StringJoiner odds = new StringJoiner(" ", "奇数 : ", "");
		StringJoiner evens = new StringJoiner(" ", "偶数 : ", "");

		for (int number : data) {
			String str = String.valueOf(number);
			all.add(str);
			if ((number & 1) != 0) {
				odds.add(str);
			} else {
				evens.add(str);
			}
		}
		System.out.println(all.toString());
		System.out.println(odds.toString());
		System.out.println(evens.toString());
	}

	public static int[] initialize() {
		Random rnd = new Random();
		// rnd.setSeed(42);
		return rnd.ints(10, 1, 100 + 1).toArray();
	}
}
