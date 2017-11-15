import java.util.ArrayList;
import java.util.List;

import org.opencv.core.*;
import org.opencv.imgcodecs.*;
import org.opencv.imgproc.Imgproc;

public class ImageComparison {
	public static void main(String[] args) {
		System.out.println("èàóùäJén");
		new Demo().run();
		System.out.println("èàóùèIóπ");
	}
}

class Demo {
	static {
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
	}

	public void run() {
		String[] strArray = new String[] { "source/name1.png", "source/name2.png" };
		List<Mat> temp = new ArrayList<Mat>();
		for (String str : strArray) {
			java.io.File f = new java.io.File(str);
			if (!f.exists())
				throw new RuntimeException(f.getAbsolutePath());
			Mat m = Imgcodecs.imread(f.getAbsolutePath(), Imgcodecs.CV_LOAD_IMAGE_GRAYSCALE);
			if (m.empty())
				throw new RuntimeException(f.getAbsolutePath());
			temp.add(m);
		}
		Mat image[] = temp.toArray(new Mat[0]);
		Mat hist1 = new Mat();

		List<Mat> src1 = new ArrayList<Mat>();
		src1.add(image[0]);

		Imgproc.calcHist(src1, new MatOfInt(0), new Mat(), hist1, new MatOfInt(256), new MatOfFloat(0, 64));

		Mat hist2 = new Mat();
		List<Mat> src2 = new ArrayList<Mat>();
		src2.add(image[1]);

		Imgproc.calcHist(src2, new MatOfInt(0), new Mat(), hist2, new MatOfInt(256), new MatOfFloat(0, 64));
		List<Double> histList = new ArrayList<Double>();
		histList.add(Imgproc.compareHist(hist1, hist2, 0));

		Imgcodecs.imwrite("source/test.png", image[0]);
		System.out.println(image[0]);
		System.out.println(image[1]);
		System.out.println(histList);
	}
}