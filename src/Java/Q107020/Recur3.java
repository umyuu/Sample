import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Recur3 {
	static void recur3(int n) {
		// 引数としてその値を許容しない時は、実行時エラー(java.lang.ArrayIndexOutOfBoundsException)を発生させるのではなく、任意の例外をthowまたはドキュメント化する。
		if (n <= 0) {
			throw new UnsupportedOperationException(String.valueOf(n));
		}
		// new int[100]で宣言する意味はないです。
		int[] nstk = new int[n];
		int[] sstk = new int[n];
		int ptr = -1;
		int sw = 0;

		while (true) {
			if (n > 0) {
				ptr++;
				nstk[ptr] = n;
				sstk[ptr] = sw;
				if (sw == 0)
					n -= 1;// n = n - 1;
				else if (sw == 1) {
					n -= 2;
					sw = 0;
				}
				continue;
			}
			do {
				n = nstk[ptr];
				sw = sstk[ptr] + 1;
				// 動作確認のために変数ptrと配列の内容をデバックプリント
				System.out.println(Stream.generate(() -> "-").limit(30).collect(Collectors.joining("")));
				System.out.println(ptr);
				System.out.println(Arrays.toString(nstk) + ' ' + Arrays.toString(sstk));
				ptr--;
				if (sw == 2) {
					System.out.println(n);
					if (ptr < 0)
						return;
				}
			} while (sw == 2);
		}
	}

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			System.out.print("整数を入力せよ：");
			int x = Integer.parseInt(sc.nextLine());
			recur3(x);
		}
	}
}
