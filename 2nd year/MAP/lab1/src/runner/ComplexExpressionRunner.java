package runner;

import domain.ComplexNumber;

public abstract class ComplexExpressionRunner {

    public ComplexExpressionRunner() {
    }

    public abstract ComplexNumber execute(ComplexNumber a, ComplexNumber b);

}
