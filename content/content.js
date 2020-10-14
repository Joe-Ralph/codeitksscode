const fs = require("fs");
const path = require("path");
let beginData = null;
let endData = null;

const getAppendingData = () => {
  try {
    const beginData = fs.readFileSync("content/begin.py", "utf8");
    const endData = fs.readFileSync("content/end.py", "utf8");
    return [beginData, endData];
  } catch (err) {
    console.error(err);
  }
};

module.exports = getAppendingData;
