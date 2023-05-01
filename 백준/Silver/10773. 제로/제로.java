import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(bf.readLine());
        for (int i = 0; i <n ; i++) {
            int x = Integer.parseInt(bf.readLine());
            if (x != 0){
                stack.push(x);
            } else if (x == 0 & !stack.isEmpty()) {
                stack.pop();
            }
        }
        int sum = 0;
        while (!stack.isEmpty()){
            sum += stack.pop();
        }
        System.out.println(sum);
    }
}
