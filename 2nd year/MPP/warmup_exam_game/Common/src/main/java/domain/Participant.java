package domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@javax.persistence.Entity
@Table(name = "Participanti")
public class Participant extends Entity<Long> implements Serializable {
    private String nume;
    private Double nota1;
    private Double nota2;
    private Double nota3;
    private ParticipantStatus status;
    private Double total;

    public Participant() { }

    public Participant(String nume, Double nota1, Double nota2, Double nota3, ParticipantStatus status) {
        this.nume = nume;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
        this.status = status;
    }

    public void entityUpdated() {
        Double[] note = new Double[]{nota1, nota2, nota3};
        for (Double nota : note) {
            if (null != nota) {
                status = ParticipantStatus.PENDING;
            }
        }
        if (nota1 != null && nota2 != null && nota3 != null) {
            total = nota1 + nota2 + nota3;
            status = ParticipantStatus.COMPLETED;
        }
    }

    @Id
    @GeneratedValue(generator = "identity")
    @GenericGenerator(name = "identity", strategy = "identity")
    @Override
    public Long getId() {
        return super.getId();
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Double getNota1() {
        return nota1;
    }

    public void setNota1(Double nota1) {
        this.nota1 = nota1;
    }

    public Double getNota2() {
        return nota2;
    }

    public void setNota2(Double nota2) {
        this.nota2 = nota2;
    }

    public Double getNota3() {
        return nota3;
    }

    public void setNota3(Double nota3) {
        this.nota3 = nota3;
    }

    public ParticipantStatus getStatus() {
        return status;
    }

    public void setStatus(ParticipantStatus status) {
        this.status = status;
    }

    public Double getTotal() {
        return total;
    }

    public void setTotal(Double total) {
        this.total = total;
    }

//    public void setStatus(String status) {
//        this.status = ParticipantStatus.valueOf(status);
//    }
}
