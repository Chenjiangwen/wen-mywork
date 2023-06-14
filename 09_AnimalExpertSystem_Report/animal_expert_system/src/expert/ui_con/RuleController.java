package expert.ui_con;

import expert.Core;
import expert.Dao.Rule;
import expert.Dao.RuleProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;

import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.ResourceBundle;

public class RuleController implements Initializable {

    @FXML
    private TableView<RuleProperty> tableViewComponent;

    @FXML
    private Button addButtonComponent;

    @FXML
    private Button deleteButtonComponent;

    @FXML
    private TableColumn<RuleProperty, Integer> idTableColumnComponent;

    @FXML
    private TableColumn<RuleProperty, String> conditionTableColumnComponent;

    @FXML
    private TableColumn<RuleProperty, String> resultTableColumnComponent;

    @FXML
    private TextField resultTextFieldComponent;

    @FXML
    private TextField conditionTextFieldComponent;

    @FXML
    private TextField idTextFieldComponent;

    @FXML
    private RadioButton isAddToAimsRadioButtonComponent;

    /**
     * Load the initialization.
     */
    public void initialize(URL location, ResourceBundle resources) {
        ObservableList<RuleProperty> data = FXCollections.observableArrayList();
        System.out.println("Number of rules in the rule library: " + Core.rules.size());
        for (int i = 0; i < Core.rules.size(); ++i) {
            data.add(new RuleProperty(i + 1, Core.rules.get(i).getP(), Core.rules.get(i).getQ()));
        }

        conditionTableColumnComponent.setCellValueFactory(new PropertyValueFactory<>("condition"));
        idTableColumnComponent.setCellValueFactory(new PropertyValueFactory<>("id"));
        resultTableColumnComponent.setCellValueFactory(new PropertyValueFactory<>("result"));

        // field data editable
        conditionTableColumnComponent.setCellFactory(TextFieldTableCell.<RuleProperty>forTableColumn());
        resultTableColumnComponent.setCellFactory(TextFieldTableCell.<RuleProperty>forTableColumn());
        // Function triggered when the editing is submitted
        conditionTableColumnComponent.setOnEditCommit(
                (TableColumn.CellEditEvent<RuleProperty, String> t) -> {
                    // change line，first is 0
                    int row = t.getTablePosition().getRow();
                    // Content after modification
                    String newValue = t.getNewValue();
                    System.out.println("Modified the condition on the " + (row + 1) + " line, new content is:" + newValue);
                    List<String> list = new ArrayList<>();
                    Collections.addAll(list, newValue.substring(1, newValue.length() - 1).split(", "));
                    // Update the rule library with the new modification
                    Rule rule = Core.rules.get(row);
                    rule.setP(list);
                    Core.rules.set(row, rule);
                    System.out.println(" the modified condition: " + Core.rules);
                });
        resultTableColumnComponent.setOnEditCommit(
                (TableColumn.CellEditEvent<RuleProperty, String> t) -> {
                    //  change line，first is 0
                    int row = t.getTablePosition().getRow();
                    // Content after modification
                    String newValue = t.getNewValue();
                    System.out.println("Modified the condition on the " + (row + 1) + " line, new content is:" + newValue);
                    // Update the rule library with the new modification
                    Rule rule = Core.rules.get(row);
                    rule.setQ(newValue);
                    Core.rules.set(row, rule);
                    // Update the target value
                    if (Core.targetSet.contains(t.getOldValue())) {
                        Core.targetSet.remove(t.getOldValue());
                        Core.targetSet.add(newValue);
                    }
                    System.out.println("the modified condition: " + Core.rules);
                });


        // Add data visualization
        tableViewComponent.setEditable(true);
        tableViewComponent.setItems(data);
        // Add button event binding.
        addButtonComponent.setOnAction((ActionEvent e) -> {
            String condition = conditionTextFieldComponent.getText();
            String result = resultTextFieldComponent.getText();

            if (condition.equals("")) {
                System.err.println("Adding content cannot be empty.");
                conditionTextFieldComponent.setText("Adding content cannot be empty.");
                return;
            }
            if (result.equals("")) {
                System.err.println("Adding content cannot be empty.");
                resultTextFieldComponent.setText("Adding content cannot be empty.");
                return;
            }

            List<String> p = new ArrayList<>();
            Collections.addAll(p, condition.split("&"));
            // Add to the rule library
            Core.rules.add(new Rule(p, result));
            // Should it be added to the target set
            if (isAddToAimsRadioButtonComponent.isSelected())
                Core.targetSet.add(result);
            System.out.println(Core.targetSet);
            // refresh to the table.
            data.add(new RuleProperty(Core.rules.size(), p, result));
            conditionTextFieldComponent.clear();
            resultTextFieldComponent.clear();
        });

        // Add button event binding
        deleteButtonComponent.setOnAction((ActionEvent e) -> {
            // Get the rule ID of the deleted rule
            if (idTextFieldComponent.getText().equals("")) {
                System.err.println("The ID cannot be empty.");
                idTextFieldComponent.setText("The ID cannot be empty.");
                return;
            }
            int id;
            try {
                id = Integer.parseInt(idTextFieldComponent.getText());
            } catch (NumberFormatException ex) {
                System.err.println("Illegal characters");
                idTextFieldComponent.setText("Illegal characters");
                return;
            }
            if (id > Core.rules.size() || id <= 0) {
                System.err.println("Illegal boundary");
                idTextFieldComponent.setText("Illegal boundary");
                return;
            }
            Core.rules.remove(id - 1);

            // Ensure that refreshing does not interrupt the numbering.
            initialize(location, resources);
            idTextFieldComponent.clear();
        });
    }
}
