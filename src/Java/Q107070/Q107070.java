import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Q107070 {

	public static void main(String[] args) throws InstantiationException, IllegalAccessException,
			IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException {
		try {
			Class<?> c = inputFindClass();
			Constructor<?>[] ctors = c.getDeclaredConstructors();
			Constructor<?> ctor = ctors[0];
			List<Object> params = getParams(ctor.getParameterTypes());
			// コンストラクタを呼び出してインスタンスを生成
			Object obj = ctor.newInstance(params.toArray());
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

	public static List<Object> getParams(Class<?> parameterTypes[])
			throws InstantiationException, IllegalAccessException {
		List<Object> params = new ArrayList<>();
		for (Class<?> p : parameterTypes) {
			if (p.isPrimitive()) {
				if (p.equals(boolean.class)) {
					params.add(false);
					continue;
				}
				if (p.equals(byte.class)) {
					params.add(0);
					continue;
				}
				if (p.equals(short.class)) {
					params.add(0);
					continue;
				}
				if (p.equals(int.class)) {
					params.add(0);
					continue;
				}
				if (p.equals(char.class)) {
					params.add('\u0000');
					continue;
				}
				if (p.equals(float.class)) {
					params.add(0f);
					continue;
				}
				if (p.equals(double.class)) {
					params.add(0d);
					continue;
				}
			}
			params.add(p.newInstance());
		}
		return params;
	}
}

class Point {
	double x1, y1, x;
	double y = 2.0;
}

class Point2 {
	double x1 = 2, y1, x;
	double y = 2.0;

	public Point2(double v) {
		this.x1 = v;
	}
}

class Point3 {
	int x1, y1, x;
	int y = 2;

	public Point3(int v) {
		this.x1 = v;
	}
}

class Point4 {
	String x1 = "aaa", y1, x;
	int y = 2;

	public Point4(String v) {
		this.x1 = v;
	}
}

class Point5 {
	String x = "aaa";
	double y = 2;

	public Point5(String x, double y) {
		this.x = x;
		this.y = y;
	}
}