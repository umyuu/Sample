
import java.util.EnumMap;
import java.util.Random;
import java.util.Scanner;
import java.util.InputMismatchException;

/**
 *
 * @author umyu
 */
public class Main {

    public static void main(String[] args) {
        GamePlay game = new GamePlay();
        Actor player = new Player();
        Actor computer = new Computer();
        while (!game.isGameOver()) {
            try {
                System.out.println("ジャンケンゲームです！あなたの手を入力してください グー：0 チョキ：1 パー：2");
                System.out.println("コンピュータに" + GamePlay.MAX_LOSE_COUNT + "回負けたら終了です。");
                
                game.determineWinner(player.choice(), computer.choice());
                game.displayResults();
            } catch (InputMismatchException ex) {
                System.out.println("0.1.2.以外は入力しないでください");
            }
        }
        System.out.println(GamePlay.MAX_LOSE_COUNT + "回負けたので終了です");
    }
}

enum Judge {
    Win("勝ち"),
    Lose("負け"),
    Draw("引き分け");
    private final String name;

    Judge(String name) {
        this.name = name;
    }

    String getName() {
        return this.name;
    }
}

enum Hand {
    グー,
    チョキ,
    パー;

    static Hand valueOf(int i) {
        return Hand.values()[i];
    }

    static Judge judge(Hand handA, Hand handB) {
        if (handA.equals(handB)) {
            return Judge.Draw;
        }
        switch (handA) {
            case グー:
                if (handB.equals(Hand.チョキ)) {
                    return Judge.Win;
                }
                break;
            case チョキ:
                if (handB.equals(Hand.パー)) {
                    return Judge.Win;
                }
                break;
            case パー:
                if (handB.equals(Hand.グー)) {
                    return Judge.Win;
                }
                break;
        }
        return Judge.Lose;
    }
}

interface Actor<T extends Hand> {

    T choice();
}

class Player implements Actor {

    @Override
    public Hand choice() {
        Scanner scanner = new Scanner(System.in);
        int hand = scanner.nextInt(3);
        scanner.reset();
        return Hand.valueOf(hand);
    }
}

class Computer implements Actor {

    private final Random random = new Random();

    @Override
    public Hand choice() {
        int hand = random.nextInt(3);
        return Hand.valueOf(hand);
    }
}

class GamePlay {

    public static final int MAX_LOSE_COUNT = 3;
    private final EnumMap<Judge, Integer> counter = new EnumMap<>(Judge.class);

    <T extends Hand> void determineWinner(T player, T computer) {
        System.out.println("あなたの手は" + player);
        System.out.println("コンピュータは" + computer);

        Judge judge = Hand.judge(player, computer);
        counter.put(judge, counter.getOrDefault(judge, 0) + 1);

        System.out.println(judge.getName());
    }

    void displayResults() {
        System.out.print("勝った回数:" + counter.getOrDefault(Judge.Win, 0));
        System.out.print("/負けた回数:" + counter.getOrDefault(Judge.Lose, 0));
        System.out.print("/引きわけの回数:" + counter.getOrDefault(Judge.Draw, 0));
        System.out.println();
    }

    boolean isGameOver() {
        return counter.getOrDefault(Judge.Lose, 0) >= MAX_LOSE_COUNT;
    }
}
