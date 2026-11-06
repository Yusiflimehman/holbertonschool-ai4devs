function checkAge(age) {
    if (age >= 18) {
        return "User is adult";
    }
    return "User is minor";
}

const testAdult = checkAge(20);
const testMinor = checkAge(15);
console.log("Adult Test:", testAdult);
console.log("Minor Test:", testMinor);
if (testAdult !== "User is adult" || testMinor !== "User is minor") {
    throw new Error("Age validation test failed");
}
