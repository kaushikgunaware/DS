// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ArithmeticServiceImpl extends UnicastRemoteObject implements ArithmeticService {
   public ArithmeticServiceImpl() throws RemoteException {
   }

   public double add(double var1, double var3) throws RemoteException {
      return var1 + var3;
   }

   public double subtract(double var1, double var3) throws RemoteException {
      return var1 - var3;
   }

   public double multiply(double var1, double var3) throws RemoteException {
      return var1 * var3;
   }

   public double divide(double var1, double var3) throws RemoteException {
      if (var3 == 0.0) {
         throw new RemoteException("Cannot divide by zero");
      } else {
         return var1 / var3;
      }
   }
}