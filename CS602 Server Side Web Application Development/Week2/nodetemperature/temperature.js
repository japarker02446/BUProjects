// Use the readline module to read from stdin.
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter a temperature value:', (value) => {
    rl.question('Please enter a starting temperature scale number:\n[1] Fahrenheit\n[2] Celsius\n[3] Kelvin:\n', (scale) =>{
        
        var farValue;
        var celValue;
        var kelValue;

        switch(scale){
            // from Farhenheit
            case "1":
                farValue = value;
                celValue = (value - 32) * (5/9);
                kelValue = ((value - 32) * (5/9)) + 273.15;
                break;
            // from Celsius
            case "2":
                farValue = (value * 9/5) + 32;
                celValue = value;
                kelValue = Number(value + 273.15);
                break;
            // from Kelvin
            case "3":
                farValue = (value - 273.15) * (9/5) + 32;
                celValue = (value - 273.15);
                kelValue = value;
                break;
            default:
                rl.write('Please enter a valid value: 1, 2 or 3\n');
        }
        
        rl.write('The converted values are:\n');
        rl.write(Number(farValue).toFixed(2) + " °F\n");
        rl.write(Number(celValue).toFixed(2) + " °C\n");
        rl.write(Number(kelValue).toFixed(2) + " K\n");

        rl.close();
    })
})