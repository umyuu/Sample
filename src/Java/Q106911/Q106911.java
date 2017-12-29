import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Q106911 extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public Q106911(){
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(600, 480);
		this.getContentPane().add(new MainPanel());
	}
	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> new Q106911().setVisible(true));
	}
}
