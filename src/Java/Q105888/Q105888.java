import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.io.*;

class ToDo {
	int number;
	int month;
	int day;
	String item;
	int priority;

	@Override
	public String toString() {
		return this.month + "月" + this.day + "日 " + this.item + "優先度:" + this.priority;
	}
}

public class Q105888 {
	public static void main(String[] args) throws IOException {
		try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
			//配列から動的配列(ArrayList)に宣言を変更。
			List<ToDo> ToDoList = new ArrayList<>();

			while (true) {
				System.out.println("予定を追加するなら1を入力。予定を月順で表示するなら２、優先度順で表示するなら３を入力。");

				String str = br.readLine();
				int num = Integer.parseInt(str);
				switch (num) {
				case 1:
					ToDo todo = new ToDo();
					do {
						System.out.println("月を入力して下さい(1〜12)");
						String month = br.readLine();
						todo.month = Integer.parseInt(month);
					} while (!(1 <= todo.month && todo.month <= 12));
					// ↑1〜12以外が入力されたら再入力を求める
					
					do {
						System.out.println("日を入力して下さい(1〜31)");
						String day = br.readLine();
						todo.day = Integer.parseInt(day);
					} while (32 <= todo.day);

					System.out.println("予定");
					String item = br.readLine();
					todo.item = item;

					do {
						System.out.println("優先度を入力して下さい(1〜5)");
						String priority = br.readLine();
						todo.priority = Integer.parseInt(priority);
					} while (6 <= todo.priority);
					
					ToDoList.add(todo);
					break;
				case 2:
					display_month_order(ToDoList);
					break;
				case 3:
					display_priority_order(ToDoList);
					break;
				}
			}
		}
	}

	private static void display_month_order(List<ToDo> ToDoList) {
		System.out.println("予定です。(月昇順)");
		ToDoList.sort(new Comparator<ToDo>() {
			@Override
			public int compare(ToDo todo1, ToDo todo2) {
				// 標準ライブラリのInteger.compareを使用すると、compareをシンプルに記述することができます。
				int month = Integer.compare(todo1.month, todo2.month);
				// ガード節による入れ子条件記述の置き換え
				if (month != 0) {
					return month;
				}
				return Integer.compare(todo1.day, todo2.day);
			}
		});
		ToDoList.forEach(t -> System.out.println(t));
	}

	private static void display_priority_order(List<ToDo> ToDoList) {
		System.out.println("予定です。(優先度昇順)");
		ToDoList.sort((a, b) -> a.priority - b.priority);
		ToDoList.forEach(t -> System.out.println(t));
	}
}
