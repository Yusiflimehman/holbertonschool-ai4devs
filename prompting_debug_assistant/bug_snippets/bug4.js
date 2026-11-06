function checkAge(age) {
    // Intentional Logical error
    if (age = 18) {
        return "User is adult";
    }
    return "User is minor";
}

console.log(checkAge(15));
