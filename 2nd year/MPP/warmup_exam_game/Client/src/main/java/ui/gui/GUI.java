package ui.gui;

import ui.IUI;

public class GUI implements IUI {

    public GUI() {
    }

    @Override
    public void startUI() {
        StagePuppeteer.startApp();
    }
}
