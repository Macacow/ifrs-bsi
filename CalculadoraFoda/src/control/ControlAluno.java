/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package control;

import javax.swing.JTextField;
import javax.swing.JTextArea;
import model.Aluno;

/**
 *
 * @author alunos
 */
public class ControlAluno {
    JTextField nome;
    JTextField nota1;
    JTextField nota2;
    JTextArea saida;

    public ControlAluno(JTextField nome, JTextField idade, JTextField nota1, JTextField nota2, JTextField nota3, JTextArea saida) {
        this.nome = nome;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.saida = saida;
    }
    
    public void criarAluno(){
        Aluno aluno1 = new Aluno(nome.getText(), Float.parseFloat(nota1.getText()), Float.parseFloat(nota2.getText()));
        float resultado = calcularMedia(aluno1);
        
        if(resultado >= 7){
            //Aprovado
            saida.setText(aluno1.getNome() + ": Aprovado | " + resultado);
        } else{
            saida.setText(aluno1.getNome() + ": Reprovado | " + resultado);
        }
        
        
    }
    
    public float calcularMedia(Aluno x){
        float media = (x.getNota1() + x.getNota2())/2;
        return media;
    }
}
