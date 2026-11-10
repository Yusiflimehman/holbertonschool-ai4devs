package bug_snippets;

import java.util.ArrayList;
import java.util.List;

public class Bug3 {

    public static List<String> removeShortStrings(List<String> strings, int minLength) {
        // minLength-dən qısa olan mətnləri siyahıdan silmək nəzərdə tutulub
        for (int i = 0; i < strings.size(); i++) {
            if (strings.get(i).length() < minLength) {
                strings.remove(i);
            }
        }
        return strings;
    }

    public static boolean compareUserIds(Integer id1, Integer id2) {
        // İki Integer obyektini bərabərlik üçün müqayisə edir
        return id1 == id2;
    }

    public static void main(String[] args) {
        List<String> words = new ArrayList<>(List.of("a", "b", "hello", "c", "world"));
        System.out.println("Filtrlənmiş: " + removeShortStrings(words, 3));
        
        Integer a = 200;
        Integer b = 200;
        System.out.println("İD-lər uyğundur: " + compareUserIds(a, b));
    }
}
