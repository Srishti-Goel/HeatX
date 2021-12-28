const express = require("express");
const bodyParser = require("body-parser");
const spawn = require("child_process").spawn;

const router = express.Router();
  
router.use(bodyParser.urlencoded({extended:true}));

router.get("/", function(req, res){
  res.sendFile(__dirname + "/calculator.html");
})

router.post("/", function(req,res){

  console.log("Going to python with", req.body);
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

module.exports = router;