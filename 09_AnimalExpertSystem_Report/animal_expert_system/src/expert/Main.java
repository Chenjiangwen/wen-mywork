package expert;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.util.Objects;

public class Main extends Application {
    @Override
    public void start(Stage panel) throws Exception {
    // Load the FXML file for the UI
    Parent root = FXMLLoader.load(Objects.requireNonNull(getClass().getResource("ui/index.fxml")));

    // Set the title of the window
    panel.setTitle("Animal Recognition Expert System");

    // Set the scene to display the UI
    panel.setScene(new Scene(root));

    // Disable window resizing
    panel.setResizable(false);

    // Show the window
    panel.show();
}

    public static void main(String[] args) {
//        Load initial rule library
        Core.init();
//        Run interface
        launch(args);
    }
}
