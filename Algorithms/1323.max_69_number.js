function maximum69Number(num) {
  let numStr = num.toString();
  let res = '';
  for (let i = 0; i < numStr.length; i++) {
    if (numStr[i] === '6') {
      res += '9';
      res += numStr.substring(i + 1);
      break;
    }
    res += numStr[i];
  }
  return parseInt(res);
}

// consice solution
const maximum69Number = (num) => parseInt(num.toString().replace('6', '9'));
