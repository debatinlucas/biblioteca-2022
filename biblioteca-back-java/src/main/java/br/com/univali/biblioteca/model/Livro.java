package br.com.univali.biblioteca.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import java.util.List;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import lombok.Data;

@Data
@Entity
public class Livro {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @JsonIgnore
    @ManyToMany(mappedBy = "livros")
    private List<Emprestimo> emprestimos;
    
    @Column(nullable = false, length=100)
    private String titulo;
    
    @Column(length=500)
    private String resumo;
}
