/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package BancoDados;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import model.Cliente;

/**
 *
 * @author alunos
 */
public class BancoDadosCliente {
    public int salvarBanco(ArrayList<Cliente> dados) {
        try {
            FileOutputStream fileStream = new FileOutputStream("BancoCliente.minas");
            ObjectOutputStream outputStream = new ObjectOutputStream(fileStream);
            outputStream.writeObject(dados);
            outputStream.close();
            return 0;
        } catch(Exception ex) {
            ex.printStackTrace();
            return -1;
        }
    }
    
    public ArrayList<Cliente> carregarBanco() {
        ArrayList<Cliente> dados = new ArrayList<>();
        try {
            FileInputStream fis = new FileInputStream("BancoCliente.minas");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Object objeto =ois.readObject();
            
            dados = (ArrayList<Cliente>) objeto;
            ois.close();
            return dados;
        } catch(Exception ex) {
            ex.printStackTrace();
            return dados;
        }
    }
    
}
