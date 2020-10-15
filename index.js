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

app.use((req,res,next) => {
  res.header('Access-Control-Allow-Origin','*')
  res.header('Access-Control-Allow-Headers','Content-Type,Authorization')
  res.header('Access-Control-Allow-Methods','GET,PUT,POST,DELETE')
  next()
})

app.post("/api/",(req, res) => {
  messages=[]
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

  setTimeout(()=>{
    pyshell.kill()
    messages = ["TLE ERROR!!!"]
  },5000)

  pyshell.on("message", function (message) {
    messages.push(message)
  });

  pyshell.end(function (err) {
    if (err) {
      return res.json({result: err.traceback})
    } else {
      return res.json({result: messages.join("\n")})
    }
  });
});

app.listen(3000);
