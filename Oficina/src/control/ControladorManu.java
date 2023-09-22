/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package control;

import BD.BD_Carro;
import BD.BD_Manutencao;
import java.util.ArrayList;
import java.util.Collections;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import model.Carro;
import model.Manutencao;

/**
 *
 * @author alunos
 */
public class ControladorManu {

    JTextField JTid;
    JTextField JTidCarro;
    JTextField JTPlaca;
    JTextField JTkm;
    JTextField JTultimakm;
    JButton JBsalvarRemover;

    JList<String> JListCarro;
    JList<String> JListManu;

    ArrayList<Carro> BDcarros = new ArrayList<>();
    ArrayList<Manutencao> BDmanu = new ArrayList<>();

    DefaultListModel ListaTelaCarro = new DefaultListModel();
    DefaultListModel ListaTelaManu = new DefaultListModel();

    BD_Carro bdCarro = new BD_Carro();
    BD_Manutencao bdManu = new BD_Manutencao();

    public ControladorManu(JTextField JTid, JTextField JTidCarro, JTextField JTPlaca, JTextField JTkm, JTextField JTultimakm, JButton JBsalvarRemover, JList<String> JListCarro, JList<String> JListManu) {
        this.JTid = JTid;
        this.JTidCarro = JTidCarro;
        this.JTPlaca = JTPlaca;
        this.JTkm = JTkm;
        this.JTultimakm = JTultimakm;
        this.JBsalvarRemover = JBsalvarRemover;
        this.JListCarro = JListCarro;
        this.JListManu = JListManu;

        BDcarros = bdCarro.carregarBanco();
        carregarListaCarro();

        BDmanu = bdManu.carregarBanco();

        novoID();
    }

    public void carregarListaCarro() {
        ListaTelaCarro = new DefaultListModel();

        ArrayList<String> ListaTelaAtualizada = new ArrayList<>();

        for (Carro carro1 : BDcarros) {
            ListaTelaAtualizada.add(carro1.getPlaca() + " (" + carro1.getId() + ")");
        }

        Collections.sort(ListaTelaAtualizada);

        ListaTelaCarro.addAll(ListaTelaAtualizada);
        JListCarro.setModel(ListaTelaCarro);
    }

    public void novoID() {
        BDcarros = bdCarro.carregarBanco();

        int tamanhoArray = BDmanu.size();
        JTid.setText((tamanhoArray + 1) + "");
        JTidCarro.setText("");
        JTPlaca.setText((""));
        JTkm.setText("");

        carregarListaCarro();

    }

    public void SelecionarCarro() {
        String temp = JListCarro.getSelectedValue();
        int indexInicioConsulta = temp.indexOf("(", 2);
        int indexFinalConsulta = temp.indexOf(")", 2);

        String res = temp.substring(indexInicioConsulta + 1, indexFinalConsulta);

        int id = Integer.parseInt(res);

        Carro carroSelecionado = buscar(id);

        JTidCarro.setText(carroSelecionado.getId() + "");
        JTPlaca.setText(carroSelecionado.getPlaca() + "");
        JTkm.setText(carroSelecionado.getKms() + "");

    }

    public Carro buscar(int id) {
        for (Carro carro1 : BDcarros) {
            if (carro1.getId() == id) {
                return carro1;
            }
        }
        return null;
    }

    public void salvarManu(){
        String nId = JTid.getText();
        String nIDCarro = JTidCarro.getText();
        
        Carro car = buscar(Integer.parseInt(nIDCarro));

        Manutencao manu = new Manutencao(Integer.parseInt(nId), car.getKms(), car);
        
        BDmanu.add(manu);
                
        bdManu.salvarBanco(BDmanu);
        
        novoID();
        
        
        
        }
    }
