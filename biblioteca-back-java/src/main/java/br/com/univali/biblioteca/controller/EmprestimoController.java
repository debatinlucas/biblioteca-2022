package br.com.univali.biblioteca.controller;

import br.com.univali.biblioteca.model.Emprestimo;
import br.com.univali.biblioteca.repository.EmprestimoRepository;
import java.util.Date;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/emprestimos")
public class EmprestimoController { 
    
    @Autowired
    private EmprestimoRepository emprestimoRepository;
    
    @GetMapping
    public List<Emprestimo> listarTodos() {
        return emprestimoRepository.findAll(Sort.by(Sort.Order.asc("status")));
    }
    
    @GetMapping(value="/{id}")
    public Optional<Emprestimo> listarPeloId(@PathVariable Long id) {
        return emprestimoRepository.findById(id);
    }
    
    @PostMapping
    public Emprestimo adicionar(@RequestBody Emprestimo emprestimo) {
        emprestimo.setDataRetirada(new Date());
        emprestimo.setStatus(1);
        return emprestimoRepository.save(emprestimo);
    }
    
    @PutMapping(value="/{id}")
    public ResponseEntity editar(@PathVariable Long id, @RequestBody Emprestimo emprestimo) {
        return emprestimoRepository.findById(id)
                .map(record -> {
                    record.setStatus(emprestimo.getStatus());
                    Emprestimo emprestimoUpdated = emprestimoRepository.save(record);
                    return ResponseEntity.ok().body(emprestimoUpdated);
                }).orElse(ResponseEntity.notFound().build());
    }
    
    @DeleteMapping(value="/{id}")
    public ResponseEntity deletar(@PathVariable Long id) {
        return emprestimoRepository.findById(id)
                .map(record-> {
                    emprestimoRepository.deleteById(id);
                    return ResponseEntity.ok().build();
                }).orElse(ResponseEntity.notFound().build());
    }
}
