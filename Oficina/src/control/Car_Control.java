/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package control;

import BD.BD_Carro;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import model.Carro;

/**
 *
 * @author alunos
 */
public class Car_Control {
    JTextField jTid;
    JTextField jTNome;
    JTextField jTPlaca;
    JTextField jTkms;
    JButton jBSalvarEditar;
    
    JList<String> jListCarro;

    ArrayList<Carro> BDcarro = new ArrayList<>();
    DefaultListModel ListaTelaCarro = new DefaultListModel();
    
    BD_Carro bd = new BD_Carro();
    
    public Car_Control(JTextField jTid, JTextField jTNome, JTextField jTPlaca, JTextField jTkms, JButton jBSalvarEditar, JList<String> jListCarro) {
        this.jTid = jTid;
        this.jTNome = jTNome;
        this.jTPlaca = jTPlaca;
        this.jTkms = jTkms;
        this.jBSalvarEditar = jBSalvarEditar;
        this.jListCarro = jListCarro;
        
        BDcarro= bd.carregarBanco();
        carregarLista();
        novoID();
    }
    
    public void novoID(){
        int tamanhoArray = BDcarro.size();
        jTid.setText((tamanhoArray + 1)+"");
    }
    
    public void salvarCarro(){
    String nId = jTid.getText();
    String nPlaca = jTPlaca.getText();
    String nKm = jTkms.getText();
    boolean verificador = true;
    
    if(campoVazio(nPlaca)){
        JOptionPane.showMessageDialog(null, "O Campo Placa não pode ser vazio");
        verificador = false;
    }
    if(campoVazio(nKm)){
        JOptionPane.showMessageDialog(null, "O Campo Kms não pode ser vazio");
        verificador = false;
    }
    
    if(verificador){
        //SALVAR
        
        Carro novoCarro = new Carro(Integer.parseInt(nId), nPlaca, Integer.parseInt(nKm));
        
        if(jBSalvarEditar.getText().compareToIgnoreCase("Salvar")==0){
            BDcarro.add(novoCarro);
            
        }else{
            int index = 0;
            
            for(Carro carro1 : BDcarro){
                if(carro1.getId() == novoCarro.getId()){
                    break;
                }
                index++;
            }
            
            BDcarro.set(index, novoCarro);
        }
        
        limpar();
        carregarLista();

        bd.salvarBanco(BDcarro);

    }
    }
    
    public boolean campoVazio(String temp){
        return temp.isEmpty();
    }

    public void limpar(){
        jTNome.setText("");
        jTPlaca.setText("");
        jTkms.setText("");
        jBSalvarEditar.setText("Salvar");
        novoID();
                
    }  
    
    public void carregarLista(){
        ListaTelaCarro = new DefaultListModel();
        
        ArrayList<String> ListaTelaAtualizada = new ArrayList<>();

        for(Carro carro1 : BDcarro) {
            ListaTelaAtualizada.add(carro1.getPlaca()+" ("+carro1.getId()+")");
        }
        
        Collections.sort(ListaTelaAtualizada);
        
        ListaTelaCarro.addAll(ListaTelaAtualizada);

        jListCarro.setModel(ListaTelaCarro);
    }

    
    public void editar(){
        String temp = jListCarro.getSelectedValue();
        int indexInicioConsulta = temp.indexOf("(", 2);
        int indexFinalConsulta = temp.indexOf(")", 2);
        
        String res = temp.substring( indexInicioConsulta +1, indexFinalConsulta);
        
        int id = Integer.parseInt(res);
        
        Carro carroEditar = buscar(id);

        jTid.setText(carroEditar.getId()+"");
        jTPlaca.setText(carroEditar.getPlaca()+"");
        jTkms.setText(carroEditar.getKms()+"");
        jBSalvarEditar.setText("Editar");
        
    }
    
    public Carro buscar(int id){
        for(Carro carro1 : BDcarro){
            if(carro1.getId()== id){
                return carro1;
            }
        }
        return null;
    }
}   