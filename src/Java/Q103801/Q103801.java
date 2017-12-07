import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class Q103801 {

	public static void main(String[] args) {
		Map<String, Integer> map = new LinkedHashMap<>();
		try(Scanner sc = new Scanner(System.in)){
			String[] line = sc.nextLine().split(" ");
			for (String str:line){
				map.merge(str, 1, (oldValue, value) -> {
	                return oldValue + 1;
	            });
			}
			// •\Ž¦
			map.forEach((key, value) -> System.out.println(key + " " + value));
		}
	}
}