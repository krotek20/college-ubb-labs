package validator;

import domain.ComplexNumber;
import domain.Operation;
import factory.ExpressionFactory;
import runner.ComplexExpressionRunner;

public class ExpressionParser {

    private static final ExpressionFactory expressionFactory = ExpressionFactory.getFactory();

    // a => first complex number parsed from input
    // b => every complex number parsed after the first one
    // Every single operation will compress in a (returning value)
    public static ComplexNumber computeExpression(String expr) {
        String[] splitted = expr.split(" ");
        ComplexNumber a = ComplexNumber.fromString(splitted[0]);
        ComplexExpressionRunner runner = expressionFactory.createExpression(Operation.fromRepr(splitted[1]));

        for (int i = 2; i < splitted.length; i += 2) {
            ComplexNumber b = ComplexNumber.fromString(splitted[i]);
            a = runner.execute(a, b);
        }

        return a;
    }

}
