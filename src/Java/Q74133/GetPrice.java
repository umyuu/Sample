package answer6;

import java.util.concurrent.BlockingQueue;

public class GetPrice implements Runnable {

    private final BlockingQueue<Integer> queue;

    public GetPrice(BlockingQueue q) {
        queue = q;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int x = queue.take();
                if (x == Integer.MIN_VALUE) {
                    // end-of-stream
                    break;
                }
                consume(x);
            }
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }

    void consume(int x) {
        System.out.println("課税後価格は" + x * 1.08 + "円です。");
    }
}
