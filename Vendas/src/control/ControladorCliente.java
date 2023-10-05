/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package control;

import BancoDados.BancoDadosCliente;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Collections;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import model.Cliente;

/**
 *
 * @author alunos
 */
public class ControladorCliente {
    JTextField jTextfieldID;
    JTextField jTextFieldNome;
    JList<String> jListClientes;
    JButton jButtonSalvarEditar;
    
    ArrayList<Cliente> BancoDadosClientes = new ArrayList<>();
    
    DefaultListModel listaTelaCliente = new DefaultListModel();
    
    BancoDadosCliente bancoCliente = new BancoDadosCliente();

    public ControladorCliente(JTextField jTextfieldID, JTextField jTextFieldNome, JList<String> jListClientes, JButton jButtonSalvarEditar) {
        this.jTextfieldID = jTextfieldID;
        this.jTextFieldNome = jTextFieldNome;
        this.jListClientes = jListClientes;
        this.jButtonSalvarEditar = jButtonSalvarEditar;
        
        novoID();
        carregarLista();
    }
    
    public void novoID() {
        BancoDadosClientes = bancoCliente.carregarBanco();
        int tamanhoArray = BancoDadosClientes.size();
        jTextfieldID.setText((tamanhoArray + 1) + "");
        limpar();
    }
    
    public void limpar() {
        jTextFieldNome.setText("");
        jTextFieldNome.setBackground(Color.white);
        jButtonSalvarEditar.setText("Salvar");
    }
    
    public int pegarIndex(Cliente cliente) {
        int index = 0;
        for(Cliente cli : BancoDadosClientes) {
            if(cli.getId() == cliente.getId()) {
                break;
            }
            index++;
        }
        return index;
    }
    
    public void editar() {
        String temp = jListClientes.getSelectedValue();
        int indexInicioConsulta = temp.indexOf("(", 2);
        int indexFinalConsulta = temp.indexOf(")", 2);
        String res = temp.substring(indexInicioConsulta + 1, indexFinalConsulta);
        int id = Integer.parseInt(res);
        Cliente clienteEditar = buscar(id);
        
        jTextfieldID.setText(clienteEditar.getId()+"");
        jTextFieldNome.setText(clienteEditar.getNome());
        
        jButtonSalvarEditar.setText("Editar");
    }
    
    public boolean campoVazio(String temp) {
        return temp.isEmpty();
    }
    
    public Cliente buscar(int id) {
        for (Cliente cliente01 : BancoDadosClientes) {
            if(cliente01.getId() == id) {
                return cliente01;
            }
        }
        return null;
    }
    
    public void carregarLista() {
        listaTelaCliente = new DefaultListModel();
        ArrayList<String> ListaTelaAtualizada = new ArrayList<>();
        for (Cliente cliente01 : BancoDadosClientes) {
            ListaTelaAtualizada.add(cliente01.getNome()+" ("+cliente01.getId()+")");
        }
        Collections.sort(ListaTelaAtualizada);
        listaTelaCliente.addAll(ListaTelaAtualizada);
        jListClientes.setModel(listaTelaCliente);
    }
    
    public void salvarEditarCliente() {
        String nId = jTextfieldID.getText();
        String nome = jTextFieldNome.getText();
        boolean verificador = true;
        
        if (campoVazio(nome)) {
            JOptionPane.showMessageDialog(null, "O campo Nome não poder ser vazio");
            jTextFieldNome.setBackground(Color.red);
            verificador = false;
        }
        
        if(verificador) {
            //SALVAR
            Cliente cliente = new Cliente(Integer.parseInt(nId), nome);
            
            if (jButtonSalvarEditar.getText().compareToIgnoreCase("Salvar") == 0) {
                BancoDadosClientes.add(cliente);
            } else {
                int index = pegarIndex(cliente);
                BancoDadosClientes.set(index, cliente);
            }
            bancoCliente.salvarBanco(BancoDadosClientes);
            carregarLista();
            novoID();
        }
    }
}
