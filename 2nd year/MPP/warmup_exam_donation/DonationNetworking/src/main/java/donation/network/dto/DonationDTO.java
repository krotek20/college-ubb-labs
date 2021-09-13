package donation.network.dto;

import java.io.Serializable;

public class DonationDTO implements Serializable {
    Long charityId;
    Long donorId;
    Long sum;

    public DonationDTO(Long charityId, Long donorId, Long sum) {
        this.charityId = charityId;
        this.donorId = donorId;
        this.sum = sum;
    }

    public Long getCharityId() {
        return charityId;
    }

    public void setCharityId(Long charityId) {
        this.charityId = charityId;
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
}
