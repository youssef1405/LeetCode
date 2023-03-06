// O(N) and O(1) solutions

/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function (low, high) {
  // O(N) solution
  //let oddCount = 0;
  // for (let i=low; i<=high; i++){
  //     if (i % 2 !== 0) oddCount++
  // }
  // return oddCount;

  // O(1) solution
  if (low % 2 == 0) low += 1;
  if (high % 2 == 0) high -= 1;
  return (high - low) / 2 + 1;
};
