package factory;

import domain.Operation;
import runner.*;

public class ExpressionFactory {

    private static ExpressionFactory factory;

    private ExpressionFactory() {
    }

    public static ExpressionFactory getFactory() {
        if (factory == null) {
            factory = new ExpressionFactory();
        }
        return factory;
    }

    public ComplexExpressionRunner createExpression(Operation op) {
        return switch (op) {
            case ADD -> new AdditionExpressionRunner();
            case SUB -> new SubstractExpressionRunner();
            case MUL -> new MultiplyExpressionRunner();
            case DIV -> new DivisionExpressionRunner();
        };
    }

}
