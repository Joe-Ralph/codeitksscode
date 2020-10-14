const express = require("express")
const getAppendingData = require("./content/content")
const PythonShell = require("python-shell").PythonShell
const app = express()
const fs = require("fs")


app.use(express.static("public"))


try {
  const appendingData = getAppendingData()
  const current = fs.readFileSync("temp.py", "utf8")
  const data = appendingData[0] + current + appendingData[1]
  fs.writeFileSync("current.py", data)
} catch (err) {
  console.error(err)
}


const pyshell = new PythonShell("current.py")

pyshell.on("message", function (message) {
  console.log(message)
})

pyshell.end(function (err) {
  if (err) {
    console.log(err)
  }
})

app.listen(3000)