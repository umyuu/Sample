import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class Main {
	public static void main(String[] args) {

		final ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
		executor.scheduleAtFixedRate(new Runnable() {
			private final String text = "demo";
			private int number = 1;

			@Override
			public void run() {
				System.out.println(text + " " + String.format("%05d", number) + " " + System.nanoTime());
				number += 1;
				if (number > 10) {
					executor.shutdown();
				}
			}
		}, 1, 1, TimeUnit.SECONDS);

	}
}
