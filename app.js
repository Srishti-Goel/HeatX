//jshint esversion:6

const express = require("express");

const https = require("https");

const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended:true}));

app.use(express.static("public"));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/views/index.html");
})

app.get("/blog", function(req, res){
  res.sendFile(__dirname + "/views/index-blog.html");
})

app.get("/community-guidelines", function(req, res){
  res.sendFile(__dirname + "/views/community-guidelines.html");
})

app.listen(3000, function(){
  console.log("Server is running on port 3000.");
})
