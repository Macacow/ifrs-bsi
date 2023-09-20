/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package BD;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import model.Carro;

/**
 *
 * @author alunos
 */
public class BD_Carro {
    
    public int salvarBanco(ArrayList<Carro> dados){
        try{
            FileOutputStream fs = new FileOutputStream("CarrosBanco.txt");
            ObjectOutputStream os = new ObjectOutputStream(fs);
            os.writeObject(dados);
            os.close();
            return 0;
        } catch (Exception ex) {
            ex.printStackTrace();
            return -1;
        }
    }
    
    public ArrayList<Carro> carregarBanco() {
        ArrayList<Carro> carrosBD = new ArrayList<>();
        try {
            FileInputStream fis = new FileInputStream("CarrosBanco.txt");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Object ob = ois.readObject();
            
            carrosBD = (ArrayList<Carro>) ob;
            ois.close();
            return carrosBD;
        } catch (Exception ex) {
            ex.printStackTrace();
            return carrosBD;
        }
    }
    
}
