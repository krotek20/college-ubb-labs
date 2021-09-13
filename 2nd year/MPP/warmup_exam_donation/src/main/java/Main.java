
public class Main {
    public static void main(String[] args) {

        VolunteerDatabaseRepository volunteerRepo = new VolunteerDatabaseRepository();
        Volunteer v = new Volunteer(1L,"nume","user","parola");
        System.out.println("INITIAL");
        for(Volunteer vo : volunteerRepo.FindAll())
            System.out.println(vo.getName()+ " "+ vo.getUsername() + " " +vo.getPassword());
        System.out.println("ADDING ONE");
        volunteerRepo.Add(v);
        for(Volunteer vo : volunteerRepo.FindAll())
            System.out.println(vo.getName()+ " "+ vo.getUsername() + " " +vo.getPassword());
        System.out.println("UPDATING IT");
        volunteerRepo.Update(new Volunteer(1L, "hola" ,"yes", "yesss"));
        for(Volunteer vo : volunteerRepo.FindAll())
            System.out.println(vo.getName()+ " "+ vo.getUsername() + " " +vo.getPassword());
        System.out.println("DELETING IT");
        volunteerRepo.Delete(1L);
        for(Volunteer vo : volunteerRepo.FindAll())
            System.out.println(vo.getName()+ " "+ vo.getUsername() + " " +vo.getPassword());





    }
}
