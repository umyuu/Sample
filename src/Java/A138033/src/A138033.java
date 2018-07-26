import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

@SuppressWarnings("serial")
public class A138033 extends Applet {
	enum ShapeType {
		NONE, OVAL, X_MARK
	}

	private ShapeType shapeType = ShapeType.NONE;
	private final Rectangle rect = new Rectangle(30, 30, 300, 300);
	private Point point = new Point();

	@Override
	public void init() {
		addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				if (rect.contains(e.getPoint())) {
					shapeType = ShapeType.OVAL;
				} else {
					shapeType = ShapeType.X_MARK;
				}
				point = e.getPoint();
				repaint();
			}
		});
	}

	@Override
	public void paint(Graphics g) {
		super.paint(g);
		g.drawRect(rect.x, rect.y, rect.width, rect.height);
		
		final int x = (int) point.getX();
		final int y = (int) point.getY();
		if (shapeType == ShapeType.OVAL) {
			g.setColor(Color.red);
			g.drawOval(x - 10, y - 10, 20, 20);
		} else if (shapeType == ShapeType.X_MARK) {
			g.setColor(Color.blue);
			g.drawLine(x - 10, y - 10, x + 10, y + 10);
			g.drawLine(x - 10, y + 10, x + 10, y - 10);
		}
	}
}