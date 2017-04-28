package answer6;

import static java.lang.Thread.sleep;
import java.util.Random;
import java.util.concurrent.BlockingQueue;

public class PutPrice implements Runnable {

    private final BlockingQueue<Integer> queue;
    private final int[] price = {100, 200, 300, 400, 500};

    public PutPrice(BlockingQueue q) {
        queue = q;
    }

    @Override
    public void run() {
        Random rnd = new Random();
        for (int x : price) {
            try {
                queue.put(x);
                sleep(rnd.nextInt(500));
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        // end-of-stream
        shutdown();
    }

    void shutdown() {
        try {
            queue.put(Integer.MIN_VALUE);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
