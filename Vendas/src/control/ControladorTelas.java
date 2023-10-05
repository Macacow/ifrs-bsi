/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package control;

import java.awt.Dimension;
import javax.swing.JDesktopPane;
import view.TelaCliente;

/**
 *
 * @author alunos
 */
public class ControladorTelas {
    JDesktopPane desktopPane;
    
    public ControladorTelas(JDesktopPane desktopPane) {
        this.desktopPane = desktopPane;
    }
    
    public void telaCliente() {
        desktopPane.removeAll();
        desktopPane.updateUI();
        Dimension resolucao = desktopPane.getSize();
        TelaCliente tela = new TelaCliente();
        tela.setSize(resolucao);
        tela.setLocation(0, 0);
        desktopPane.add(tela);
        tela.setVisible(true);
    }
    
    public void inicio() {
        desktopPane.removeAll();
        desktopPane.updateUI();
    }
}
