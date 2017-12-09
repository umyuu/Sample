import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.MouseEvent;

import javax.swing.Timer;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.event.MouseInputAdapter;

public class BlockCanvas extends JPanel {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private final Ball ball;
	private final Pad pad;
	private final Image bg_Image = new ImageIcon(getClass().getClassLoader().getResource("resources/blockback.png"))
			.getImage();

	private final Dimension canvas_Size; // �`��̈�̑傫��
	private final Timer paint_Timer;

	public BlockCanvas(int w, int h) {
		canvas_Size = new Dimension(w, h);
		setPreferredSize(canvas_Size);
		ball = new Ball(canvas_Size);
		pad = new Pad(canvas_Size);
		this.addMouseListener(pad);
		final int delay = 50; // milliseconds
		paint_Timer = new Timer(delay, (evt) -> {
			ball.move();
			pad.move(ball);
			repaint();
		});
	}

	public void start() {
		paint_Timer.start();
	}

	public void stop() {
		paint_Timer.stop();
	}

	@Override
	protected void paintComponent(Graphics arg0) {
		super.paintComponent(arg0);
		arg0.drawImage(bg_Image, 0, 0, canvas_Size.width, canvas_Size.height, null);
		ball.draw(arg0);
		pad.draw(arg0);
	}

	public class Ball {
		private final Image ballImage = new ImageIcon(
				getClass().getClassLoader().getResource("resources/smileyball2.png")).getImage();
		int x = 10, y = 100; // �{�[�����S�̍��W
		int vx = 4, vy = 5; // �{�[���̑��x�x�N�g��

		private static final double RADIUS = 0.02; // �{�[���̔��a�̓E�C���h�E��2%

		private final Dimension canvas_size;
		private final int radius; // �{�[���̔��a

		public Ball(Dimension dim) {
			canvas_size = dim;
			radius = (int) (RADIUS * dim.width);
		}

		public void draw(Graphics g) {
			g.drawImage(ballImage, x - radius, y - radius, radius + radius, radius + radius, null);
		}

		public void move() {
			x += vx;
			if (x < radius) {
				x = radius;
				vx = -vx;
			} else if (x > canvas_size.width - radius) {
				// ���܂��͉E�ɓ���������x�������x�̕����𔽓]������
				x = canvas_size.width - radius;
				vx = -vx;
			}
			y += vy;
			if (y < radius) {
				y = radius;
				vy = -vy;
			} else if (y > canvas_size.height - radius) {
				y = canvas_size.height - radius;
				vy = -vy;
			}

		}
	}

	class Pad extends MouseInputAdapter {

		int x = 100, y = 380; // �p�b�h�̒��S���W
		int vx = 0; // �p�b�h�̑��x�x�N�g��
		private static final double WIDTH = 0.25; // �p�b�h���̃E�C���h�E���ɑ΂���䗦
		private static final double HEIGHT = 0.95; // �p�b�h�ʒu��y���W�̃E�C���h�E�����ɑ΂���䗦
		private final Dimension size;// �p�b�h�̕��C����
		private final Dimension canvas_size;

		public Pad(Dimension dim) {
			canvas_size = dim;
			size = new Dimension();
			size.width = (int) (WIDTH * dim.width);
			size.height = size.width / 8;
			y = (int) (HEIGHT * dim.height);
		}

		public void draw(Graphics m_g) {
			m_g.fillRect(x - size.width / 2, y - size.height / 2, size.width, size.height);
		}

		public void move(Ball ball) {
			x += vx; // �p�b�h�̈ړ�
			if (x < size.width / 2) {
				x = size.width / 2;
				vx = -vx;
			} else if (x > canvas_size.width - size.width / 2) {
				// ���܂��͉E�ɓ���������x�������x�̕����𔽓]������
				x = canvas_size.width - size.width / 2;
				vx = -vx;
			} // ���E�̕ǂƂ̏Փ˔�����s���D���������ꍇ�͕ǂɐڂ����ʒu�Ŏ~�߂�D
				// �{�[���Ƃ̏Փ˔���
		}

		@Override
		public void mousePressed(MouseEvent me) {
			final int a = 8;
			if (me.getButton() == MouseEvent.BUTTON1) {// ���{�^���N���b�N?
				vx = -a; // �������Ɉړ�������
			} else {
				vx = a; // �E�����Ɉړ�������
			}
		}

		@Override
		public void mouseReleased(MouseEvent me) {
			vx = 0; // �p�b�h���~�߂�
		}
	}
}