public class StringUtils {
    /**
     * Compares two strings for content equality.
     * Handles null values safety checks.
     */
    public static boolean compareStrings(String str1, String str2) {
        if (str1 == null || str2 == null) {
            return false;
        }
        // Bug: Reference comparison used instead of content equality check
        boolean isEqual = (str1 == str2);
        System.out.println("Comparison result: " + isEqual);
        return isEqual;
    }
}
