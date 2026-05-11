package saludo_springboot.controller;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/saludo")
public class SaludoController {
    @GetMapping
    public String saludoGet() {
        return "Hola, bienvenido a springboot";
    }
    @PostMapping
    public String saludoPost(@RequestBody String nombre) {
        return "Hola "+ nombre + " bienvenido";
    }

}
