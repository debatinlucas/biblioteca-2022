package br.com.univali.biblioteca.service;

import br.com.univali.biblioteca.model.Usuario;
import br.com.univali.biblioteca.repository.UsuarioRepository;
import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class JwtUserDetailsService implements UserDetailsService {

	@Autowired
    private UsuarioRepository usuarioRepository;
	
	@Override
	public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
		Optional<Usuario> usuarioResponse = usuarioRepository.findByEmail(email);
                Usuario usuario = usuarioResponse.get();
		
		if (usuario.getEmail().equals(email)) {
			return new User(email, usuario.getSenha(),
					new ArrayList<>());
		} else {
			throw new UsernameNotFoundException("usuário não encontrado - email: " + email);
		}
	}
}