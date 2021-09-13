package donation.network.dto;

import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class DTOUtils {
    public static Donation getFromDTO(DonationDTO donDTO){
        return new Donation(donDTO.getCharityId(),donDTO.getDonorId(),donDTO.getSum());
    }

    public static DonationDTO getDTO(Donation d){
        return new DonationDTO(d.getCaseId(),d.getDonorId(),d.getSum());
    }

    public static Volunteer getFromDTO(VolunteerDTO voldto){
        return new Volunteer(voldto.getId(),voldto.getName(),voldto.getUsername(), voldto.getPassword());
    }

    public static VolunteerDTO getDTO(Volunteer vol){
        return new VolunteerDTO(vol.getId(),vol.getName(),vol.getUsername(), vol.getPassword());
    }

    public static Donor getFromDTO(DonorDTO dondto){
        return new Donor(dondto.getId(), dondto.getName(), dondto.getAddress(), dondto.getPhoneNumber());
    }

    public static DonorDTO getDTO(Donor don){
        return new DonorDTO(don.getId(), don.getName(), don.getAddress(), don.getPhoneNumber());
    }

    public static CharityCase getFromDTO(CharityCaseDTO ccdto){
        return new CharityCase(ccdto.getId(), ccdto.getName(),ccdto.getSumRaised());
    }

    public static CharityCaseDTO getDTO(CharityCase cc){
        return new CharityCaseDTO(cc.getId(), cc.getName());
    }

    public static CharityCaseDTO getDTO(CharityCase cc, Long sum){
        return new CharityCaseDTO(cc.getId(), cc.getName(),sum);
    }

    public static DonorDTO[] getDTO(Donor[] d){
        DonorDTO[] ddto=new DonorDTO[d.length];
        for(int i=0;i<d.length;i++)
            ddto[i]=getDTO(d[i]);
        return ddto;
    }

    public static Donor[] getFromDTO(DonorDTO[] ddto){
        Donor[] d=new Donor[ddto.length];
        for(int i=0;i<ddto.length;i++){
            d[i]=getFromDTO(ddto[i]);
        }
        return d;
    }

    public static CharityCaseDTO[] getDTO(CharityCase[] d){
        CharityCaseDTO[] ddto=new CharityCaseDTO[d.length];
        for(int i=0;i<d.length;i++)
            ddto[i]=getDTO(d[i]);
        return ddto;
    }

    public static CharityCaseDTO[] getDTO(CharityCase[] d, Long[] sums){
        CharityCaseDTO[] ddto=new CharityCaseDTO[d.length];
        for(int i=0;i<d.length;i++)
            ddto[i]=getDTO(d[i], sums[i]);
        return ddto;
    }

    public static CharityCase[] getFromDTO(CharityCaseDTO[] ddto){
        CharityCase[] d=new CharityCase[ddto.length];
        for(int i=0;i<ddto.length;i++){
            d[i]=getFromDTO(ddto[i]);
        }
        return d;
    }


}
