import CalculatorApp.*;
import org.omg.CORBA.*;
import org.omg.CosNaming.*;

public class CalculatorClient {
    public static void main(String args[]) {
        try {
            // Initialize ORB
            ORB orb = ORB.init(args, null);

            // Get reference to Naming Service
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            // Resolve Calculator object
            Calculator calculator = CalculatorHelper.narrow(ncRef.resolve_str("Calculator"));

            // Perform operations
            System.out.println("Addition (10 + 5): " + calculator.add(10, 5));
            System.out.println("Subtraction (10 - 5): " + calculator.subtract(10, 5));
            System.out.println("Multiplication (10 * 5): " + calculator.multiply(10, 5));

            try {
                System.out.println("Division (10 / 2): " + calculator.divide(10, 2));
                System.out.println("Division (10 / 0): " + calculator.divide(10, 0)); // Should raise exception
            } catch (DivisionByZero e) {
                System.out.println("Error: Division by zero is not allowed!");
            }

        } catch (Exception e) {
            System.err.println("Client exception: " + e.getMessage());
            e.printStackTrace();
        }
    }
}