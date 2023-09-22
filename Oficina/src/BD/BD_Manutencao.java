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
import model.Manutencao;

/**
 *
 * @author alunos
 */
public class BD_Manutencao {
    
    public int salvarBanco(ArrayList<Manutencao> dados){
        try{
            FileOutputStream fs = new FileOutputStream("ManuBanco.txt");
            ObjectOutputStream os = new ObjectOutputStream(fs);
            os.writeObject(dados);
            os.close();
            return 0;
        } catch (Exception ex) {
            ex.printStackTrace();
            return -1;
        }
    }
    
    public ArrayList<Manutencao> carregarBanco() {
        ArrayList<Manutencao> manuBD = new ArrayList<>();
        try {
            FileInputStream fis = new FileInputStream("ManuBanco.txt");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Object ob = ois.readObject();
            
            manuBD = (ArrayList<Manutencao>) ob;
            ois.close();
            return manuBD;
        } catch (Exception ex) {
            ex.printStackTrace();
            return manuBD;
        }
    }
    
}
