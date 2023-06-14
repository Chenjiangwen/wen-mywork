package expert;

import expert.Dao.ResultDto;
import expert.Dao.Rule;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Core {

    /**
     * Pre-set database path
     */
    private static final String FILE_PATH = "rules.txt";

    /**
     * Target collection.
     */
    public static Set<String> targetSet;

    /**
     * rule base
     */
    public static List<Rule> rules;

    /**
     * System data initialization.
     */
    public static void init() {
        // creat target collection.
        targetSet = new HashSet<String>() {{
            add("Tiger");
            add("Leopard");
            add("Zebra");
            add("Giraffe");
            add("Ostrich");
            add("Penguin");
        }};

        // To create a rule library
        rules = new ArrayList<>();

        // Read the initialization file
        String encoding = "UTF-8";
        try {
            // Load the file as an input stream
            InputStream inputStream = Core.class.getResourceAsStream(FILE_PATH);

            // Create a buffered reader to read the file
            BufferedReader bufferedReader = null;
            if (inputStream != null) {
                bufferedReader = new BufferedReader(new InputStreamReader(inputStream, encoding));
            }

            // Read each line of the file and add the rule to the rule library
            String line;
            if (bufferedReader != null) {
                while ((line = bufferedReader.readLine()) != null) {
                    String[] arr = line.split("->");
                    // Add the rule to the rule library
                    List<String> p = new ArrayList<>();
                    Collections.addAll(p, arr[0].split("&"));
                    rules.add(new Rule(p, arr[1]));
                }
            }

            // Close the input stream and buffered reader
            if (inputStream != null) {
                inputStream.close();
            }
            if (bufferedReader != null) {
                bufferedReader.close();
            }
        } catch (Exception e) {
            // Print an error message if there was an issue reading the file
            System.err.println("Error reading initialization file content.");
        }
    }

    /**
     * Inference engine.
     *
     * @param dataBase The retrieval criteria entered by the user, i.e. the current database.
     */
    public static ResultDto reason(Set<String> dataBase) {
        ResultDto resultDto = new ResultDto();
        resultDto.setProcess("");

        // Keep track of the number of inferences made
        int count = 0;

        while (true) {
            // Determine if there is new inference available.
            boolean change = false;
            for (Rule rule : rules) {
                // Determine if the database contains all conditions of the current rule
                boolean flag = true;
                for (String condition : rule.getP()) {
                    if (!dataBase.contains(condition)) {
                        flag = false;
                        break;
                    }
                }
                // All conditions of the current rule are met.
                if (flag) {
                    // Add the result of the current rule to the database
                    if (!dataBase.contains(rule.getQ())) {
                        dataBase.add(rule.getQ());
                        change = true;
                        // Print the current rule and result to the console
                        System.out.println(++count + ".Using Rule: " + rule.toString() + ", Result : " + rule.getQ());
                        System.out.println("Current Database: " + dataBase);
                        // Add the current rule and result to the resultDto
                        resultDto.setProcess(resultDto.getProcess() + count + ".Using Rule: " + rule.toString() + ", Result: " + rule.getQ() + "\n");
                        resultDto.setProcess(resultDto.getProcess() + "Current Database: " + dataBase + "\n\n");
                    }
                    // If the inferred result is an element of the target set, the reasoning process ends
                    if (targetSet.contains(rule.getQ())) {
                        resultDto.setResult(rule.getQ());
                        return resultDto;
                    }
                }
            }
            // There are no new inferences available
            if (!change)
                break;
        }
        resultDto.setResult("Unable to recognize specific target animals.");
        return resultDto;
    }
}







