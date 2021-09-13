package runner;

import domain.ComplexNumber;

public class MultiplyExpressionRunner extends ComplexExpressionRunner {

    public MultiplyExpressionRunner() {
        super();
    }

    @Override
    public ComplexNumber execute(ComplexNumber a, ComplexNumber b) {
        return new ComplexNumber(
                a.getRe() * b.getRe() - a.getIm() * b.getIm(),
                a.getRe() * b.getIm() + a.getIm() * b.getRe()
        );
    }

}
