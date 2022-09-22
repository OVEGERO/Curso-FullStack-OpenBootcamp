package ola;

public class Main {

    public static void main(String[] args) {

        Persona persona = new Persona();
        persona.setNombre("Jhon");
        persona.setEdad(21);
        persona.setTelefono("91274891264");
        Persona persona2 = new Persona();
        persona2.setNombre("Isabel");
        persona2.setEdad(20);
        persona2.setTelefono("912742312891264");

        System.out.println("Nombre: " + persona.getNombre() + " " + " Edad: " + persona.getEdad() + " " + " Telefono: " + persona.getTelefono());
        System.out.println("Nombre: " + persona2.getNombre() + " " + " Edad: " + persona2.getEdad() + " " + " Telefono: " + persona2.getTelefono());


    }

}

class Persona{

    private String nombre;
    private int edad;
    private String telefono;

    public Persona(){
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

}
