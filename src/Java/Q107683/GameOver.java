import javax.swing.JPanel;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.Color;

@SuppressWarnings("serial")
public class GameOver extends JPanel {

	/**
	 * Create the panel.
	 */
	public GameOver() {
		//背景を黄色にする。
		setBackground(Color.YELLOW);
		setLayout(new BorderLayout(0, 0));
		// drawStringはコンポーネントの領域を計算する必要があるので、文字列を表示するだけならJLabelの方がいいです。
		JLabel lblGameOver = new JLabel("GameOver");
		// 文字色を赤色にする。
		lblGameOver.setForeground(Color.RED);
		lblGameOver.setVerticalAlignment(SwingConstants.TOP);
		lblGameOver.setHorizontalAlignment(SwingConstants.CENTER);
		add(lblGameOver, BorderLayout.NORTH);
		
		JLabel lblScore = new JLabel("Score");
		lblScore.setForeground(Color.RED);
		lblScore.setHorizontalAlignment(SwingConstants.CENTER);
		add(lblScore);

	}

}
