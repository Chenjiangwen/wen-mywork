package expert.Dao;

/**
 * Return the reasoning process and result
 */
public class ResultDto {
    /**
     * Process
     */
    private String process;

    /**
     * Result
     */
    private String result;

    public String getProcess() {
        return process;
    }

    public void setProcess(String process) {
        this.process = process;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public ResultDto() {}

    @Override
    public String toString() {
        return "ResultDto{" + "process='" + process + '\'' + ", result='" + result + '\'' + '}';
    }
}