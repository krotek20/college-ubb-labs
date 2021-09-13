package runner;

import domain.ComplexNumber;

public class SubstractExpressionRunner extends ComplexExpressionRunner {

    public SubstractExpressionRunner() {
        super();
    }

    @Override
    public ComplexNumber execute(ComplexNumber a, ComplexNumber b) {
        return new ComplexNumber(a.getRe() - b.getRe(), a.getIm() - b.getIm());
    }

}