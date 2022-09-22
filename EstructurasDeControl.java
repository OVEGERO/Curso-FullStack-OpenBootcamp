public class EstructurasDeControl {

    public static void main(String[] args) {


        //IF
        int numero = 1;

        if(numero > 0 ){
            System.out.println("Numero positivo");
        }else if (numero < 0){
            System.out.println("Numero negativo");
        }else{
            System.out.println("Numero igual a 0");
        }


        //WHILE
        int numeroWhile = 0;
        while(numeroWhile < 3){
            System.out.println("numeroWhile = " + numeroWhile);
            numeroWhile++;
        }


        //DO WHILE
        int numeroDoWhile = 0;
        do{
            System.out.println("numeroDoWhile = " + numeroDoWhile);
            numeroDoWhile++;
        }while(numeroDoWhile != 1);


        //FOR
        int numeroFor = 0;
        for(; numeroFor < 3; numeroFor++){
            System.out.println("numeroFor = " + numeroFor);
        }


        //SWITCH
        String estacion = "";
        switch(estacion){
            case "Invierno":
                System.out.println("estación = " + estacion);
                break;

            case "Verano":
                System.out.println("estación = " + estacion);
                break;

            case "Otoño":
                System.out.println("estación = " + estacion);
                break;

            case "Primavera":
                System.out.println("estación = " + estacion);
                break;

            default:
                System.out.println("Esa estación no existe");
        }



    }

}
