import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        if (n % 2 == 0){
            System.out.println("CY");
        }else {
            System.out.println("SK");
        }
    }
}