import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class Eaction {

	public static void main(String[] args) {
		Employee employee1 = new Employee(1, "Mr.Yamada");
		Employee employee2 = new Employee(1, "Mr.Yamada");
		Employee employee3 = new Employee(1, null);
		int[] hash_values = { employee1.hashCode(), employee2.hashCode(), employee3.hashCode() };

		System.out.println(Arrays.toString(hash_values));

		Set<Employee> employees = new HashSet<>();
		employees.add(employee1);
		employees.add(employee2);

		System.out.println();
		System.out.println(String.format("size:%d, equals:%b, contains:%b", employees.size(),
				employee1.equals(employee2), employees.contains(employee1)));
	}

}
