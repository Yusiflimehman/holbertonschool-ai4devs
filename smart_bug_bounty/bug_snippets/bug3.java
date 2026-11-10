public class StringUtils {
    /**
     * Utility method to compare two string inputs.
     * Intended to check equal content value.
     */
    public static boolean compareStrings(String str1, String str2) {
        if (str1 == null || str2 == null) {
            return false;
        }
        
        // Bug: Using reference comparison instead of value comparison (.equals)
        return str1 == str2;
    }
}
