
import java.io.File;
import java.net.URL;
import java.nio.file.Paths;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.BoxLayout;

@SuppressWarnings("serial")
public class Q109389 extends JFrame {
	private static final File EXECUTABLE_PATH = getExecutablePath();// アプリケーションの実行パス

	private static final File getExecutablePath() {
		File f = null;
		try {
			URL location = Q109389.class.getProtectionDomain().getCodeSource().getLocation();
			f = new File(location.toURI().getPath());
		} catch (java.net.URISyntaxException ex) {
			ex.printStackTrace();
		}
		return f;
	}
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> {
			Q109389 frame = new Q109389();
			frame.setVisible(true);
		});
	}

	/**
	 * Create the frame.
	 */
	public Q109389() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setBounds(100, 100, 500, 500);
		contentPane = new JPanel();
		setContentPane(contentPane);
		contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.X_AXIS));
		
		JPanel panel = new JPanel();
		contentPane.add(panel);
		panel.setLayout(null);
		
		JButton newButton = new JButton("最初から");
		newButton.setBounds(162, 248, 101, 25);
		panel.add(newButton);
		
		JButton continueButton = new JButton("続きから");
		continueButton.setBounds(162, 319, 101, 25);
		panel.add(continueButton);
		
		JLabel lblNewLabel = new JLabel("");
		lblNewLabel.setBounds(0, 0, 517, 471);
		lblNewLabel.setIcon(new ImageIcon(Paths.get(EXECUTABLE_PATH.toString(), "bg.png").toString()));
		panel.add(lblNewLabel);
	}
}
