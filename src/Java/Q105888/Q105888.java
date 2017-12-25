import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class ToDo {
	int number;
	final LocalDate localdate;
	final String item;
	int priority;

	ToDo(String item, LocalDate localdate) {
		this.localdate = localdate;
		this.item = item;
		this.priority = 0;
	}

	@Override
	public String toString() {
		return this.localdate.format(DateTimeFormatter.ofPattern("MM月dd日")) + " " + this.item + "優先度:" + this.priority;
	}
}

public class Q105888 {
	public static void main(String[] args) throws IOException {
		// 配列から動的配列(ArrayList)に宣言を変更。
		List<ToDo> ToDoList = new ArrayList<>();
		try (Scanner sc = new Scanner(System.in)) {
			while (true) {
				String str = Prompt(sc, "予定を追加するなら1を入力。予定を月順で表示するなら２、優先度順で表示するなら３を入力。");
				final int num = Integer.parseInt(str);
				switch (num) {
				case 1:
					add_todo(sc, ToDoList);
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

	private static void add_todo(Scanner sc, List<ToDo> ToDoList) {

		int month;
		do {
			String input_month = Prompt(sc, "月を入力して下さい(1〜12)");
			month = Integer.parseInt(input_month);
		} while (!(1 <= month && month <= 12));
		// ↑1〜12以外が入力されたら再入力を求める
		int dayOfMonth;
		do {
			String input_day = Prompt(sc, "日を入力して下さい(1〜31)");
			dayOfMonth = Integer.parseInt(input_day);
		} while (!(1 <= dayOfMonth && dayOfMonth <= 31));
		
		String input_item = Prompt(sc, "予定");
		LocalDate localdate = LocalDate.of(LocalDate.now().getYear(), month, dayOfMonth);
		ToDo todo = new ToDo(input_item, localdate);
		do {
			String input_priority = Prompt(sc, "優先度を入力して下さい(1〜5)");
			todo.priority = Integer.parseInt(input_priority);
		} while (!(1 <= todo.priority && todo.priority <= 5));

		ToDoList.add(todo);
	}

	private static String Prompt(Scanner sc, String msg) {
		System.out.println(msg);
		return sc.nextLine();
	}

	private static void display_month_order(List<ToDo> ToDoList) {
		System.out.println("予定です。(月昇順)");
		ToDoList.sort((a, b) -> {
			return a.localdate.compareTo(b.localdate);
		});
		ToDoList.forEach(t -> System.out.println(t));
	}

	private static void display_priority_order(List<ToDo> ToDoList) {
		System.out.println("予定です。(優先度昇順)");
		ToDoList.sort((a, b) -> {
			return Integer.compare(a.priority, b.priority);
		});
		ToDoList.forEach(t -> System.out.println(t));
	}
}
