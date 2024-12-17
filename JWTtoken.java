import java.security.SecureRandom;
import java.util.Base64;

public class JWTtoken {
    public static void main(String[] args) {
        SecureRandom secureRandom = new SecureRandom();
        byte[] key = new byte[32];
        secureRandom.nextBytes(key);
        String encodedKey = Base64.getEncoder().encodeToString(key);
        System.out.println("Generated Secret Key: " + encodedKey);
    }
}
