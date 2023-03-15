/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  const len1 = str1.length;
  const len2 = str2.length;

  const isDivisor = (l) => {
    if (len1 % l || len2 % l) return false;
    let rep1 = len1 / l,
      rep2 = len2 / l;
    return (
      str1 === str1.slice(0, l).repeat(rep1) &&
      str2 === str1.slice(0, l).repeat(rep2)
    );
  };

  for (let l = Math.min(len1, len2); l >= 1; l--) {
    if (isDivisor(l)) {
      return str1.slice(0, l);
    }
  }
  return '';
};
