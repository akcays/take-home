const NUMBERS = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
};

const DIGITS = {
  10: 'ten',
  100: 'hundred',
  1000: 'thousand',
  1000000: 'million',
  1000000000: 'billion',
  1000000000000: 'trillion',
  1000000000000000: 'quadrillion',
  1000000000000000000: 'quintillion',
};

module.exports = function numberInEnglish(num) {
  let digit, numberInDigit, numberLeft, restOfString, output;
  let isNegative = num < 0 ? true : false;
  let number = Math.abs(num);

  if (NUMBERS[number]) {
    // numbers less than 20 or divisible by 10 are predefined
    output = NUMBERS[number];
  } else if (number < 100) {
    // numbers less than 100 are a multiple of 10 and a single digit
    numberInDigit = Math.floor(number / 10);
    numberLeft = number % 10;
    // if we have 98, first part will generate 'ninety' second part will handle eight
    output = NUMBERS[numberInDigit * 10] + ' ' + numberInEnglish(numberLeft);
  } else {
    // all other numbers are a combination of a number we can write, and a digit name
    if (number < 1000) {
      // the hundreds digit is special
      digit = 100;
    } else {
      // all other digits are a multiple of 1000
      digit = 1000;
      while (digit * 1000 <= number) {
        digit *= 1000;
      }
    }
    numberInDigit = Math.floor(number / digit);
    numberLeft = number % digit;
    // assemble the 1000s digit
    output = numberInEnglish(numberInDigit) + ' ' + DIGITS[digit];
    // assemble the rest of the number
    restOfString = numberInEnglish(numberLeft);
    // prevent having an output such as 'hundred zero'
    if (restOfString !== 'zero') {
      output += ' ' + restOfString;
    }
  }
  return isNegative ? 'negative ' + output : output;
};
