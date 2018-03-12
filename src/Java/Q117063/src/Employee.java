import java.util.Objects;

public class Employee {

	private final int employeeNo;
	private final String employeeName;

	public Employee(int employeeNo, String employeeName) {
		this.employeeNo = employeeNo;
		this.employeeName = employeeName;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		// 言語仕様にてinstanceof演算子は値が nullの時はfalseを返す。
		if (!(obj instanceof Employee)) {
			return false;
		}
		Employee other = (Employee) obj;
		if (!Objects.deepEquals(this.employeeNo, other.employeeNo)) {
			return false;
		}
		return Objects.deepEquals(this.employeeName, other.employeeName);
	}

	@Override
	public int hashCode() {
		return Objects.hash(employeeNo, employeeName);
	}
}
