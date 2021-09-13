package runner;

import domain.ComplexNumber;

public class DivisionExpressionRunner extends ComplexExpressionRunner {

    public DivisionExpressionRunner() {
        super();
    }

    @Override
    public ComplexNumber execute(ComplexNumber a, ComplexNumber b) {
        ComplexExpressionRunner complexExpressionRunner = new MultiplyExpressionRunner();
        ComplexNumber numerator = complexExpressionRunner.execute(a, b.getConjugate());
        ComplexNumber denominator = complexExpressionRunner.execute(b, b.getConjugate());
        return new ComplexNumber(
                numerator.getRe() / denominator.getRe(),
                numerator.getIm() / denominator.getRe()
        );
    }

}