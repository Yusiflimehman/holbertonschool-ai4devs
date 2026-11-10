public class UserAuthenticator {

    public static boolean authenticate(String inputPassword, String storedPassword) {
        // Bug: Using '==' instead of '.equals()' for String comparison
        if (inputPassword == storedPassword) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String input = new String("secret123");
        String stored = "secret123";

        // Expected: true, Actual: false due to memory reference check
        System.out.println("Authenticated: " + authenticate(input, stored));
    }
}
