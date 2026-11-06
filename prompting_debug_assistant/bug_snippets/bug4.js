function checkAge(age) {
    // Function to check user eligibility based on age input
    console.log("Validating user age:", age);
    
    // Intentional Logical error: assignment operator '=' used instead of strict comparison '==='
    if (age = 18) {
        return "User is adult and access granted";
    } else {
        return "User is minor and access denied";
    }
}

const inputAge = 15;
const validationMessage = checkAge(inputAge);
console.log("Verification status:", validationMessage);
