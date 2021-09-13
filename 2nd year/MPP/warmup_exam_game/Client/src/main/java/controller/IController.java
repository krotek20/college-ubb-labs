package controller;

public class IController {
    //static protected IService service = null;
    static protected GeneralController controller;

    /*public void setService(IService service) {
        IController.service = service;
    }*/
    public void setGeneralController(GeneralController controller) {
        IController.controller = controller;
    }
}
