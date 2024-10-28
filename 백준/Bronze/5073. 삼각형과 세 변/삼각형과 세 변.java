import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            if (x == 0 && y == 0 && z == 0)
                break;

            System.out.println(checkLength(x, y, z));
        }

    }

    public static String checkLength(int x, int y, int z){
        int[] triangle = {x, y, z};
        Arrays.sort(triangle);
        if (x==y && y==z)
            return "Equilateral";
        else if (triangle[2] >= triangle[0] + triangle[1])
            return "Invalid";
        else if (x == y || y == z || x == z)
            return "Isosceles";
        else
            return "Scalene";
    }
}
