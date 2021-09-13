package domain;

public enum Operation {

    ADD("+"), SUB("-"), MUL("*"), DIV("/");

    private final String repr;

    Operation(String repr) {
        this.repr = repr;
    }

    public static Operation fromRepr(String repr) {
        for (Operation operation : Operation.values()) {
            if (operation.repr.equals(repr)) return operation;
        }
        return null;
    }

}
