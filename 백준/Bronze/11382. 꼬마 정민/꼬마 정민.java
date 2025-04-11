import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] num = br.readLine().split(" ");

        br.close();

        System.out.println(Long.parseLong(num[0]) + Long.parseLong(num[1]) + Long.parseLong(num[2]));
    }
}