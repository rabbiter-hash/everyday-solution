
function isLeapYear(year){
    /*
     Check if the given year is a leap year
     :conditions:
        // 1. year is a positive integer
        // 2. year can be divided by 4 but not 100;
        // 3. year can be divided by 400;
      :param year: positive integer
      :return: Boolean
     */

    // 1. year must be positive integer
    if((typeof year!=='number') || (!Number.isInteger(year)) || (year <= 0)) {
        return false;
    }
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}