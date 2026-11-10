import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Bug3 {

    // Count how many times `target` appears in the list
    static int countOccurrences(List<String> words, String target) {
        int count = 0;
        for (String word : words) {
            if (word.equals(target)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        List<String> words = new ArrayList<>();
        Scanner scanner = new Scanner("apple banana apple cherry apple");
        while (scanner.hasNext()) {
            words.add(scanner.next());
        }
        scanner.close();

        String target = new String("apple");
        System.out.println("apple appears " + countOccurrences(words, target) + " times");
    }
}
