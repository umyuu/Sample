import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.Scanner;

public class Q107070 {

	public static void main(String[] args) throws InstantiationException, IllegalAccessException,
			IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
		try {
			Class<?> c = inputFindClass();
			// コンストラクタを呼び出してインスタンスを生成
			Object obj = c.getDeclaredConstructor().newInstance();
			for (Field fieled : c.getDeclaredFields()) {
				fieled.setAccessible(true);
				String fieldName = fieled.getName();
				Class<?> fieldType = fieled.getType();
				String fieldTypeStr = fieldType.getName();
				System.out.print("Type : " + fieldTypeStr + ", Name : " + fieldName + ", Value : ");
				try {
					Object value = fieled.get(obj);
					System.out.println(value);
				} catch (IllegalArgumentException | IllegalAccessException e) {
					System.err.println(e);
				}
			}
		} catch (ClassNotFoundException e) {
			System.err.println("クラスが見つかりません．");
			System.err.println(e);
		}
	}

	public static Class<?> inputFindClass() throws ClassNotFoundException {
		System.out.println("フィールドとフィールドの値を表示します．");
		System.out.println("検査するクラスを入力してください");
		System.out.print(">");
		try (Scanner sc = new Scanner(System.in)) {
			String className = sc.nextLine();
			return Class.forName(className);
		}
	}
}

class Point {
	double x1, y1, x;
	double y = 2.0;// 値を取得できてるのかの確認値
}