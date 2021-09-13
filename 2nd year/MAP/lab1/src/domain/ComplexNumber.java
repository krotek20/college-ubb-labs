package domain;

public class ComplexNumber {

    private Double re, im;

    public ComplexNumber(Double re, Double im) {
        this.re = re;
        this.im = im;
    }

    public Double getRe() {
        return re;
    }

    public Double getIm() {
        return im;
    }

    public void setRe(Double re) {
        this.re = re;
    }

    public void setIm(Double im) {
        this.im = im;
    }

    public ComplexNumber getConjugate() {
        return new ComplexNumber(this.re, -this.im);
    }

    @Override
    public String toString() {
        return this.re.toString() + (this.im < 0 ? "" : "+") + this.im.toString() + "i";
    }

    public static ComplexNumber fromString(String s) {
        String input = s.replace("+", " +").replace("-", " -").trim();

        String[] numbers = input.split(" ");
        if (numbers.length > 2) {
            return null;
        }

        Double real = null, imag = null;
        for (String n : numbers) {
            if (n.endsWith("i")) {
                if (imag != null) return null;
                imag = n.equals("i") ?
                        1.0 : (n.equals("-i") ?
                        -1.0 : Double.parseDouble(n.replace("i", "")));

            } else {
                if (real != null) return null;
                real = Double.parseDouble(n);
            }
        }

        real = real == null ? 0 : real;
        imag = imag == null ? 0 : imag;

        return new ComplexNumber(real, imag);
    }

}