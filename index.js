const express = require("express");
const getAppendingData = require("./content/content");
var bodyParser = require("body-parser");
const PythonShell = require("python-shell").PythonShell;
const app = express();
const fs = require("fs");
let messages = [];
app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: false,
  })
);

app.use(express.static("public"));

app.post("/api/",(req, res) => {
  if (req.body.code === undefined){
    return res.status(400).send("Bad Request")
  }
  global.result = null
  try {
    const appendingData = getAppendingData();
    // const current = fs.readFileSync("temp.py", "utf8");
    const data = `${appendingData[0]}codetotest="""\n${req.body.code}\n"""${appendingData[1]}`;
    // const data = `${appendingData[0]}codetotest="""\n${current}\n"""${appendingData[1]}`;
    fs.writeFileSync("current.py", data);
  } catch (err) {
    console.error(err)
  }

  const pyshell = new PythonShell("current.py");

  pyshell.on("message", function (message) {
    messages.push(message)
  });

  pyshell.end(function (err) {
    if (err) {
      return res.json({result: err.traceback})
    } else {
      res.json({result: messages.join("\n")})
      messages = []
    }
  });
 
});

app.listen(3000);
