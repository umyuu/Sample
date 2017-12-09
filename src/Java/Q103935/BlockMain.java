import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class BlockMain extends JFrame {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private final BlockCanvas bc = new BlockCanvas(500, 500);

	public BlockMain() {
		this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		this.setResizable(false);
		this.setTitle("�u���b�N����?");
		this.setSize(505, 540); // Window �̃T�C�Y���Z�b�g
		this.getContentPane().add(this.bc);
		this.addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosed(WindowEvent e) {
				bc.stop();
			}

			@Override
			public void windowDeiconified(WindowEvent e) {
				bc.start();
			}

			@Override
			public void windowIconified(WindowEvent e) {
				bc.stop();
			}
		});
	}

	public void start() {
		bc.start();
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> {
			BlockMain w = new BlockMain();
			w.setVisible(true); // �\������
			w.start();
		});
	}
}
