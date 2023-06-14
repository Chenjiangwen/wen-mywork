package expert.Dao;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

import java.util.List;

/**
 * Record list generic object corresponds to the Rule
 */
public class RuleProperty {
    private final SimpleIntegerProperty id;

    private final SimpleStringProperty condition;

    private final SimpleStringProperty result;

    public RuleProperty(Integer id, List condition, String result) {
        this.id = new SimpleIntegerProperty(id);
        this.condition = new SimpleStringProperty(condition.toString());
        this.result = new SimpleStringProperty(result);
    }

    public Integer getId() {
        return id.get();
    }

    public void setId(Integer id) {
        this.id.set(id);
    }

    public String getCondition() {
        return condition.get();
    }

    public void setCondition(List condition) {
        this.condition.set(condition.toString());
    }

    public String getResult() {
        return result.get();
    }

    public void setResult(String result) {
        this.result.set(result);
    }
}
