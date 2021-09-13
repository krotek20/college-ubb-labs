package validator;

public class ExpressionValidator {

    private static boolean characterValidator(char c) {
        for (char i = '0'; i <= '9'; i++) {
            if (c == i) return true;
        }
        return c == '+' || c == '-' || c == 'i' || c == '.';
    }

    public static void isValid(String expr) {
        String[] splitted = expr.split(" ");
        String currentOp = splitted[1];

        // Operation validator
        for (int i = 3; i < splitted.length; i += 2) {
            if (!currentOp.equals(splitted[i])) {
                throw new IllegalArgumentException("Invalid operation! Please make sure " +
                        "every operation will match the first operation inserted!");
            }
        }
        // Complex number validator
        for (int i = 0; i < splitted.length; i += 2) {
            for (int j = 0; j < splitted[i].length(); j++) {
                if (!characterValidator(splitted[i].charAt(j))) {
                    throw new IllegalArgumentException("Invalid format for complex number!");
                }
            }
        }
    }

}
