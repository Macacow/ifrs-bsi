/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.io.Serializable;

/**
 *
 * @author alunos
 */
public class Carro implements Serializable{
    int id;
    String placa;
    int kms;

    public Carro() {
    }

    public Carro(int id, String placa, int kms) {
        this.id = id;
        this.placa = placa;
        this.kms = kms;
    }
    
    
    public int getId() {
        return id;
    }

    public String getPlaca() {
        return placa;
    }

    public int getKms() {
        return kms;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public void setKms(int kms) {
        this.kms = kms;
    }

    
    
}
