const express = require("express");
const bodyParser = require("body-parser")
const app = express();
const spawn = require("child_process").spawn;
const spawn2 = require("child_process").spawn;
  
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");
})

app.post("/", function(req,res){

  console.log("Going to python");
  const pythonProcess = spawn('python', ['./modis.py', req.body.lat, req.body.long]);
    pythonProcess.stdout.on('data', (data) => {
      dataStr = data.toString().split('\r\n');
      console.log("Param data: ", dataStr);
      NDVI = (parseFloat(dataStr[0]));
      LST = (parseFloat(dataStr[1]));
      ta = (parseFloat(dataStr[2]));

      const pythonProcess2 = spawn('python', ['./calc_risk.py', NDVI, LST, ta]);
      pythonProcess2.stdout.on('data', (data) => {
      dataSTR = data.toString();
      res.write(data);
      res.send();

    })    
});
  
})

app.listen(3000, function(){
  console.log("Server is running on port 3000.");
})
