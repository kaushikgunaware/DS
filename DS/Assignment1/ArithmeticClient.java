import java.rmi.Naming;
import java.util.Scanner;

public class ArithmeticClient {
    public static void main(String[] args) {
        try {
            ArithmeticService arithmeticService =
                (ArithmeticService) Naming.lookup(
                    "rmi://localhost/ArithmeticService"
                );

            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the first number: ");
            double num1 = scanner.nextDouble();

            System.out.print("Enter the second number: ");
            double num2 = scanner.nextDouble();

            System.out.println("\nChoose an operation:");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.print("Enter your choice (1-4): ");
            int choice = scanner.nextInt();

            double result = 0;
            switch (choice) {
                case 1: result = arithmeticService.add(num1, num2); break;
                case 2: result = arithmeticService.subtract(num1, num2); break;
                case 3: result = arithmeticService.multiply(num1, num2); break;
                case 4: result = arithmeticService.divide(num1, num2); break;
                default:
                    System.out.println("Invalid choice");
                    return;
            }

            System.out.println("Result: " + result);
            scanner.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}