package expert.ui_con;

import expert.Core;
import expert.Main;
import expert.Dao.ResultDto;


import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import java.io.IOException;
import java.net.URL;
import java.util.*;

public class IndexController implements Initializable {

    @FXML
    private TextArea userInputComponent;

    @FXML
    private TextField resultComponent;

    @FXML
    private TextArea processComponent;

    public void initialize(URL location, ResourceBundle resources) {

    }

   public void goReason() {
    // Get the user input facts and convert them to a set.
    String[] arr = userInputComponent.getText().split("\n");
    Set<String> dataBase = new HashSet<>(Arrays.asList(arr));

    // Call the reason method to perform inference on the user input facts
    ResultDto resultDto = Core.reason(dataBase);

    // Display the result of the inference on the UI
    resultComponent.setText(resultDto.getResult());
    processComponent.setText(resultDto.getProcess());

    // Print the result to the console
    System.out.println("Result: " + resultDto.getResult());
}

    public void goRuleView() throws IOException {
        // open the rule base
        Parent root = FXMLLoader.load(Objects.requireNonNull(Main.class.getResource("ui/rules.fxml")));
        Stage stage = new Stage();
        stage.setTitle("Animal Recognition Expert System");
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

}
