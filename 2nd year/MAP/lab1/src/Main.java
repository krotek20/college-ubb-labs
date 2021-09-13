import domain.ComplexNumber;
import validator.ExpressionParser;
import validator.ExpressionValidator;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("Insert expresion: ");
        Scanner scanner = new Scanner(System.in);
        String expression = scanner.nextLine();
        ComplexNumber result;

        try {
            ExpressionValidator.isValid(expression);
            result = ExpressionParser.computeExpression(expression);
        } catch (IllegalArgumentException | IllegalStateException exception) {
            System.out.println(exception);
            return;
        }

        System.out.println("Result: " + result.toString());
    }

}
