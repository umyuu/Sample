import java.awt.CardLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.Timer;

@SuppressWarnings("serial")
public class Q107683 extends JFrame {

	private Timer countdown_timer;// 変数名をtimerから変更
	private int countdown_sec = 5;// 変数名をsecから変更
	private CardLayout card = new CardLayout(0, 0);

	public static void main(String[] args) {
		// 画面の生成はSwingUtilities.invokeLaterを使用してスレッドセーフにしてくださいな。
		SwingUtilities.invokeLater(() -> {
			Q107683 frame = new Q107683();
			frame.setBounds(10, 10, 800, 800);
			frame.setVisible(true);
		});
	}

	Q107683() {
		// setDefaultCloseOperationは一番先頭で
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setTitle("タイトル画面");
		setLayout(card);
		JPanel labelPanel = new JPanel();
		JLabel label = new JLabel();
		labelPanel.add(label);
		add(labelPanel, "title_window");
		countdown_timer = new Timer(1000, (e) -> {
			label.setText(String.valueOf(countdown_sec));
			if (countdown_sec == -1) {
				countdown_timer.stop();
				showPanel("gameover_window");
				return;
			}
			countdown_sec--;
		});
		JPanel game_over = new GameOver();
		// showPanelの引数の文字列とaddで渡す文字列は一致させてください。
		add(game_over, "gameover_window");

		countdown_timer.start();
	}

	public void showPanel(String name) {
		card.show(getContentPane(), name);
	}

}
