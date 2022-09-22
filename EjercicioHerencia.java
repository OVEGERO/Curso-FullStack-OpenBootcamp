public class EjercicioHerencia {

    public static void main(String[] args) {

        Cliente cliente = new Cliente( "Jhon", 21, "13981312", 21.69 );
        System.out.println(cliente.toString());

        Trabajador trabajador = new Trabajador( "Mauricio", 31, "1113981312", 3000.00 );
        System.out.println(trabajador.toString());
    }
}


class Persona{
    String nombre;
    int edad;
    String telefono;

    public Persona(String nombre, int edad, String telefono){
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
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

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", edad=" + edad +
                ", telefono='" + telefono + '\'' +
                '}';
    }
}

class Cliente extends Persona{
    double credito;


    public Cliente(String nombre, int edad, String telefono, double credito) {
        super(nombre, edad, telefono);
        this.credito = credito;
    }

    public double getCredito() {
        return credito;
    }

    public void setCredito(double credito) {
        this.credito = credito;
    }

    @Override
    public String toString() {
        return super.toString() +" " + "Cliente{" +
                "credito=" + credito +
                '}';
    }
}

class Trabajador extends Persona{
    double sueldo;

    public Trabajador(String nombre, int edad, String telefono, double sueldo) {
        super(nombre, edad, telefono);
        this.sueldo = sueldo;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        return super.toString() +" " + "Trabajador{" +
                "sueldo=" + sueldo +
                '}';
    }
}
