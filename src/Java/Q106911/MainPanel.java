import javax.swing.JPanel;
import java.awt.CardLayout;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;

public class MainPanel extends JPanel {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	/**
	 * Create the panel.
	 */
	public MainPanel() {
		setLayout(new CardLayout(0, 0));
		JPanel first = new JPanel();
		add(first, "name_23628913398839");
		
		JButton btnNewButton = new JButton("次画面へ");
		btnNewButton.setBounds(48, 116, 101, 25);
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				showPanel("name_23656904932933");
			}
		});
		first.setLayout(null);
		first.add(btnNewButton);
		
		JLabel lblNewLabel = new JLabel("画面１");
		lblNewLabel.setBounds(12, 13, 327, 66);
		first.add(lblNewLabel);
		
		JPanel second = new JPanel();
		add(second, "name_23656904932933");
		second.setLayout(null);
		
		JLabel label = new JLabel("画面２");
		label.setBounds(28, 39, 57, 16);
		second.add(label);
		
		JButton btnNewButton_1 = new JButton("前画面へ");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				showPanel("name_23628913398839");
			}
		});
		btnNewButton_1.setBounds(39, 101, 101, 25);
		second.add(btnNewButton_1);
	}
	public void showPanel(String name){
		CardLayout card = (CardLayout)getLayout();
		card.show(this, name);
	}
}
