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

	private final Dimension canvas_Size; // 描画領域の大きさ
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
		int x = 10, y = 100; // ボール中心の座標
		int vx = 4, vy = 5; // ボールの速度ベクトル

		private static final double RADIUS = 0.02; // ボールの半径はウインドウの2%

		private final Dimension canvas_size;
		private final int radius; // ボールの半径

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
				// 左または右に当たったらx方向速度の符号を反転させる
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

		int x = 100, y = 380; // パッドの中心座標
		int vx = 0; // パッドの速度ベクトル
		private static final double WIDTH = 0.25; // パッド幅のウインドウ幅に対する比率
		private static final double HEIGHT = 0.95; // パッド位置のy座標のウインドウ高さに対する比率
		private final Dimension size;// パッドの幅，高さ
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
			x += vx; // パッドの移動
			if (x < size.width / 2) {
				x = size.width / 2;
				vx = -vx;
			} else if (x > canvas_size.width - size.width / 2) {
				// 左または右に当たったらx方向速度の符号を反転させる
				x = canvas_size.width - size.width / 2;
				vx = -vx;
			} // 左右の壁との衝突判定を行う．当たった場合は壁に接した位置で止める．
				// ボールとの衝突判定
		}

		@Override
		public void mousePressed(MouseEvent me) {
			final int a = 8;
			if (me.getButton() == MouseEvent.BUTTON1) {// 左ボタンクリック?
				vx = -a; // 左向きに移動させる
			} else {
				vx = a; // 右向きに移動させる
			}
		}

		@Override
		public void mouseReleased(MouseEvent me) {
			vx = 0; // パッドを止める
		}
	}
}