const express = require("express");
const bodyParser = require("body-parser")
const app = express();
const spawn = require("child_process").spawn;
  
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");
})

app.post("/", function(req,res){

  console.log("Going to python");
  console.log(req.body);
    const calculateNDVIProcess = spawn('python', ['./modis.py']);
    calculateNDVIProcess.on('data', (data) => {
      console.log('From MODIS: ', data.toString());
    })


    NDVI = 1;
    LST = 35;
    ta = 1;

    const pythonProcess = spawn('python', ['./calc_risk.py', NDVI, LST, ta]);
    pythonProcess.stdout.on('data', (data) => {
    console.log(data.toString());
    res.write(data);
    res.send();
});
    
})

app.listen(3000, function(){
  console.log("Server is running on port 3000.");
})