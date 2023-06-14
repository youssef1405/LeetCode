romans = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const romanToInt = (s) => {
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    s[i + 1] && romans[s[i]] < romans[s[i + 1]]
      ? (result -= romans[s[i]])
      : (result += romans[s[i]]);
  }
  return result;
};
