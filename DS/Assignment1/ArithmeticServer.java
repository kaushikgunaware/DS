import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ArithmeticServer {
    public static void main(String[] args) {
        try {
            // Start RMI registry on default port 1099
            LocateRegistry.createRegistry(1099);

            ArithmeticServiceImpl arithmeticService = new ArithmeticServiceImpl();

            // Bind service
            Naming.rebind("rmi://localhost/ArithmeticService", arithmeticService);

            System.out.println("Arithmetic Server is ready...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

