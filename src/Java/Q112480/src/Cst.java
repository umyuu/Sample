import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Cst {

	public static void main(String[] args) {
		// 重複を許可しないなら、配列よりSetを使用するのがベター！
		Set<String> exit = Stream.of("exit", "quit").collect(Collectors.toSet());
		// try～with～Resources文を使う！
		try (Scanner sc = new Scanner(System.in)) {
			while (true) {
				String input = sc.nextLine();
				// 終了条件は最初に判定する。
				if (exit.contains(input)) {
					System.out.println(input + "が入力されたので処理を終了します");
					break;
				}
				// 数字に変換。NumberFormatExceptionのチェックもできればすること！
				int n = Integer.valueOf(input);
				if (n < 71) {
					System.out.println(n + "番目のフィボナッチ数は:" + Cst2.fbnt(n));
					System.out.println(n + "番目までのフィボナッチ数列は:" + Cst2.fbn(n));
				} else {
					System.out.println("範囲外です");
				}
			}
		}
	}
}

class Cst2 {
	public static long fbnt(int n) {
		return n;
	}

	public static long fbn(int n) {
		return n;
	}
}
