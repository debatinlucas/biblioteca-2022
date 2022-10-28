package br.com.univali.biblioteca.controller;

import br.com.univali.biblioteca.config.JwtTokenUtil;
import br.com.univali.biblioteca.model.JwtResponse;
import br.com.univali.biblioteca.model.Usuario;
import br.com.univali.biblioteca.repository.UsuarioRepository;
import br.com.univali.biblioteca.service.JwtUserDetailsService;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.DisabledException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {
    
    @Autowired
    private UsuarioRepository usuarioRepository;
    
    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Autowired
    private JwtUserDetailsService userDetailsService;
    
    @GetMapping
    public List<Usuario> listarTodos() {
        return usuarioRepository.findAll();
    }
    
    @GetMapping(value="/{id}")
    public Optional<Usuario> listarPeloId(@PathVariable Long id) {
        return usuarioRepository.findById(id);
    }
    
    @PostMapping
    public Usuario adicionarUsuario(@RequestBody Usuario usuario) {
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
        usuario.setSenha(encoder.encode(usuario.getSenha()));
        return usuarioRepository.save(usuario);
    }
    
    @PutMapping(value="/{id}")
    public ResponseEntity editar(@PathVariable Long id, @RequestBody Usuario usuario) {
        if (usuario.getSenha() != null) {
            BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
            usuario.setSenha(encoder.encode(usuario.getSenha()));
        } else {
            Usuario usuarioAux = usuarioRepository.findById(id).get();
            usuario.setSenha(usuarioAux.getSenha());
        }
        return usuarioRepository.findById(id)
                .map(record -> {
                    record.setNome(usuario.getNome());
                    record.setEmail(usuario.getEmail());
                    record.setSenha(usuario.getSenha());
                    Usuario usuarioUpdated = usuarioRepository.save(record);
                    return ResponseEntity.ok().body(usuarioUpdated);
                }).orElse(ResponseEntity.notFound().build());
    }
    
    @DeleteMapping(value="/{id}")
    public ResponseEntity deletar(@PathVariable Long id) {
        return usuarioRepository.findById(id)
                .map(record-> {
                    usuarioRepository.deleteById(id);
                    return ResponseEntity.ok().build();
                }).orElse(ResponseEntity.notFound().build());
    }
}
