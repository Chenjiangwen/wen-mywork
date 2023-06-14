package expert.Dao;

import java.util.List;

/**
 * Rule
 */
public class Rule {
    /**
     * Condition
     */
    private List<String> p;

    /**
     * Result
     */
    private String q;

    public Rule(List<String> p, String q) {
        this.p = p;
        this.q = q;
    }

    public List<String> getP() {
        return p;
    }

    public void setP(List<String> p) {
        this.p = p;
    }

    public String getQ() {
        return q;
    }

    public void setQ(String q) {
        this.q = q;
    }

    @Override
    public String toString() {
        return "Rule{" + "p=" + p + ", q='" + q + '\'' + '}';
    }
}

