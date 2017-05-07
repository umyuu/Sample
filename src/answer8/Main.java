
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
            } catch (InputMismatchException ex) {
                System.out.println("0.1.2.以外は入力しないでください");
            }
        }
        System.out.println(GamePlay.MAX_LOSE_COUNT + "回負けたので終了です");
    }
}

enum Judge {
    Win,
    Lose,
    Draw,
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
    private int winCount = 0;
    private int loseCount = 0;
    private int drawCount = 0;

    <T extends Hand> void determineWinner(T player, T computer) {
        System.out.println("あなたの手は" + player);
        System.out.println("コンピュータは" + computer);
        switch (Hand.judge(player, computer)) {
            case Win:
                System.out.println("勝ち");
                winCount++;
                break;
            case Lose:
                System.out.println("負け");
                loseCount++;
                break;
            case Draw:
                System.out.println("引き分け");
                drawCount++;
                break;
        }
        System.out.println("勝った回数:" + winCount + "/負けた回数:" + loseCount + "/引きわけの回数:" + drawCount + "");
    }

    boolean isGameOver() {
        return loseCount >= MAX_LOSE_COUNT;
    }
}
