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
import model.Produto;

/**
 *
 * @author alunos
 */
public class BancoDadosProduto {
    public int salvarBanco(ArrayList<Produto> dados) {
        try {
            FileOutputStream fileStream = new FileOutputStream("BancoProdutos.minas");
            ObjectOutputStream outputStream = new ObjectOutputStream(fileStream);
            outputStream.writeObject(dados);
            outputStream.close();
            return 0;
        } catch(Exception ex) {
            ex.printStackTrace();
            return -1;
        }
    }
    
    public ArrayList<Produto> carregarBanco() {
        ArrayList<Produto> dados = new ArrayList<>();
        try {
            FileInputStream fis = new FileInputStream("BancoProdutos.minas");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Object objeto =ois.readObject();
            
            dados = (ArrayList<Produto>) objeto;
            ois.close();
            return dados;
        } catch(Exception ex) {
            ex.printStackTrace();
            return dados;
        }
    }
    
}
