import java.util.Random;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Q107092 extends JFrame {
	private static final long serialVersionUID = 1L;

	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> {new Q107092().setVisible(true);});
	}
	private final JButton bt = new JButton("●");
	private final Random rnd = new java.util.Random();
	public Q107092() {
		// 画面が閉じられなくなることを防ぐため、setDefaultCloseOperationは一番最初に設定。
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(700, 600);
		setLayout(null);
		bt.addActionListener((e) -> {
			moveTo();
			//コンポーネントの再配置のみならrepaintよりrevalidate
			revalidate();
		});
		moveTo();
		add(bt);
	}
	private void moveTo(){
		int x = rnd.nextInt(650);
		int y = rnd.nextInt(550);
		// ボタンのサイズを5➾50に変更
		bt.setBounds(x, y, 50, 50);
	}
}
