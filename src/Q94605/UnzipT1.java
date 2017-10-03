import java.io.*;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

import net.lingala.zip4j.core.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import java.util.Scanner;

// 外部ライブラリに zip4j_1.3.2.jar を使用
public class UnzipT1 {
	private final String destination = "C:\\unzip"; // 出力先フォルダ
	private char[] password = "pwd".toCharArray(); // 解凍パスワード

	public UnzipT1() {

	}

	public static void main(String args[]) throws IOException {
		System.out.println("対象フォルダを入力してください。");
		try (Scanner in = new Scanner(System.in)) {
			String strIn = in.nextLine();
			
			UnzipT1 unzip = new UnzipT1();
	        Files.walkFileTree(Paths.get(strIn), new SimpleFileVisitor<Path>() {
	            @Override
	            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
	            	unzip.extractAll(file.toFile());
	                return FileVisitResult.CONTINUE;
	            }
	        });
		}
	}

	// unzip
	public boolean extractAll(File f) {
		try {
			ZipFile zipFile = new ZipFile(f);
			System.out.println(f);
			if (!zipFile.isValidZipFile()) {
				return false;
			}
			// 解凍パスワードを割り当て
			if (zipFile.isEncrypted()) {
				zipFile.setPassword(password);
			}
			zipFile.extractAll(destination);

		} catch (ZipException e) {
			//e.printStackTrace();
			return false;
		}
		return true;
	}
}