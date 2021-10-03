const express = require("express");
const https = require("https");
const bodyParser = require("body-parser")
const app = express();
const spawn = require("child_process").spawn;
  
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");
})

app.post("/", function(req,res){
    NDVI = req.body.NDVI;
    LST = req.body.LST;
    ta = req.body.ta;

    const pythonProcess = spawn('python', ['./calc_risk.py']);
    pythonProcess.stdout.on('data', (data) => {
    console.log(data.toString());
    res.write(data);
    res.send();
});
    
})

app.listen(3000, function(){
  console.log("Server is running on port 3000.");
})