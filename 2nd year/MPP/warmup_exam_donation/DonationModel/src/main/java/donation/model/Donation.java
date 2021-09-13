package donation.model;

import java.io.Serializable;

public class Donation extends Entity<Long> implements Serializable {
    public Long getCaseId() {
        return caseId;
    }

    public void setCaseId(Long caseId) {
        this.caseId = caseId;
    }

    public Long getDonorId() {
        return donorId;
    }

    public void setDonorId(Long donorId) {
        this.donorId = donorId;
    }

    public Long getSum() {
        return sum;
    }

    public void setSum(Long sum) {
        this.sum = sum;
    }

    private Long caseId;
    private Long donorId;
    private Long sum;

    public Donation(Long caseId, Long donorId, Long sum) {
        this.caseId = caseId;
        this.donorId = donorId;
        this.sum = sum;
    }

    public Donation(Long id, Long caseId, Long donorId, Long sum) {
        this.id = id;
        this.caseId = caseId;
        this.donorId = donorId;
        this.sum = sum;
    }
}
