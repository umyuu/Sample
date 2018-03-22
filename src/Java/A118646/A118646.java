import javafx.application.Application;
import javafx.stage.Stage;

import javafx.scene.Scene;
import javafx.scene.control.ToggleButton;
import javafx.scene.layout.VBox;
import javafx.geometry.Pos;

public class A118646 extends Application {

	@Override
	public void start(Stage stage) throws Exception {

		ToggleButton favoriteButton = new ToggleButton("お気に入り");
		VBox layout = new VBox(10);
		layout.setAlignment(Pos.CENTER);
		layout.getChildren().setAll(favoriteButton);
		layout.getStylesheets().add(getClass().getResource("colored-toggle.css").toExternalForm());

		stage.setTitle("JavaFX");
		stage.setResizable(false);
		stage.setScene(new Scene(layout, 400, 300));
		stage.show();
	}

	public static void main(String[] args) {

		launch(args);
	}

}
