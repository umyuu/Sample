package answer6;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class ExThread5 {

    public static void main(String[] args) {
        BlockingQueue<Integer> q = new LinkedBlockingQueue<>();
        PutPrice pp = new PutPrice(q);
        GetPrice gp = new GetPrice(q);
        new Thread(pp).start();
        new Thread(gp).start();
    }
}
