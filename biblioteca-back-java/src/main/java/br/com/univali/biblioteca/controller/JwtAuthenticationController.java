package br.com.univali.biblioteca.controller;

import br.com.univali.biblioteca.config.JwtTokenUtil;
import br.com.univali.biblioteca.model.JwtRequest;
import br.com.univali.biblioteca.model.JwtResponse;
import br.com.univali.biblioteca.model.Usuario;
import br.com.univali.biblioteca.repository.UsuarioRepository;
import br.com.univali.biblioteca.service.JwtUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.DisabledException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
@CrossOrigin
public class JwtAuthenticationController {

    @Autowired
    private UsuarioRepository usuarioRepository;
    
    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private JwtTokenUtil jwtTokenUtil;

    @Autowired
    private JwtUserDetailsService userDetailsService;

    @RequestMapping(value = "/api/login", method = RequestMethod.POST)
    public ResponseEntity<?> createAuthenticationToken(@RequestBody JwtRequest authenticationRequest) {
        try {
            authenticate(authenticationRequest.getUsername(), authenticationRequest.getPassword());
            final UserDetails userDetails = userDetailsService
                    .loadUserByUsername(authenticationRequest.getUsername());
            final String token = jwtTokenUtil.generateToken(userDetails);
            return ResponseEntity.ok(new JwtResponse(token));
        } catch (Exception e) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "USUARIO_INCORRETO");
        }
    }
    
    @RequestMapping(value = "/api/signup", method = RequestMethod.POST)
    public ResponseEntity<?> adicionar(@RequestBody Usuario usuario) {
        try {
            BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
            String senha = usuario.getSenha();
            usuario.setSenha(encoder.encode(usuario.getSenha()));

            Usuario usuarioSave = usuarioRepository.save(usuario);
            authenticate(usuarioSave.getEmail(), senha);
            final UserDetails userDetails = userDetailsService
                    .loadUserByUsername(usuarioSave.getEmail());
            final String token = jwtTokenUtil.generateToken(userDetails);
            return ResponseEntity.ok(new JwtResponse(token));
        } catch (Exception e) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "EMAIL_DUPLICADO");
        }
    }

    private void authenticate(String username, String password) throws Exception {
        try {
            authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(username, password));
        } catch (DisabledException e) {
            throw new Exception("USER_DISABLED", e);
        } catch (BadCredentialsException e) {
            throw new Exception("INVALID_CREDENTIALS", e);
        }
    }
}
